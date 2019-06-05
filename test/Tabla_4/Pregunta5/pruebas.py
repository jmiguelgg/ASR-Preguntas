import os

templates = os.listdir("tratamientoConfigs/")
prueba = "r1-confg"
archivo = open("tratamientoConfigs/" + prueba, "r+")
lineas = len(archivo.readlines())
archivo.seek(0)
bandera = 0
while bandera != lineas:
    linea = archivo.readline()
    if linea.find("hostname") >= 0:
        tamanio = len(linea)
        inicio = linea.find("hostname")
        espacio = linea.find(" ")
        primera = linea[inicio:espacio + 1]
        segunda = linea[espacio + 1:tamanio - 1]
        temp = primera + "${" + segunda + "}\n"
        print(temp)
    if linea.find("router ospf") >= 0:
        tamanio = len(linea)
        inicio = linea.find("router ospf")
        espacio = len("router ospf")
        primera = linea[inicio:espacio + 1]
        segunda = linea[espacio + 1:tamanio - 1]
        temp = primera + "${" + segunda + "}\n"
        print(temp)
    if linea.find("logging trap") >= 0:
        tamanio = len(linea)
        inicio = linea.find("logging trap")
        espacio = len("logging trap")
        primera = linea[inicio:espacio + 1]
        segunda = linea[espacio + 1:tamanio - 1]
        temp = primera + "${" + segunda + "}\n"
        print(temp)
    if linea.find("logging") >= 0 and linea.find("logging trap") < 0:
        tamanio = len(linea)
        inicio = linea.find("logging")
        espacio = linea.find(" ")
        primera = linea[inicio:espacio + 1]
        segunda = linea[espacio + 1:tamanio - 1]
        temp = primera + "${" + segunda + "}\n"
        print(temp)
    if linea.find("interface") >= 0:
        lista = list(linea.split(" "))
        ultimo = lista[5]
        ultimo = ultimo.replace("\n", "")
        temp = lista[0] + " ${" + lista[1] + "} " + lista[2] + " " + lista[3] + " ${" + lista[4] + "} ${" + ultimo + "}\n" 
        print(temp)
    if linea.find("network") >= 0:
        lista = list(linea.split(" "))
        ultimo = lista[5]
        ultimo = ultimo.replace("\n", "")
        temp = lista[1] + " ${" + lista[2] + "} ${" + lista[3] + "} " + lista[4] + " ${" + ultimo + "}\n"
        print(temp)
    bandera = bandera + 1
