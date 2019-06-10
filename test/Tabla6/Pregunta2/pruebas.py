from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

archivo = open(r"cpu/29-05-19-10.1.200.1", "r")
contenido = archivo.read()
w, h = A4
x = 50
y = h - 104
c = canvas.Canvas("hola-mundo.pdf")
text = c.beginText(50, h - 117)
c.drawString(50,h - 100," CPU Estadistics ")
c.drawImage("escudoESCOM.jpg", 460, h - 100, width=75, height=60)
c.line(x, y, x + 500, y)
text.textLines(contenido)
c.drawText(text)

c.save()