""" PREGUNTA 4 (Para MV con linux) - REDES III """
import time
import sys
import os
from funcionesP4 import *

comando = "grep reboot ../../../var/log/pregunta4/lubuntu-pc1/systemd-logind.log>reboot_linux.txt"
os.system(comando)
fichero = open("reboot_linux.txt", "r")
original = len(fichero.readlines())
fichero.close()
while 1:
    os.system(comando)
    fichero = open("reboot_linux.txt", "r")
    nuevo = len(fichero.readlines())
    fichero.close()

    print ("OR: %d" % original)
    print ("NV: %d" % original)

    if original != nuevo:
        print("SYSLOG DETECTADO")
        original = nuevo
        enviarMensaje("6", "System is rebooting", "lubuntu-pc1")
    else:
        print(".")
        time.sleep(1)