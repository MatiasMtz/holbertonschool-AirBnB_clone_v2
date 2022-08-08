#!/usr/bin/python3
""" City Module for HBNB project """
from tkinter import CASCADE
from turtle import back
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete-orphan", \
                          backref="cities")
