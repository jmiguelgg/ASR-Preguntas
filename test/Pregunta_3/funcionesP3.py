""" FUNCIONES PARA LA EJECUCIoN DE LA PREGUNTA 4 - REDES III """
import os 
from twilio.rest import Client

""" ........................ Funcion para obtener el nivel de un syslog ....................... """
def obtenerNivel(syslog):
    posicion = syslog.find("%")
    bandera = 0
    while bandera != 1:
        if syslog[posicion].isdigit() == True:
            nivel = int(syslog[posicion])
            bandera = 1
        else:
            posicion = posicion + 1
    
    print(" Nivel: %d " % nivel)

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
""" ..................................................................................... """

""" ........................ Funcion para mandar un correo ........................ """
def enviarCorreo(nivel, contenido):
    mensaje = nivel + contenido
    asunto = " ! SYSLOG DETECTADO ! "
    comando = "echo \"" + mensaje + "\" | mail -s \"" + asunto + "\" hsantana.2611@gmail.com"
    os.system(comando)
    print(" ! Notificacion de correo enviada !")
""" ..................................................................................... """

""" ........................ Funcion para mandar un whatsApp ........................ """

def enviarMensaje(nivel, contenido):
    account_sid = 'ACb149282acccbdf97c1004710c2e3d11d'
    auth_token = '8d0aa7e211ea99f907ea7b6de8f4ca46'

    whatsapp = " ! SYSLOG DETECTADO ! \n" + nivel + contenido
    cliente = Client(account_sid, auth_token)
    mensaje = cliente.messages.create(
        body = whatsapp,
        from_= 'whatsapp:+14155238886',
        to = 'whatsapp:+5215545077393'
    )
    print(" ! Notificacion de WhatsApp enviada !")
""" ..................................................................................... """

""" ........................ Funcion para saber si el syslog corresponde a un reboot ........................ """
def obtenerReinicio(syslog):
    palabra = "STARTSTOP"
    posicion = syslog.find(palabra)
    if posicion >= 0:
        reinicio = 1
    else:
        reinicio = 0
    return reinicio
""" ..................................................................................... """

""" ........................ Funcion para obtener la IP de un syslog ........................ """
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