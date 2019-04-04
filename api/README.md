#Probar el API

##Tabla 3

### Pregunta 1
Las pruebas estan hechas con CURL
curl -F 'file=@/Users/jmiguel/Documents/ASR/Proyecto/test/Pregunta_1/ips.txt' "http://localhost:5000/api/Tabla3/P1?numPing=3&timePing=10"

file=@<Ruta absoluta donde tomará el archivo>
numPing=<Numero de veces que probará hacer ping>
timePing=<Tiempo de respuesta del ping en milisegundos antes de estar a destiempo>