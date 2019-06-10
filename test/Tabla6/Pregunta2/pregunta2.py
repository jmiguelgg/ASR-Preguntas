""" PREGUNTA 2 - TABLA 6 - REDES III """
from funcionesP2 import *
direcciones = ['10.1.200.1', '10.3.200.2', '10.4.200.2', '10.6.200.2', '10.8.200.2', '10.14.200.1', '10.9.200.2', '10.10.200.1']

for direccion in direcciones:
    extraerInformacion(direccion) 
    nombre = obtenerNombre(direccion)
    extraerProcesamiento(nombre, direccion) 


