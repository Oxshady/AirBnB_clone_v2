#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id: Mapped[str] = mapped_column(
        String(60),
        primary_key=True
        )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
        )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
        )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        if not kwargs:
            from models import storage
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k == 'updated_at':
                    kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
                if k == 'created_at':
                    kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'],
                        '%Y-%m-%dT%H:%M:%S.%f'
                        )
                if k == '__class__':
                    del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """delete object from storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            if "_sa_instance_state" in dictionary.keys():
                del dictionary['_sa_instance_state']
        except Exception:
            pass
        return dictionary
