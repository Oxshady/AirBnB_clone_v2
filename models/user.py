#!/usr/bin/python3
"""This module defines a class User"""
from typing import Optional, List
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(
        String(128),
        nullable=False
        )
    password: Mapped[str] = mapped_column(
        String(128),
        nullable=False
        )
    first_name: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=False
        )
    last_name: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=False
        )
    import models.place
    places: Mapped[List['models.place.Place']] = relationship(
        models.place.Place,
        backref="user",
        cascade='all, delete-orphan'
        )
    from models.review import Review
    reviews: Mapped[List['Review']] = relationship(
        Review,
        backref='user',
        cascade='all, delete-orphan'
    )
