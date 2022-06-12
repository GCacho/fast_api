Instalar un ambiente virtual y correr los siguientes comandos.
-pip install fastapi uvicorn -> Instalará el framework fastapi y el servidor unicorn.

Para correr la app hay que poner en comandos 
    -> uvicorn main:app --reload

--reload hace que cada vez que modifiquemos el código se cargarán automaticamente.

Despues de correr el API te mandará un localhost, en este caso 127.0.0.1:8000

127.0.0.1:8000/docs  -->  Muestra la ventana de documentacion del API
127.0.0.1:8000/redoc -->  Otra forma de documentación.

-Path Operations: 
    -Paths: Son los endponts o routes (guillermocacho.com/cv) /cv es un endpoint/path
    -Operations:                            Otros Operations.
        -GET : Traer la información         -Options
        -POST : Enviar la información       -Head
        -PUT : Actualiza la información     -Patch
        -Delete : Borra la información      -Trace

Path operation es una combinación entre los paths y operaciones.

-Query Parameter:
    -Request Body: Es el body que envia el cliente a servidor de ida y vuelta.

-Validadiones:
    -Strings
        -max_Length : Máximo de letras.
        -min_Length : Mínimo de letras.
        -regex : "La navaja suiza del programador" más avanzado

    -Números:
        -ge : greater or equal than >=
        -le : less or equal than <=
        -gt : greater than >
        -lt : less than <

    -Parámetros:
        -Title : 
        -Description : 
