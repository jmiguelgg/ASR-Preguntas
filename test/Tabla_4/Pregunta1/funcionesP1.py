""" FUNCIONES CREADAS PARA LA PREGUNTA 1 DE LA TABLA 4 - REDES III """
import telnetlib
from twilio.rest import Client
import time
import smtplib
from email.mime.text import MIMEText
""" .............. Funcion para extraer la informacion del HW de un router a traves de telnet .............. """
def extraerInformacion(direccion):
    user = "humberto"
    password = "123456"
    show = "show version"
    salir = "exit"
    espacio = " "
    nombre_archivo = "buffer.txt"

    archivo = open(nombre_archivo, "w+")
    tn = telnetlib.Telnet(direccion)

    print(" !!! CONEXION TELNET EXITOSA !!! ")

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(show.encode('ascii') + b"\n")
    tn.write(espacio.encode('ascii') + b"\n")

    tn.write(salir.encode('ascii') + b"\n")

    archivo.write(tn.read_all().decode('ascii'))
    print(archivo.read())
    archivo.close()

    print (" ! FIN DE LA CONEXION !!! ")
    return nombre_archivo
""" ..................................................................................... """
""" ......... Funcion para extraer el id del router .......... """
def extraerID(nombre_archivo):
    bandera = 0
    archivo = open(nombre_archivo, "r")
    while bandera != 1:
        cadena = archivo.readline()
        posicion = cadena.find("#")
        if posicion >= 0:
            bandera = 1
            cadena_final = cadena
    archivo.close()

    print ("P: %d " % posicion)
    print (cadena_final)
    hostname = cadena_final[0:posicion]
    print("Hostname: " + hostname)

    return hostname
""" ..................................................................................... """
""" ......... Funcion para extraer la informacion del HW del router .......... """
def extraerInformacionHardware(nombre_archivo, nombre_router):
    bandera = 0
    archivo = open(nombre_archivo, "r")

    while bandera != 1:
        cadena = archivo.readline()
        posicion = cadena.find("export@cisco.com.")
        if posicion >= 0:
            posicion = archivo.tell()
            bandera = 1

    print ("P: %d " % posicion)
    archivo.seek(posicion)
    contenido = archivo.read()
    archivo.close()

    tipo = type(contenido)
    print (tipo)
    print (contenido)

    limite = contenido.find("R1#")
    print("%d" % limite)

    salida = open(nombre_router, "w+")
    hardware = contenido[0:limite]

    salida.write(hardware)

    salida.close()

    return hardware
""" ..................................................................................... """
""" .......................... Funcion para enviar un WhatsApp .......................... """
def enviarWhats(router, ip, contenido):
    account_sid = 'ACb149282acccbdf97c1004710c2e3d11d'
    auth_token = '8d0aa7e211ea99f907ea7b6de8f4ca46'
    cliente = Client(account_sid, auth_token)

    whats = " ID: " + router + "\n IP: " + ip + "\n Informacion: " + contenido 

    mensaje = cliente.messages.create(
    body = whats,
    from_= 'whatsapp:+14155238886',
    to = 'whatsapp:+5215545077393'
    )
    time.sleep(1)
    print(" ! Notificacion de WhatsApp enviada !")

""" ..................... Funcion para enviar un correo electronico ................ """
def enviarCorreo(router, ip, contenido):
    from_addr = "redes3manager@gmail.com"
    to_addr = "hsantana.2611@gmail.com"

    mensaje = MIMEText("ID: %s \n IP: %s \n Informacion: %s " % (router, ip, contenido))
    mensaje['From'] = from_addr
    mensaje['To'] = to_addr
    mensaje['Subject'] = " Informacion de dispositivo"

    username = "redes3manager@gmail.com"
    password = "escom_1pn"

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, mensaje.as_string())
    server.quit()
    print(" ! Notificacion de correo enviada !")
""" ................................................................................................................... """