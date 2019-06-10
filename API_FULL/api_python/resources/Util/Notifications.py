import sys
import os
import smtplib
from twilio.rest import Client
from email.mime.text import MIMEText

account_sid = 'ACb149282acccbdf97c1004710c2e3d11d'
auth_token = '8d0aa7e211ea99f907ea7b6de8f4ca46'
emisor = 'coldpcmickey@gmail.com'
password = 'Revolution45vi'

class Notifications:
    def funcname(self):
        pass

    def sendEmail(self,mails,issue,message):
        # Configuracion del mail 
        mensaje = MIMEText(message) 
        mensaje['From'] = 'Redes>'+emisor
        mensaje['Subject'] = issue

        # Nos conectamos al servidor SMTP de Gmail 
        serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
        serverSMTP.ehlo() 
        serverSMTP.starttls() 
        serverSMTP.ehlo() 
        serverSMTP.login(emisor,password) 

        # Enviamos el mensaje 
        for mail in mails:
            mensaje['To'] = mail
            serverSMTP.sendmail(emisor,mail,mensaje.as_string()) 
        # Cerramos la conexion 
        serverSMTP.close()
    
    def sendWhatsApp(self,message,numbers):
        cliente = Client(account_sid, auth_token)
        for num in numbers:
            cliente.messages.create(
                body = message,
                from_= 'whatsapp:+14155238886',
                to = 'whatsapp:+' + num
            )
