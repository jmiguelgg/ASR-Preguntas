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
copy = "copy running-config tftp"
destino = "10.1.200.3"
salir = "exit"
#carpetaCompartida = "/Volumes/R3/"
carpetaCompartida = "/Users/jmiguel/Desktop/respaldoSyslog/10.6.200.2/"

class T4_P2(Resource):
    def post(self):
        data = ImmutableMultiDict(request.form)
        data.to_dict(flat=False)
        file = request.files['file']
        emails = [data['email']]
        numbers = [data['number']]
        resptPP = getInfoHardware(file)
        message = message_formater(resptPP)
        notify_email(emails,message)
        notify_whatsapp(numbers,message)
        return jsonify(resptPP)

    def get(self):
        res = []
        counter = 0
        try:
            archivos = os.listdir(carpetaCompartida)
            archivos.sort()
            for archivo in archivos:
                leerArchivo = open(r""+carpetaCompartida+archivo, "r")
                data = leerArchivo.read()
                counter += 1
                res.append({'id':counter,'nombre':archivo,'data':data})
        except:
            print('No se pudo acceder a la carpeta compartida')
        return jsonify(res)

def allowed_file(file_name):
    raise '.' in file_name and file_name.rsplit('.',1)[1] in ALOWED_EXTENSIONS

def file_json_IP(file):
    return [{'ip': ip.rstrip('\n'),'fecha': '','status': 'false'} for ip in file]

def getInfoHardware(file):
    json_build = file_json_IP(file)
    counter = 0
    for ip in json_build:
        #Codigo
        flag = False
        try:
            tn = telnetlib.Telnet(ip['ip'],69,2)
            flag = True
        except:
            print('No fue posible la conexion con : ' + ip['ip'])
        if flag:
            tn.read_until(b"Username: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
            tn.write(copy.encode('ascii') + b"\n")
            tn.write(destino.encode('ascii') + b"\n")
            tn.write(b"\n")
            time.sleep(1)
            tn.write(salir.encode('ascii') + b"\n")
            json_build[counter]['status'] = 'true'

        t = time.localtime()
        current_time = time.strftime("%d/%m/%y %H:%M:%S", t)
        json_build[counter]['fecha'] = current_time
        counter += 1
    return json_build

def message_formater(json_resp):
    message = 'Se respaldo la informacion de las interfaces con ip:\n'
    for ip in json_resp:
        if ip['status'] == 'true':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] + '\n\t'
    message += '\nLas interfaces no respaldadas son:\n'
    for ip in json_resp:
        if ip['status'] == 'false':
            message += ip['ip'] + ' - fecha de respuesta: ' + ip['fecha'] + '\n'
    return message

def notify_email(emails, message):
    notify = Notifications()
    notify.sendEmail(emails,'Respaldo de configuracion',message)

def notify_whatsapp(numbers, message):
    notify = Notifications()
    notify.sendWhatsApp(message,numbers)
