#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60, collation='latin1_swedish_ci'),
                nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs.get('id'):
            self.id = str(uuid.uuid4())
        if not kwargs.get('created_at'):
            self.created_at = datetime.now()
        if not kwargs.get('updated_at'):
            self.updated_at = datetime.now()

        if args:
            if name:
                self.name = name
            if state_id:
                self.state_id = state_id
        if 'updated_at' in kwargs:
            kwargs['updated_at'] = datetime.\
                    strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.\
                strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        '''if '__class__' in kwargs:
            del kwargs['__class__']'''
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""

        if '_sa_instance_state' in self.__dict__.keys():
            del self.__dict__['_sa_instance_state']

        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)

        return dictionary

    def delete(self):
        """delete the current instance from storage."""
        models.storage.delete(self)
