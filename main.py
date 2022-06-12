#Python
from typing import Optional #Es para realizar tipado estatico
from enum import Enum #Para crear enumeraciones de strings

#PYdantic
from pydantic import BaseModel #permite crear modelos
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
    white="white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel): #Herencias aplicadas 
    city: str
    state: str
    country: str

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_Length=1,
        max_Length=50,
        example="Guillermo"
        )
    last_name: str = Field(
        ...,
        min_Length=1,
        max_Length=50,
        example="Nacho"
        )
    age: int = Field(
        ...,
        gt=0, #tiene que ser mayor a 0
        le=115,
        example="99"
    )
    hair_color: Optional[HairColor] = Field(default=None,example="black") #Restringimos a nuestro porpio hair color
    is_married: Optional[bool] = Field(default=None,example="False") #Restringimos con booleanos

class Person(PersonBase):
    password: str = Field(..., min_length=8)


class PersonOut(PersonBase): #Es lo mismo que el de person pero le retiramos la contrasena, revisar app.post()
    pass

    # class Config:
    #     schema_extra = {
    #         "example":{
    #             "first_name":"Guillermo",
    #             "last_name":"Cacho",
    #             "age":21,
    #             "hair_color":"black",
    #             "is_married":False
    #         }
    #     }

#El siguiente bloque es un PATH OPERATION: (leer mas en readme.txt)
@app.get("/")   #Path operation decorator -> Cada vez que alguien abra esta app (/) = Home 
def home():     #Path operation function  -> Se aplicará la siguiente función
    return{"Hello":"World"} #regresa un Json

#Request and Response Body
@app.post("/person/new", response_model=PersonOut) #Para la contrasena
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
        description="This is the person name. It's between 1 and 50 strings",
        example="Paola"
        ), 
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person's age. It's required",
        example=25
        ) #Lo convierte en un campo obligatorio
):
    return {name: age}

#Validaciones: Path Validations
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        example=123
        ) #importamos Path
):
    return{person_id: "It exists!"}

#Validaciones: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),

):
    return person