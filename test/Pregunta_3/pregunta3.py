import os
import time
archivos_or = os.listdir("/var/log/192.168.3.1")
#print (archivos_or)


while 1:
    archivos_or.sort()
    #print ("Original --> ")
    print (archivos_or)
    tamanio_or = len(archivos_or)
    archivos_nuevo = os.listdir("/var/log/192.168.3.1")
    tamanio_nuevo = len(archivos_nuevo)
    archivos_nuevo.sort()
    #print ("Nueva --> ")
    #print (archivos_nuevo)

    bandera = 0
    if tamanio_or != tamanio_nuevo:
        print(" SYSLOG DETECTADO !!! ")
        diferencia = tamanio_nuevo - tamanio_or
        print ("OR: " + str(tamanio_or))
        print ("NV: " + str(tamanio_nuevo))
    
        while bandera != diferencia:
            c = tamanio_or
            print(c)
            print(archivos_nuevo[c])
            syslog = open(r"/var/log/192.168.3.1/" + str(archivos_nuevo[c]), "r" )
            contenido = syslog.read()
            print (contenido)
            correo = "echo \"" + contenido + " \"" + " | mail -s \" SYSLOG DETECTADO \" hsantana.2611@gmail.com"  
            syslog.close()
            bandera = bandera + 1
            c = c + 1
        archivos_or = archivos_nuevo
    else:
        print(".")
        time.sleep(1)


"""
syslog = archivos_nuevo[tamanio_check - 1]
aux1 = syslog.lstrip('\'')
aux2 = aux1.rstrip('\'')
print (aux2)
syslog_file = open(r"/var/log/192.168.3.1/" + aux2, "r")
contenido = syslog_file.read()
print (contenido)
"""