#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import (
    String,
    ForeignKey,
    Integer,
    Float,
    Table,
    Column
    )
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )
from typing import Optional, List


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
        ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
        )
)
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
    from models.review import Review
    reviews: Mapped[List['Review']] = relationship(
        Review,
        backref='place',
        cascade='all, delete-orphan'
    )

    amenity_ids = []

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False,
        back_populates="place_amenities"
        )
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """getter for file storage"""
            from models import storage
            from models.amenity import Amenity as A
            data = storage.all(A)
            return [am for am in data.values() if am.id in self.amenity_ids]
        @amenities.setter
        def amenities(self, obj=None):
            """setter for file storage"""
            if obj.__class__.__name__ == "Amenity":
                if obj:
                    self.amenity_ids.append(obj.id)
        @property
        def reviews(self):
            """getter for reviews"""
            import models
            from models.review import Review
            revs = models.storage.all(Review)
            return [
            review for review in revs.values() if review.place_id == self.id
            ]
