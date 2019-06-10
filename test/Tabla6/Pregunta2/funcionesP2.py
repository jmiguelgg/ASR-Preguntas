""" FUNCIONES PARA LA PREGUNTA 2 - TABLA 6 - REDES III """
import telnetlib
from twilio.rest import Client
import time
import smtplib
from email.mime.text import MIMEText

def extraerInformacion(direccion):
    user = "humberto"
    password = "123456"
    show = "show processes CPU"
    salir = "exit"
    espacio = " "
    ruta = r"cpu/"
    nombre = direccion
    nombre_archivo = "buffer.txt"
    archivo = open(ruta + nombre, "w+")

    tn = telnetlib.Telnet(direccion)

    print(" ¡¡¡ CONEXIÓN TELNET EXITOSA !!! ")

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(show.encode('ascii') + b"\n")
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


    archivo.write(tn.read_all().decode('ascii'))
    print(archivo.read())
    archivo.close()

    print (" ¡¡¡ FIN DE LA CONEXIÓN !!! ")
    return nombre_archivo
""" ---------------------------------------------------------------------------------- """

def obtenerNombre(direccion):
    ruta = r"cpu/"
    archivo = open(ruta + direccion, "r")
    bandera = 0
    while bandera != 1:
        linea = archivo.readline()
        if linea.find("#") >= 0:
            limite = linea.find("#")
            nombre_router = linea[0:limite]
            bandera = 1
    print(nombre_router)
    return nombre_router    
""" ---------------------------------------------------------------------------------- """

""" ---------------------------------------------------------------------------------- """
def extraerProcesamiento(nombre, direccion):
    informacion = r"cpu/" + direccion
    ruta_salida = r"Estadisticas/" + nombre

    archivo = open(informacion, "r")
    archivo_salida = open(ruta_salida, "a+")
    bandera = 0
    while bandera != 1:
        linea = archivo.readline()
        if linea.find(":") >= 0 and linea.find("/"):
            inicio = linea.find(":")
            fin = linea.find("/")
            porcentaje = linea[inicio + 2: fin - 1]
            print(porcentaje)
            bandera = 1 
    estadistica = porcentaje + "\n"
    porcentaje = int(porcentaje)
    if porcentaje >= 1:
        print("ADVERTENCIA, EL ROUTER " + nombre + " HA ALCANZADO EL LIMITE DE PROCESAMIENTO")
    archivo_salida.write(estadistica)


    
            


