import socket
import sys
import os
import pprint
from pysnmp.hlapi.asyncore import * 
from pysnmp.hlapi import *
from pysnmp.proto import api
from pyasn1.codec.ber import decoder 
from tkinter import messagebox as MessageBox 
#from snmp_helper import snmp_get_oid_v3,snmp_extract 

#archivo = open("trap.txt", "w")
port = 162
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
#pp = pprint.PrettyPrinter()
while 1:
        data, addr = s.recvfrom(4048)
        algo = decoder.decode(data)
        print ("\n - - - - - - - - - - - - - - - - - TRAP DETECTADA - - - - - - - - - - - - - - - - - -  \n")
        print (algo) 
        dos = str(algo)
        comando = "echo " + dos + " | mail -s \" TRAP DETECTADA \" hsantana.2611@gmail.com"
        os.system(comando)
        #MessageBox.showwarning("Advertencia", "TRAP DETECTADA")
        #print data.decode('unicode-escape')
        #octal = int(data, 8)
        #print oct(octal)
        #pp.pprint(data)
        #print type(data)
        #print(' = '.join([x.prettyPrint() for x in data])) 
        #str(data)
        #archivo.write(data) 
