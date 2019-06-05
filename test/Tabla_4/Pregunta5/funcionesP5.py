""" FUNCIONES PARA LA PREGUNTA 5 - TABLA 4 - REDES III """
from twilio.rest import Client
import smtplib
import time
from email.mime.text import MIMEText

""" ................. Función para comparar el template con los archivos de configuración de un router ............... """
def compararTemplate():
    archivos = ['r1-confg', 'r2-confg', 'r3-confg', 'r4-confg', 'r6-confg', 'r7-confg', 'r8-confg', 'r9-confg', 'r10-confg']
    
    for archivo in archivos:
        archivo_temp = open("template.txt", "r")
        salida = open("resultado.txt", "w+")
        tamanio = len(archivo_temp.readlines())
        archivo_temp.seek(0)
        print("########### Archivo %s ###########" % archivo)
        bandera = 0
        while bandera != tamanio:
            cadena = archivo_temp.readline()
            resultado = buscarCadena(cadena, archivo)
            if resultado == 1:
                info = " La cadena " + cadena + " SI se encontro en el archivo \n" 
                salida.write(info)
            elif resultado == 0:
                info = " La cadena " + cadena + " NO se encontro en el archivo \n" 
                salida.write(info)
            bandera = bandera + 1
        archivo_temp.close()
        salida.seek(0)
        sss = salida.read()
        print (sss)
        salida.close()
        #enviarCorreo(sss, archivo)
        enviarWhats(sss, archivo)

        

""" ................................................................................................................... """

""" ............................... Función para buscar una cadena dentro de un archivo ........................."""
def buscarCadena(cadena, archivo):
    archivo_conf = open("../Pregunta2/configurciones/" + archivo, "r")
    tamanio = len(archivo_conf.readlines())
    archivo_conf.seek(0)
    bandera = 0
    status = 0
    while bandera != tamanio:
        linea = archivo_conf.readline()
        #print ("L: %s " % linea)
        posicion = linea.find(cadena)
        if posicion >= 0:
            status = 1
        bandera = bandera + 1
    archivo_conf.close()
    if status == 1:
        #print(" -------> La cadena %s coincide <-------" % cadena)
        return 1
    elif status == 0:
        #print(" -------> La cadena %s NO coincide <-------" % cadena)
        return 0
    
""" ................................................................................................................... """

""" ..................... Función para enviar un correo electrónico ................ """
def enviarCorreo(informacion, archivo):
    from_addr = "redes3manager@gmail.com"
    to_addr = "hsantana.2611@gmail.com"

    mensaje = MIMEText("¡ Comparacion realizada con el archivo %s ! \n Resultado: %s " % (archivo, informacion))
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = "Comparación de template"

    username = "redes3manager@gmail.com"
    password = "escom_1pn"

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, mensaje.as_string())
    server.quit()
    print(" ! Notificacion de correo enviada !")
""" ................................................................................................................... """

""" .......................... Función para enviar un WhatsApp .......................... """
def enviarWhats(informacion, archivo):
    account_sid = 'ACb149282acccbdf97c1004710c2e3d11d'
    auth_token = '8d0aa7e211ea99f907ea7b6de8f4ca46'
    cliente = Client(account_sid, auth_token)

    whats = " ¡ Comparación de template ! \n Archivo: %s \n Resultado: \n %s " % (archivo, informacion)

    mensaje = cliente.messages.create(
    body = whats,
    from_= 'whatsapp:+14155238886',
    to = 'whatsapp:+5215545077393'
    )
    time.sleep(1)
    print(" ! Notificacion de WhatsApp enviada !")
""" ......................................................................................................"""