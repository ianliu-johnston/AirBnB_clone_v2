#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Amenity(**{"name": "amenities"})
        self.model.save()

    def tearDown(self):
        self.model.delete()
        self.cli.do_destroy("Amenity " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "amenities")


if __name__ == "__main__":
    unittest.main()
