""" Extraer el ID host del router """
bandera = 0
archivo = open("show_ip_route.txt", "r")
while bandera != 1:
    cadena = archivo.readline()
    posicion = cadena.find("#")
    if posicion >= 0:
        bandera = 1
        cadena_final = cadena
archivo.close()

print ("P: %d " % posicion)
print (cadena_final)
hostname = cadena_final[0:posicion]
print("Hostname: " + hostname)