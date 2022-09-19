from fastapi import FastAPI
from pydantic import BaseModel
import consultas


app = FastAPI()

@app.get("/Pregunta_N°1")
def Año_más_Carreras():
    return consultas.Pregunta1()

@app.get("/Pregunta_N°2")
def Piloto_más_Ganador():
    return consultas.Pregunta2()

@app.get("/Pregunta_N°3")
def Circuito_más_Corrido():
    return consultas.Pregunta3()

@app.get("/Pregunta_N°4")
def Piloto_más_Ganador_Americano_o_Británico():
    return consultas.Pregunta4()

@app.get("/Consulta/")
def Insertar_Query_MySQL(Query: str):
    return (consultas.query(Query))