import json
import os
from ..Util.Notifications import Notifications
from flask import Flask, request, jsonify, url_for
from werkzeug.utils import secure_filename
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLER = '~/Tabla3/APingPoller'
ALOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLER'] = UPLOAD_FOLER

@app.route('/api/Tabla3/P1', methods=['POST'])
def pingPuller():
    #numbers = ['5215586141860','5215545077393']
    #emails = ['coldpcmickey@gmail.com','hsantana.2611@gmail.com']
    numbers = ['5215586141860']
    emails = ['di_tutticolori@hotmail.com']
    file = request.files['file']
    num_ping = int(request.args.get('numPing'))
    timeToPing = request.args.get('timePing')
    resptPP = doPingPuller(num_ping,timeToPing,file)
    message = message_formater(resptPP)
    notify_email(emails,message)
    notify_whatsapp(numbers,message)
    return jsonify(resptPP)

def allowed_file(file_name):
    raise '.' in file_name and file_name.rsplit('.',1)[1] in ALOWED_EXTENSIONS

def file_json_IP(file):
    return [{'ip': ip.rstrip('\n'),'response': False,'numPingTotal': 0,'ping':0} for ip in file]

def doPingPuller(num_ping,timeToPing,file):
    json_build = file_json_IP(file)
    for i in range(num_ping):
        count = 0
        for ip in json_build:
            if ip['numPingTotal'] == 0:
                json_build[count]['numPingTotal'] = num_ping
            if not ip['response']:
                comando = "ping -W "+ timeToPing +" -c 1 " + ip['ip']
                output = os.system(comando)
                if output == 0:
                    json_build[count]['response'] = True
                    json_build[count]['ping'] = i+1
            count += 1
    return json_build

def message_formater(json_resp):
    message = 'Ping totales : '+ str(json_resp[1]['numPingTotal']) +'\nLas ip que respondieron son:\n'
    for ip in json_resp:
        if ip['response'] == True:
            message += ip['ip'] + ' respondio en el ping: '+ str(ip['ping']) +'\n'
    message += '\nLas ip que no respondieron son:\n'
    for ip in json_resp:
        if ip['response'] == False:
            message += ip['ip'] + '\n'
    return message

def notify_email(emails, message):
    notify = Notifications()
    notify.sendEmail(emails,'Ping Puller',message)

def notify_whatsapp(numbers, message):
    notify = Notifications()
    notify.sendWhatsApp(message,numbers)