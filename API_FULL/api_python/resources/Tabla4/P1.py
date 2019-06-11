import json
import os
import time
import telnetlib
from ..Util.Notifications import Notifications
from flask import Flask, request, jsonify, url_for
from werkzeug.datastructures import ImmutableMultiDict
from flask_restful import Resource, Api

ALOWED_EXTENSIONS = set(['txt'])
user = "humberto"
password = "123456"
show = "show version"
salir = "exit"
espacio = " "

class T4_P1(Resource):
    def post(self):
        data = ImmutableMultiDict(request.form)
        data.to_dict(flat=False)
        file = request.files['file']
        emails = [data['email']]
        numbers = [data['number']]
        resptPP = getInfoHardware(file)
        message = message_formater(resptPP)
        notify_email(emails,message)
        #notify_whatsapp(numbers,message)
        return jsonify(resptPP)

def allowed_file(file_name):
    raise '.' in file_name and file_name.rsplit('.',1)[1] in ALOWED_EXTENSIONS

def file_json_IP(file):
    return [{'ip': ip.rstrip('\n'),'fecha': '','hostname':'','info': ''} for ip in file]

def getInfoHardware(file):
    json_build = file_json_IP(file)
    counter = 0
    for ip in json_build:
        #Codigo
        flag = False
        try:
            tn = telnetlib.Telnet(ip['ip'],23,2)
            flag = True
        except:
            print('No fue posible la conexion con : ' + ip['ip'])
        if flag:
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(show.encode('ascii') + b"\n")
            tn.write(espacio.encode('ascii') + b"\n")

            tn.write(salir.encode('ascii') + b"\n")
            archivo = open(ip['ip'], "w+")
            archivo.write(tn.read_all().decode('ascii'))
            archivo.seek(0)
            bandera = 0
            while bandera != 1:
                cadena = archivo.readline()
                posicion = cadena.find("#")
                if posicion >= 0:
                    bandera = 1
                    cadena_final = cadena

            json_build[counter]['hostname'] = cadena_final[0:posicion]
            archivo.seek(0)
            bandera = 0
            while bandera != 1:
                cadena = archivo.readline()
                posicion = cadena.find("export@cisco.com.")
                if posicion >= 0:
                    posicion = archivo.tell()
                    bandera = 1

            archivo.seek(posicion)
            contenido = archivo.read()
            archivo.close()
            os.remove(ip['ip'])
            #tipo = type(contenido)

            limite = contenido.find("R1#")
            hardware = contenido[0:limite]
            json_build[counter]['info'] = hardware

        t = time.localtime()
        current_time = time.strftime("%d/%m/%y %H:%M:%S", t)
        json_build[counter]['fecha'] = current_time
        counter += 1
    return json_build

def message_formater(json_resp):
    message = 'Se obtuvo la informacion de las siguientes ip:\n'
    for ip in json_resp:
        if ip['info'] != '':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] +'\n\t' + 'info: ' + ip['info']
    message += '\nLas ip que no respondieron son:\n'
    for ip in json_resp:
        if ip['info'] == '':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] + '\n'
    return message

def notify_email(emails, message):
    notify = Notifications()
    notify.sendEmail(emails,'Informacion router',message)

def notify_whatsapp(numbers, message):
    notify = Notifications()
    notify.sendWhatsApp(message,numbers)
