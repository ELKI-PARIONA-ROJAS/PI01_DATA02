from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float
from config.db import meta, engine

users = Table('users', meta,Column('id', Integer, primary_key=True),
                            Column('name', String(255)),Column('email', String(255)),
                            Column('password', String(255)))

circuits = Table( 'circuits', meta,
    Column('IdCircuito', Integer),
    Column('Ciudad', String(50)),
    Column('Nombre_Circuito', String(50)),
    Column('Localidad', String(50)),
    Column('Pais', String(50)),
    Column('Latitud', Float),
    Column('Longitud', Float),
    Column('Altitud', Integer),
    Column('Url_Circuito', String(50)))

constructors = Table( 'constructors', meta,
    Column('IdConstructor', Integer),
    Column('NombreConstructor', String(50)),
    Column('Nacionalidad', String(50)),
    Column('UrlConstructor', String(50)))

drivers = Table( 'drivers', meta,
    Column('IdPiloto', Integer),
    Column('Nombre_Piloto', String(50)),
    Column('Nro_Matricula', String(50)),
    Column('Codigo', String(50)),
    Column('Nombre', String(50)),
    Column('Apellido', String(50)),
    Column('Nacimiento', Date),
    Column('Nacionalidad', String(50)),
    Column('Url_Piloto', String(50)))

laptimes = Table( 'laptimes', meta,
    Column('IdCarrera', Integer),
    Column('IdPiloto', Integer),
    Column('IdVuelta', Integer),
    Column('Posicion', Integer),
    Column('Tiempo', String(50)),
    Column('Duracion(ms)', Integer))

qualifying = Table( 'qualifying', meta,
    Column('IdCalificacion', Integer),
    Column('IdCarrera', Integer),
    Column('IdPiloto', Integer),
    Column('IdConstructor', Integer),
    Column('Nro_X', Integer),
    Column('Posicion', Integer),
    Column('Calificacion1', String(50)),
    Column('Calificacion2', String(50)),
    Column('Calificacion3', String(50)))

races = Table('races', meta,
    Column('IdCarrera',Integer),
    Column('Año', Integer),
    Column('Ronda', Integer),
    Column('IdCircuito', Integer),
    Column('Nombre_Carrera', String(50)),
    Column('Fecha', Date),
    Column('Tiempo', String(50)),
    Column('Url_Carrera', String(50)))

results = Table( 'results', meta,
    Column('IdResultado', Integer),
    Column('IdCarrera', Integer),
    Column('IdPiloto', Integer),
    Column('IdConstructor', Integer),
    Column('Nro_X', String(50)),
    Column('Parrila', Integer),
    Column('Posicion', String(50)),
    Column('PosicionTexto', String(50)),
    Column('PosicionOrden', Integer),
    Column('Puntos', Float),
    Column('Vueltas', Integer),
    Column('Tiempo', String(50)),
    Column('Duracion(ms)', String(50)),
    Column('VueltaRapida', String(50)),
    Column('Rango', String(50)),
    Column('TiempoVueltaRapida', String(50)),
    Column('VelocidadVueltaRapida', String(50)),
    Column('IdEstado', Integer))

stops = Table( 'stops', meta,
    Column('IdParada', Integer),
    Column('IdCarrera', Integer),
    Column('IdPiloto', Integer),
    Column('Parada_Nro', Integer),
    Column('Vuelta_Nro', Integer),
    Column('Tiempo', String(50)),
    Column('Duracion(ms)', Integer))

meta.create_all(engine)