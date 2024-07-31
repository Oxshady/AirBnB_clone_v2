#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import (
    relationship, 
    Mapped,
    mapped_column
    )
from sqlalchemy import String, ForeignKey
from typing import List


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False
        )
    state_id: Mapped[str] = mapped_column(
        String(60),
        ForeignKey('states.id'),
        nullable=False
        )
    from models.place import Place
    places: Mapped[List['Place']] = relationship(Place, backref='cities', cascade='all, delete-orphan')
