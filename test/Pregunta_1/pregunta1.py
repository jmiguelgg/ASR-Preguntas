import os
import time
import shutil
import sys
import telnetlib
import getpass

def obtenerIP():
    archivo = open("ips.txt", "r")
    print (" ... OBTENIEDO IPs ... ")
    for c in range(0, 25):
        cadena = archivo.readline() 
        print (cadena) 
        time.sleep(1)
    print (" ... IPs obtenidas ... \n")

def realizarPING():
    archivo2 = open("adverts.txt", "w")
    for i in range(1, 4):
        archivo = open("ips.txt", "r")
        print ("\n ************** Iteracion %d **************** " % (i))
        archivo2.write("************ ITERACION %d ************ \n" % (i))
        for c in range(0, 25):
            cadena = archivo.readline() 
            print (cadena) 
            comando = "ping -c 3 " + cadena
            output = os.system(comando)
            if output == 0:
                print (" ---------> SI RESPONDE <------------- \n ")
            else:
                print (" !!!!!!!!!!!!! NO REPONDE !!!!!!!!!!! \n")
                ip = cadena
                archivo2.write(" La ip " + ip + "no respondio \n")
                
        archivo.close()
    archivo2.close()

print (" - - - - - - - - - - - - - PIN PULLER - - - - - - - - - - - - - \n")

obtenerIP()
realizarPING()
os.system("clear")
print(" \n ... RESULTADOS OBTENIDOS .... \n")
resultado = open("adverts.txt", "r")
with open ("adverts.txt", "r") as f:
    shutil.copyfileobj(f, sys.stdout)




