#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """The base class for all storage objects in this project"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.now())
    updated_at = Column(DateTime(), nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())

        if kwargs is not None:
            for k in kwargs[0]:
                setattr(self, k, kwargs[0][k])

        """
        for k in kwargs:
            print("kwargs: {}: {}".format(k, kwargs[k]))
        """

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("_sa_instance_state" in dupe):
            dupe.pop('_sa_instance_state', None)
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe

    def delete(self):
        """deleting current instance"""
        models.storage.delete(self.id)
