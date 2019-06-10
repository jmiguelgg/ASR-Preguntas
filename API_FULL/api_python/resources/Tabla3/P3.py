import socket
from ..Util.Notifications import Notifications
#from pyasn1.codec.ber import decoder
from flask import Flask, request, jsonify, url_for
from flask_restful import Resource, Api
from threading import Thread, Event
from multiprocessing.pool import ThreadPool
import time
import select
import os

stop_it = Event()
carpetaCompartida = "/Volumes/R3/"
carpetas = ["10.3.200.1","10.1.200.1","10.3.200.2","10.4.200.2","10.6.200.2","10.8.200.2","10.9.200.2","10.10.200.1","10.13.200.2","10.5.200.1","10.5.200.2"]

def escuchaCarpeta(carpeta,otro):
    data = []
    contendio_original = os.listdir(carpetaCompartida+carpeta)
    counter = 0
    while True:
        contendio_original.sort()
        tamanio_or = len(contendio_original)

        contenido_nuevo = os.listdir(carpetaCompartida+carpeta)
        contenido_nuevo.sort()
        tamanio_nuevo = len(contenido_nuevo)

        if tamanio_or != tamanio_nuevo:
            diferencia = tamanio_nuevo - tamanio_or
            if tamanio_or == 0:
                recorrido = 0
                while recorrido != diferencia:
                    #print('El pedo1 ' + carpetaCompartida + carpeta + "/" + contenido_nuevo[recorrido])
                    archivo_syslog = open(r"" + carpetaCompartida+ carpeta + "/" + contenido_nuevo[recorrido], "r")
                    syslog = archivo_syslog.read()
                    nivel = obtenerNivel(syslog)
                    reinicio = obtenerReinicio(syslog)
                    ip = obtenerIP(syslog)
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    counter += 1
                    data.append({'id':counter,'ip':ip,'nivel':nivel,'fecha':current_time,'syslog':syslog,'reinicio':reinicio})
                    recorrido = recorrido + 1
                    archivo_syslog.close()
                
                contendio_original = contenido_nuevo

            else:
                recorrido = tamanio_or
                while recorrido != tamanio_nuevo:
                    #print('El pedo2 ' + carpetaCompartida + carpeta + "/" + contenido_nuevo[recorrido])
                    archivo_syslog = open(r"" + carpetaCompartida + carpeta + "/" + contenido_nuevo[recorrido], "r")
                    syslog = archivo_syslog.read()
                    nivel = obtenerNivel(syslog)
                    reinicio = obtenerReinicio(syslog)
                    ip = obtenerIP(syslog)
                    data.append({'syslog':syslog,'nivel':nivel,'reinicio':reinicio,'ip':ip})
                    recorrido = recorrido + 1
                    archivo_syslog.close()
                
                contendio_original = contenido_nuevo
        if stop_it.is_set():
            break
    return data

def obtenerNivel(syslog):
    posicion = syslog.find("%")
    bandera = 0
    while bandera != 1:
        if syslog[posicion].isdigit() == True:
            nivel = int(syslog[posicion])
            bandera = 1
        else:
            posicion = posicion + 1

    if nivel == 0:
        cadena = " [ NIVEL 0 ] --> [ EMERGENCIA ] \n "
    elif nivel == 1:
        cadena = " [ NIVEL 1 ] --> [ ALERTA ] \n "
    elif nivel == 2:
        cadena = " [ NIVEL 2 ] --> [ CRITICA ] \n "
    elif nivel == 3:
        cadena = " [ NIVEL 3 ] --> [ ERROR ] \n "
    elif nivel == 4:
        cadena = " [ NIVEL 4 ] --> [ WARNING ] \n "
    elif nivel == 5:
        cadena = " [ NIVEL 5 ] --> [ NOTIFICACION ] \n "
    elif nivel == 6:
        cadena = " [ NIVEL 6 ] --> [ INFORMACION ] \n "
    elif nivel == 7:
        cadena = " [ NIVEL 7 ] --> [ DEBUG ] \n "
    
    return cadena

def obtenerReinicio(syslog):
    palabra = "STARTSTOP"
    posicion = syslog.find(palabra)
    if posicion >= 0:
        reinicio = 1
    else:
        reinicio = 0
    return reinicio

def obtenerIP(syslog):
    inicio = syslog.find("-05:00 ")
    inicio = inicio + 7
    aux = inicio
    while syslog[aux] != ':':
        aux = aux + 1
    
    fin = aux
    ip = syslog[inicio:fin - 2]
    print (ip)
    return ip

def notify_All(data,correo,numero,tiempo):
    message = "En un tiempo de " + str(tiempo) + " segundos "  + " se recibieron " + str(len(data)) + " Syslogs"
    notify = Notifications()
    notify.sendEmail([correo],'Syslogs',message)
    notify.sendWhatsApp(message,[numero])

class P3(Resource):
    def post(self):
        correo = request.form['correo']
        numero = request.form['numero']
        tiempo = int(request.form['tiempo'])
        result = []

        pool = ThreadPool(processes=len(carpetas))
        async_result = []
        for x in carpetas:
            async_result.append(pool.apply_async(escuchaCarpeta,(x,'hola'))) # tuple of args for foo
        time.sleep( tiempo )
        stop_it.set()
        for x in async_result:
            result.append(x.get()) # get the return value from your function.
        stop_it.clear()
        notify_All(result,correo,numero,tiempo)
        return jsonify(result)