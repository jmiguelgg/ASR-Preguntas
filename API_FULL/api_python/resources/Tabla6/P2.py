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
show1 = "conf t"
show2 = "show processes CPU"
salir = "exit"
espacio = " "

class T6_P2(Resource):
    def post(self):
        data = ImmutableMultiDict(request.form)
        data.to_dict(flat=False)
        file = request.files['file']
        emails = [data['email']]
        numbers = [data['number']]
        resptPP = getStadistics(file)
        message = message_formater(resptPP)
        notify_email(emails,message)
        #notify_whatsapp(numbers,message)
        return jsonify(resptPP)

def allowed_file(file_name):
    raise '.' in file_name and file_name.rsplit('.',1)[1] in ALOWED_EXTENSIONS

def file_json_IP(file):
    return [{'ip': ip.rstrip('\n'),'fecha': '','hostname':'','porcentaje': 0} for ip in file]

def getStadistics(file):
    json_build = file_json_IP(file)
    counter = 0
    for ip in json_build:
        #Codigo
        flag = False
        try:
            tn = telnetlib.Telnet(ip['ip'],23,1)
            flag = True
        except:
            print('No fue posible la conexion con : ' + ip['ip'])
        if flag:
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(show1.encode('ascii') + b"\n")    
            tn.write(salir.encode('ascii') + b"\n")
            tn.write(show2.encode('ascii') + b"\n")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"")
            tn.write(espacio.encode('ascii') + b"\n")    
            tn.write(salir.encode('ascii') + b"\n")

            archivo = open(ip['ip'], "w")
            archivo.write(tn.read_all().decode('ascii'))
            archivo.close()
            archivo = open(ip['ip'], "r")
            b = 0
            while b != 2:
                linea = archivo.readline()
                b = b + 1
            pos = linea.find("#")
            json_build[counter]['hostname'] = linea[0:pos]
            archivo.seek(0)
            bandera = 0
            while bandera != 1:
                linea = archivo.readline()
                if linea.find(":") >= 0 and linea.find("/"):
                    inicio = linea.find(":")
                    fin = linea.find("/")
                    porcentaje = linea[inicio + 2: fin - 1]
                    print(porcentaje)
                    bandera = 1
            json_build[counter]['porcentaje'] = int(porcentaje)
            archivo.close()
            #os.remove(ip['ip'])

        t = time.localtime()
        current_time = time.strftime("%d/%m/%y %H:%M:%S", t)
        json_build[counter]['fecha'] = current_time
        counter += 1
    return json_build

def message_formater(json_resp):
    message = 'Se obtuvo informacion de los host:\n'
    for ip in json_resp:
        if ip['hostname'] != '':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] +'\n\t'
    message += '\nLas host que no respondieron son:\n'
    for ip in json_resp:
        if ip['hostname'] == '':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] + '\n'
    return message

def notify_email(emails, message):
    notify = Notifications()
    notify.sendEmail(emails,'Trafico de los routers',message)

def notify_whatsapp(numbers, message):
    notify = Notifications()
    notify.sendWhatsApp(message,numbers)
