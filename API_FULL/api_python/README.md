#Probar el API

##Tabla 3

### Pregunta 1
Las pruebas estan hechas con CURL
curl -F 'file=@/Users/jmiguel/Documents/ASR/Proyecto/test/Pregunta_1/ips.txt' "http://localhost:5000/api/Tabla3/P1?numPing=3&timePing=10"

file=@<Ruta absoluta donde tomará el archivo>
numPing=<Numero de veces que probará hacer ping>
timePing=<Tiempo de respuesta del ping en milisegundos antes de estar a destiempo>

curl -d "correo=di_tutticolori@hotmail.com&numero=5215586141860&tiempo=5" -H "Content-Type: application/x-www-form-urlencoded" -X POST "http://127.0.0.1:5000/api/Tabla3/P2"