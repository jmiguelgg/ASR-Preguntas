import socket
from ..Util.Notifications import Notifications
#from pyasn1.codec.ber import decoder
from flask import Flask, request, jsonify, url_for
from flask_restful import Resource, Api
from threading import Thread, Event
from multiprocessing.pool import ThreadPool
import time
import select
 
stop_it = Event()

def do_stuff():
    result = []
    port = 162
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    s.setblocking(0)
    counter = 0
    while True:
        ready = select.select([s], [], [], 1)
        if ready[0]:
            data, addr = s.recvfrom(4048)
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            counter += 1
            result.append({'id':counter,'fecha':current_time,'trap':data.decode('latin-1')})
        if stop_it.is_set():
            break
    return result

def notify_All(data,correo,numero,tiempo):
    message = "En un tiempo de " + str(tiempo) + " segundos "  + " se recibieron " + str(len(data)) + " TRAPS"
    notify = Notifications()
    notify.sendEmail([correo],'Traps',message)
    notify.sendWhatsApp(message,[numero])

class P2(Resource):
    def post(self):
        correo = request.form['correo']
        numero = request.form['numero']
        tiempo = int(request.form['tiempo'])
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(do_stuff)
        time.sleep( tiempo )
        stop_it.set()
        return_val = async_result.get()
        stop_it.clear()
        #notify_All(return_val,correo,numero,tiempo)
        return jsonify(return_val)