#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    first_name: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(128))
