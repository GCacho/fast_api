from fastapi import FastAPI

app = FastAPI()

#El siguiente bloque es un PATH OPERATION: (leer mas en readme.txt)
@app.get("/")   #Path operation decorator -> Cada vez que alguien abra esta app (/) = Home 
def home():     #Path operation function  -> Se aplicará la siguiente función
    return{"Hello":"World"} #regresa un Json

