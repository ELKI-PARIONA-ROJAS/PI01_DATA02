from sqlalchemy import Column, Integer, String
from app.conexion import Base

# Todo lo necesario para crear la tabla users

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    nombre = Column(String(50))
    rol = Column(String(50))
    estado = Column(Integer)

    class Config:
        orm_mode = True


