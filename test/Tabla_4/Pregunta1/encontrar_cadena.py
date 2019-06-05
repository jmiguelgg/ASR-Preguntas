""" Encontrar una cadena en un archivo de texto """
bandera = 0
archivo = open("show_ip_route.txt", "r")

while bandera != 1:
    cadena = archivo.readline()
    posicion = cadena.find("export@cisco.com.")
    if posicion >= 0:
        posicion = archivo.tell()
        bandera = 1

print ("P: %d " % posicion)
archivo.seek(posicion)
contenido = archivo.read()
archivo.close()

tipo = type(contenido)
print (tipo)
print (contenido)

limite = contenido.find("R1#")
print("%d" % limite)

salida = open("R1", "w+")
hardware = contenido[0:limite]

salida.write(hardware)

salida.close()