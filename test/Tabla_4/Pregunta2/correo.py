import smtplib
from email.mime.text import MIMEText

from_addr = "redes3manager@gmail.com"
to_addr = "hsantana.2611@gmail.com"
mensaje = MIMEText("Esta es una prueba de envio de correo con python")
mensaje['From'] = from_addr
mensaje['To'] = to_addr
mensaje['Subject'] = "Asunto"

username = "redes3manager@gmail.com"
password = "escom_1pn"

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, mensaje.as_string())
server.quit()