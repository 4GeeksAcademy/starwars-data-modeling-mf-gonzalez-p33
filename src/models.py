import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
        __tablename__ = 'User'
        id = Column(Integer, primary_key=True)
        username = Column(String(250), nullable=False)
        firstname = Column(String(250), nullable=False)
        lastname = Column(String(250), nullable=False)
        email= Column(String(250))
        password = Column (String(250),nullable= False)

        def to_dict(self):
            return {}


class Favorite (Base):
     __tablename__ = 'Favorites'
     id = Column(Integer, primary_key=True)
     user = Column(Integer, ForeignKey("User.id"))
     character = Column(String(250), ForeignKey('Characters.id'), nullable = True)
     planet = Column(String(250), ForeignKey('Planets.id'), nullable = True)
     vehicles = Column(String(250), ForeignKey('Vehicles.id'), nullable = True)
     species = Column(String(250), ForeignKey('Species.id'), nullable = True)
     
     def to_dict(self):
        return {}


class Characters (Base):
      __tablename__ = "Characters"
      id = Column(Integer, primary_key=True)
      name = Column (String(250), nullable=False)  

      def to_dict(self):
        return {}


class Planets (Base):
      __tablename__ = "Planets"
      id = Column(Integer, primary_key=True)
      name = Column (String(250), nullable=False)
      population = Column (String(250), nullable=False)
      gravity = Column(Integer, nullable = False)
      terrain = Column (String(250), nullable=False)
      climate = Column (String(250), nullable=False) 

      def to_dict(self):
        return {}   
      

class Vehicles (Base):
      __tablename__ = "Vehicles"
      id = Column(Integer, primary_key=True)
      model = Column (String(250), nullable=False)
      manufacturer = Column (String(250), nullable=False)
      cost = Column(Integer, nullable=False)
      passenger = Column(Integer, nullable=False) 

      def to_dict(self):
        return {}
      

class Species (Base):
      __tablename__ = "Species"
      id = Column(Integer, primary_key=True)
      name = Column (String(250), nullable=False)
      classification = Column (String(250), nullable=False)
      lenguage = Column (String(250), nullable=False)
      skin_color = Column (String(250), nullable=False)
      hair_color = Column (String(250), nullable=False)

      def to_dict(self):
        return {}
      

     
      



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
