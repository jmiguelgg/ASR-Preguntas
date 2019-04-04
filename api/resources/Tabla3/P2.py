import socket
import Notifications
from pyasn1.codec.ber import decoder

port = 162
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
notify = Notifications()

while 1:
    data, addr = s.recvfrom(4048)
    algo = decoder.decode(data)
    print ("\n - - - - - - - - - - - - - - - - - TRAP DETECTADA - - - - - - - - - - - - - - - - - -  \n")
    print (algo) 
    dos = str(algo)
    notify.sendEmail("hsantana.2611@gmail.com","Trap Detectada",dos)