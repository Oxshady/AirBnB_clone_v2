#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id: Mapped[str] = mapped_column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
        )
    user_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey('users.id'),
        nullable=False
        )
    name: Mapped[str] = mapped_column(
        String(128),
        nullable=False
        )
    description: Mapped[Optional[str]] = mapped_column(
        String(1024),
        nullable=True
        )
    number_rooms: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
        )
    number_bathrooms: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
        )
    max_guest: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
        )
    price_by_night: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
        )
    latitude: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True
        )
    longitude: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True
        )
    amenity_ids = []
