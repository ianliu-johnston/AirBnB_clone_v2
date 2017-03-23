#!/usr/bin/python3
from models.base_model import BaseModel
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
storage.reload()
