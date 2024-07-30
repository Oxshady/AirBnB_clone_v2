#!/usr/bin/python3
"""This module defines a class to manage Database storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from os import getenv

import models.city
class DBStorage:
    """db management"""
    __engine = None
    __session = None
    def __init__(self):
        """constructor"""
        name = getenv.get('HBNB_MYSQL_DB')
        host = getenv.get('HBNB_MYSQL_HOST')
        user = getenv.get('HBNB_MYSQL_USER')
        passw = getenv.get('HBNB_MYSQL_PWD')
        url = f"mysql+mysqldb://{user}:{passw}@{host}:3306/{name}"
        self.__engine = create_engine("mysql://shadi:1@localhost:3306/hbtn_0e_0_usa",
                                pool_pre_ping=True)
        if (getenv.get('HBNB_ENV') == "test"):
            base = models.base_model.Base
            base.metadata.drop_all(bind=self.__engine)
    def all(self, cls=None):
        import models.base_model
        import models.city
        import models.state
        import models.user
        import models.amenity
        import models.place
        import models.review        
        classes = []
        objects = {}
        if not cls:
            classes = [
                models.city.City,
                models.state.State,
                models.user.User,
                models.review.Review,
                models.amenity.Amenity,
                models.place.Place
                ]
        else:
            classes = [cls]
        for cl in classes:
            objs = self.__session.query(cl).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects.update({key:obj})
        return objects
    def new(self, obj):
        """add new object to current session"""
        if obj:
            self.__session.add(obj)
    def save(self):
        """commit all changes and save the changes to the db"""
        self.__session.commit()
    def delete(self, obj=None):
        """delete object from current user"""
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """create tables from created schema"""
        from models.city import City
        from models.state import State
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        from models.place import Place
        base = models.base_model.Base
        base.metadat.create_all(bind=self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory=session_fact)
        self.__session = Session()
