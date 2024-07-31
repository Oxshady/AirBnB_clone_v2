#!/usr/bin/python3
"""This module defines a class to manage Database storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


from os import getenv
import models.base_model


class DBStorage:
    """Database storage management"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        name = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        user = getenv('HBNB_MYSQL_USER')
        passw = getenv('HBNB_MYSQL_PWD')
        url = f"mysql+mysqldb://{user}:{passw}@{host}:3306/{name}"
        self.__engine = create_engine(
            url=url,
            pool_pre_ping=True)
        if (getenv('HBNB_ENV') == "test"):
            base = models.base_model.Base
            base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        classes = []
        objects = {}
        from models.state import State
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.city import City
        if cls is None:
            classes = [
                City,
                Place,
                User,
                Review,
                Amenity,
                State
                ]
        else:
            classes = [cls]
        for cl in classes:
            try:
                objs = self.__session.query(cl).all()
                for obj in objs:
                    key = f"{cl.__name__}.{obj.id}"
                    objects[key] = obj
            except Exception:
                pass
        return objects

    def new(self, obj):
        """Add new object to the current session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes and save them to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and set up the current database session"""
        from models.city import City
        from models.state import State
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        base = models.base_model.Base
        base.metadata.create_all(bind=self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory=session_fact)
        self.__session = Session()
