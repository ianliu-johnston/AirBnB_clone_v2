#!/usr/bin/python3
"""
Creating a new engine that
manages database storage
"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mymsqldb://{}:{}@{}/{}'.format(
                                      getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB')))
        self.__my_list = {"User":User}
        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict={}
#        my_list = ["User", "State", "City", "Amenity", "Place", "Review"]
        if cls is None:
            for item in self.__session.query(my_list):
                new_dict[item.id] = item
        else:
            for item in self.__session.query(cls):
                new_dict[item.id] = item
        return (new_dict)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
