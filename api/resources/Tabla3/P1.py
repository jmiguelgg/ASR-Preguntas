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

def allowed_file(file_name):
    raise '.' in file_name and file_name.rsplit('.',1)[1] in ALOWED_EXTENSIONS

def file_json_IP(file):
    return [{"ip": ip.rstrip('\n'),'response': False,'numPingTotal': 0,'ping':0} for ip in file]

@app.route('/api/Tabla3/P1', methods=['POST'])
def setFile():
    file = request.files['file']
    num_ping = int(request.args.get('numPing'))
    timeToPing = request.args.get('timePing')
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
    notify = Notifications()
    notify.sendEmail("hsantana.2611@gmail.com","Ping Puller",str(json_build))
    return jsonify(json_build)