import telnetlib
import sys

host = "10.1.200.1"
user = "humberto"
password = "123456"
show = "show version"
salir = "exit"
espacio = " "

archivo = open("show_ip_route.txt", "w+")
tn = telnetlib.Telnet(host)
# print "Conexion exitosa ... \n"
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(show.encode('ascii') + b"\n")
tn.write(espacio.encode('ascii') + b"\n")

tn.write(salir.encode('ascii') + b"\n")
# print "Fin de la conexion \n"

archivo.write (tn.read_all().decode('ascii'))
archivo.close()
# Comienza la lectura del comando show ip route y se copia la informacion de interes 