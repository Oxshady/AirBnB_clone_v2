#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False
    )
    from models.place_aminety import place_amenity
    place_amenities = relationship('Place', secondary=place_amenity)
