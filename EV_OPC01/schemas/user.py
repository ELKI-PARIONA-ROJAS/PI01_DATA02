from datetime import date
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class Circuit(BaseModel):
    IdCircuito: Optional[int]
    Ciudad: str
    Nombre_Circuito: str
    Localidad: str
    Pais: str
    Latitud: float
    Longitud: float
    Altitud: int
    Url_Circuito: str

class Constructor(BaseModel):
    IdConstructor: Optional[int]
    NombreConstructor: str
    Nacionalidad: str
    UrlConstructor: str

class Driver(BaseModel):
    IdPiloto: Optional[int]
    Nombre_Piloto: str
    Nro_Matricula: str
    Codigo: str
    Nombre: str
    Apellido: str
    Nacimiento: date
    Nacionalidad: str
    Url_Piloto: str

class Laptime(BaseModel):
    IdCarrera: int
    IdPiloto: int
    IdVuelta: int
    Posicion: int
    Tiempo: str
    Duracion: int

class Qualifying(BaseModel):
    IdCalificacion: Optional[int]
    IdCarrera: int
    IdPiloto: int
    IdConstructor: int
    Nro_X: int
    Posicion: int
    Calificacion1: str
    Calificacion2: str
    Calificacion3: str

class Races(BaseModel):
    IdCarrera: Optional[int]
    Año: int
    Ronda: int
    IdCircuito: int
    Nombre_Carrera: str
    Fecha: date
    Tiempo: str
    Url_Carrera: str

class Results(BaseModel):
    IdResultado: Optional[int]
    IdCarrera: int
    IdPiloto: int
    IdConstructor: int
    Nro_X: str
    Parrilla: int
    Posicion: str
    PosicionTexto: str
    PosicionOrden: int
    Puntos: float
    Vueltas: int
    Tiempo: str
    Duracion: str
    VueltaRapida: str
    Rango: str
    TiempoVueltaRapida: str
    VelocidadVueltaRapida: str
    IdEstado: int

class Stops(BaseModel):
    IdParada: Optional[int]
    IdCarrera: int
    IdPiloto: int
    Parada_Nro: int
    Vuelta_Nro: int
    Tiempo: str
    Duracion: int






