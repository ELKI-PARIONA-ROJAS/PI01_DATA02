from unicodedata import name
from urllib import response
from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User, Circuit, Constructor, Driver, Laptime, Qualifying, Races, Results, Stops
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter() # Esto es un objeto de tipo APIRouter que nos permite crear rutas

@user.get("/users", response_model=List[User], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()

################################################################################


@user.get("/circuits", response_model=List[Circuit], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/constructors", response_model=List[Constructor], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/drivers", response_model=List[Driver], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/laptimes", response_model=List[Laptime], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/qualifying", response_model=List[Qualifying], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/races", response_model=List[Races], tags=["users"])
def get_users():
    return conn.execute(users.selec()).fetchall()

@user.get("/races", response_model=List[Races], tags=["users"])
def get_users():
    return conn.execute(users.selec()).fetchall()

@user.get("/results", response_model=List[Results], tags=["users"])
def get_users():
    return conn.execute(users.selec()).fetchall()

@user.get("/stops", response_model=List[Stops], tags=["users"])
def get_users():
    return conn.execute(users.selec()).fetchall()
