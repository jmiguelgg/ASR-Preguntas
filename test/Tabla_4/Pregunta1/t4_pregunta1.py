""" PREGUNTA 1 - TABLA 4 - REDES III """ 
from funcionesP1 import * 

direcciones_telnet = ['192.168.3.1']


for direccion in direcciones_telnet:
    buffer = extraerInformacion(direccion)
    id_router = extraerID(buffer)
    contenido = extraerInformacionHardware(buffer, id_router)   
    #enviarWhats(id_router, direccion, contenido)
    #enviarCorreo(id_router, direccion, contenido)
