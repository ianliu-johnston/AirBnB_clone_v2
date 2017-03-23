#!/usr/bin/python3
from models.base_model import BaseModel, Base
#from models.user import User
#from models.amenity import Amenity
#from models.city import City
#from models.place import Place
#from models.state import State
from models.review import Review
from os import getenv


if getenv(HBNB_TYPE_STORAGE) == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
