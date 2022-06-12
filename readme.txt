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

-Tipos de datos especiales:
    -Clasicos
        -str 
        -int 
        -float
        -bool
    -Exóticos
        -enum -> Para enumerar.
        -httpurl -> Para trabajar con HTTP 
        -filepath -> c:/windows/sistem32/432.dll
        -directorypath -> /mnt/c/somefolder
        -emailstring -> hola@hola.com : valido / facundo.com : NO valido
        -paymentcadrnumber -> tarjetas de credito
        -IPvAnyaddress -> validar si es una IP
        -negativefloat -> si estan ingresando un flotante negativo 
        -positivefloat
        -negativeint
        -positiveint 
        Ver Más: https://pydantic-docs.helpmanual.io/usage/types/#pydantic-types

-Status Codes 
    -100 -> Information
    -200 -> OK
        -201 -> Created
        -204 -> No Content
    -300 -> Redirecting
    -400 -> Client Error
        -404 -> No Exists
        -422 -> Validation Error
    -500 -> Internal Server Error