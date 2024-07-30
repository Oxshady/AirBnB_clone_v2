#!/usr/bin/python3
""" State Module for HBNB project """
from typing import List
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
import models.city
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    cities: Mapped[List['models.city.City']] = relationship(
        models.city.City,
        backref='state',
        cascade='all, delete-orphan'
        )
    @property
    def cities(self):
        """retruning all instance of City that has relationship with instance of State"""
        from models import storage
        cities = storage.all(models.city.City)
        return [city for city in cities.values() if city.state_id == self.id]
