# Ejecutar consultas a la base de datos llamada api.db y mostrar los resultados en la consola
# Esta base de datos se encuentra en mariadb y tiene las siguientes tablas:
# - circuits
# - constructors
# - drivers
# - laptimes
# - races
# - results
# - stops

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.params import Depends
from . import models, schemas
from .conexion import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# Aqui estoy trabajando con la tabla usuarios
@app.get("/usuarios/", response_model=List[schemas.User])
def show_users(db: Session = Depends(get_db)):
    usuarios = db.query(models.User).all()
    return usuarios

@app.post("/usuarios/", response_model=schemas.User)
def create_users(entrada:schemas.User, db: Session = Depends(get_db)):
    usuario = models.User(username=entrada.username, nombre=entrada.nombre, rol=entrada.rol, estado=entrada.estado)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@app.put("/usuarios/{usuario_id}", response_model=schemas.User)
def update_users(usuario_id:int,entrada:schemas.UserUpdate, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter_by(id == usuario_id).first()
    usuario.nombre = entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}", response_model=schemas.Respuesta)
def delete_users(usuario_id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter_by(id == usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Usuario eliminado")
    return respuesta

# # Aqui estoy trabajando con la tabla drivers
# @app.get("/drivers/", response_model=List[schemas.Driver])
# def show_drivers(db: Session = Depends(get_db)):
#     drivers = db.query(models.Driver).all()
#     return drivers

# # Aqui debo devolver a los pilotos por IdPiloto
# @app.get("/drivers/{driver_id}", response_model=schemas.Driver)
# def show_drivers(driver_id:int, db: Session = Depends(get_db)):
#     driver = db.query(models.Driver).filter_by(IdPiloto == driver_id).first()
#     return driver





