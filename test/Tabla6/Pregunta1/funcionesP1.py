""" FUNCIONES PARA LA PREGUNTA 1 - TABLA 6 - REDES III """
import telnetlib
from twilio.rest import Client
import time
import smtplib
from email.mime.text import MIMEText
""" ----------------------------- FUNCION PARA EXTRAER EL NOMBRE DE UN ROUTER ----------------------------------- """
def extraerNombre(direccion):
    user = "humberto"
    password = "123456"
    show = "conf t"
    salir = "exit"
    archivo = open("nombre", "w+")

    tn = telnetlib.Telnet(direccion)

    print(" ¡¡¡ CONEXIÓN TELNET EXITOSA !!! ")

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(show.encode('ascii') + b"\n")    
    tn.write(salir.encode('ascii') + b"\n")
    tn.write(salir.encode('ascii') + b"\n")


    archivo.write(tn.read_all().decode('ascii'))
    print(archivo.read())
    archivo.close()

    print (" ¡¡¡ FIN DE LA CONEXIÓN !!! ")

    archivo = open("nombre", "r")
    b = 0
    while b != 2:
        linea = archivo.readline()
        b = b + 1
    pos = linea.find("#")
    nombre = linea[0:pos]
    archivo.close()
    return nombre
""" ------------------------------------------------------------------------------------------------------------- """

""" ----------------------------- FUNCION PARA EXTRAER LA INFORMACION DE LAS INTERFACES DE UN ROUTER ------------ """
def extraerInformacion(nombre, direccion):
    user = "humberto"
    password = "123456"
    show = "show interfaces"
    salir = "exit"
    espacio = " "
    ruta = r"Interfaces/"
    archivo = open(ruta + nombre, "w+")

    tn = telnetlib.Telnet(direccion)

    print(" ¡¡¡ CONEXIÓN TELNET EXITOSA !!! ")

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    os.remove(ip['ip'])

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
""" ------------------------------------------------------------------------------------------------------------- """

""" ----------------------------- FUNCION PARA LIMPAR LA INFORMACION DE LAS INTERFACES DE UN ROUTER ------------- """
def tratarInformacion(nombre):
    origen = r"Interfaces/" 
    destino = r"Tratamiento/"
    interfaces = ['FastEthernet', 'Serial']
    archivo_origen = open(origen + nombre, "r")
    dia = time.strftime("%d")
    mes = time.strftime("%m")
    anio = time.strftime("%y")
    fecha = "-" + dia + "-" + mes + "-" + anio
    archivo_destino = open(destino + nombre + fecha, "w+")
    

    n_lineas = len(archivo_origen.readlines())
    archivo_origen.seek(0)

    encabezado = " -------------------Este reporte se generó en la fecha: " + fecha + "---------------------------\n"
    archivo_destino.write(encabezado)
    puntero = 0
    while puntero != n_lineas:
        linea = archivo_origen.readline()
        posicion_int = linea.find("FastEthernet")
        if posicion_int >= 0:
            archivo_destino.write(linea)
        
        posicion_int = linea.find("Serial")
        if posicion_int >= 0:
            archivo_destino.write(linea)
        
        posicion_input = linea.find("packets input")
        if posicion_input >= 0:
            archivo_destino.write(linea)

        posicion_output = linea.find("packets output")
        if posicion_output >= 0:
            archivo_destino.write(linea)

        puntero = puntero + 1
    print("P: %d " % puntero)
    
    
    archivo_origen.close()
    archivo_destino.close()
    #print("T: %d " % n_lineas)