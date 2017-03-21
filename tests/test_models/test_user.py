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


class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = User()
        self.model.save()

    def tearDown(self):
        self.cli.do_destroy("User " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")


if __name__ == "__main__":
    unittest.main()
