from unicodedata import name
from urllib import response
from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import circuits, constructors, drivers, laptimes, qualifying, races, results, stops
from schemas.user import Circuit, Constructor, Driver, Laptime, Qualifying, Races, Results, Stops
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter() 


@user.get("/circuits", response_model=List[Circuit], tags=["users"])
def get_circuits():
    return conn.execute(circuits.select()).fetchall()

@user.get("/circuits/{id}", response_model=Circuit, tags=["users"])
def get_circuits(id: int):
    return conn.execute(circuits.select().where(users.c.id == id)).first()

@user.get("/constructors", response_model=List[Constructor], tags=["users"])
def get_constructors():
    return conn.execute(constructors.select()).fetchall()

@user.get("/drivers", response_model=List[Driver], tags=["users"])
def get_drivers():
    return conn.execute(drivers.select()).fetchall()

@user.get("/laptimes", response_model=List[Laptime], tags=["users"])
def get_laptimes():
    return conn.execute(laptimes.select()).fetchall()

@user.get("/qualifying", response_model=List[Qualifying], tags=["users"])
def get_qualifying():
    return conn.execute(qualifying.select()).fetchall()

@user.get("/races", response_model=List[Races], tags=["users"])
def get_races():
    return conn.execute(races.select()).fetchall()

@user.get("/results", response_model=List[Results], tags=["users"])
def get_results():
    return conn.execute(results.select()).fetchall()

@user.get("/stops", response_model=List[Stops], tags=["users"])
def get_stops():
    return conn.execute(stops.select()).fetchall() 
