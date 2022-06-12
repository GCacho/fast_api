#Python
from typing import Optional #Es para realizar tipado estatico

#PYdantic
from pydantic import BaseModel #permite crear modelos

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

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
def create_person(
    person: Person = Body(...) # ... Significa que es obligatorio.
): 
    return person

#Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query( #Restringirlo a que ponga algo y no se pase de 50
        None, 
        min_Length=1, 
        max_Length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 strings" 
        ), 
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person's age. It's required"
        ) #Lo convierte en un campo obligatorio
):
    return {name: age}

#Validaciones: Path Validations
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0) #importamos Path
):
    return{person_id: "It exists!"}