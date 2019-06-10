""" FUNCIONES PARA LA PREGUNTA 1 - REDES III - TABLA 6 """
import os 

""" ------------------ FUNCION PARA VINCULAR CADA INTERFAZ DE RED CON SU RESPECTIVO TRÁFICO DE DATOS --------------- """
def vincularDatos():
    ruta = r"../Pregunta1/Tratamiento"
    estadisticas = r"Estadisticas/"
    archivos = os.listdir(ruta)
    for archivo in archivos:
        linea = archivo
        posicion = linea.find("-")
        nombre_archivo = linea[0:posicion]
        print(nombre_archivo)

        informacion = open(ruta + "/" + archivo, "r")
        salida = open(estadisticas + nombre_archivo, "w+")
        numero_lineas = len(informacion.readlines())
        informacion.seek(0)
        recorrido = 0
        while recorrido != numero_lineas:
            linea2 = informacion.readline()
            if linea2.find("FastEthernet") >= 0 and linea2.find("/") >= 0:
                pos_interfaz = linea2.find(" ")
                nombre_ethernet = linea2[0:pos_interfaz]
                print(nombre_ethernet)
                linea3 = informacion.readline()
                entradas = obtenerBytes(linea3)
                recorrido = recorrido + 1
                linea3 = informacion.readline()
                salidas = obtenerBytes(linea3)
                recorrido = recorrido + 1
                total = entradas + salidas
                texto = nombre_ethernet + "," + str(total) + "\n"
                print(texto)
                salida.write(texto)
                
            if linea2.find("Serial") >= 0 and linea2.find("/") >= 0:
                pos_interfaz = linea2.find(" ")
                nombre_serial = linea2[0:pos_interfaz]
                print(nombre_serial)
                linea4 = informacion.readline()
                recorrido = recorrido + 1
                linea4 = informacion.readline()
                entradas = obtenerBytes(linea3)
                recorrido = recorrido + 1
                linea4 = informacion.readline()
                salidas = obtenerBytes(linea3)
                recorrido = recorrido + 1
                total = entradas + salidas
                print("Total: %d " % total)
                salida.write(nombre_serial + "," + str(total) + "\n")
            recorrido = recorrido + 1
        salida.close()
        print("------------------------------------------------------------------------")
""" ---------------------------------------------------------------------------------------------------------- """
def obtenerBytes(linea):
    inicio = linea.find(",")
    fin = linea.find("bytes")

    recorrido = linea[inicio + 1:fin - 1]
    recorrido = int(recorrido)

    return recorrido

    
