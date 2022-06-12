#Python
from typing import Optional #Es para realizar tipado estatico

#PYdantic
from pydantic import BaseModel #permite crear modelos

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


#El siguiente bloque es un PATH OPERATION: (leer mas en readme.txt)
@app.get("/")   #Path operation decorator -> Cada vez que alguien abra esta app (/) = Home 
def home():     #Path operation function  -> Se aplicará la siguiente función
    return{"Hello":"World"} #regresa un Json

#Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)): ### ... Significa que es obligatorio.
    return person

#Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_Length=1, max_Length=50), #Restringirlo a que ponga algo y no se pase de 50
    age: str = Query(...) #Lo convierte en un campo obligatorio

):
    return {name: age}