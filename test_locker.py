import unittest
from locker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class.
    '''
    
    def setUp(self):
        self.new_user = User("Raymond", "0222d082njknjdk")
    
    def test_init(self):
        assert self.new_user.username == "Raymond"