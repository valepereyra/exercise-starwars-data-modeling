import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)


class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    modelo = Column(String(250), nullable=False)
    capacidad = Column(String(20), nullable=False)
    creacion = Column(String(20), nullable=False)


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    poblacion = Column(String(20), nullable=False)
    bioma = Column(String(20), nullable=False)


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    altura = Column(String(250), nullable=False)


class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    agregar = Column(String(250), nullable=False)
    eliminar = Column(String(20), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    vehiculos = relationship(Vehiculos)
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    planetas = relationship(Planetas)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
