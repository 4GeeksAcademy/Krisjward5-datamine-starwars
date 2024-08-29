import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

class Planet(Base):
    __tablename__ = "Planet"
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(255), nullable=False)
    planet_details = Column(String(255), nullable=False)
    planet_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

class Character(Base):
    __tablename__ = "Character"
    id = Column(Integer, primary_key=True)
    character_name = Column(String(255), nullable=False)
    character_details = Column(String(255), nullable=False)
    character_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

class CharacterFavorite(Base):
    __tablename__ = "Character_Favorite"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('Character.id'), nullable=False)
    user_id = Column(String, ForeignKey('User.id'), nullable=False)

class PlanetFavorite(Base):
    __tablename__ = "Planet_Favorite"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('Planet.id'), nullable=False)
    user_id = Column(String, ForeignKey('User.id'), nullable=False)
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
