Llamados de API:

Usuario:
    Toda la información de los usuarios:
    Methos: GET

    curl -X GET "http://localhost:3000/user"

    Nuevo Usuario:
    Method: POST
    Data-Type: JSON

    curl -d '{"nombres":"Ethan Isaac","apellidos":"Bautista Treviso","correo":"ebautistat@hotmail.com","numero":"5215586141860","pass":"holakhace"}' -H "Content-Type: application/json" -X POST "http://localhost:3000/user/newuser"

    Login:
    Methos: POST
    Data-Type: JSON

    curl -d '{"correo":"di_tutticolori@hotmail.com","pass":"066731b02fa52899d4093ff164b521cb0b00230014c69aa75e1f63feebe4aee2"}' -H "Content-Type: application/json" -X POST "http://localhost:3000/user/login"
