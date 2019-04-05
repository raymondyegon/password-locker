import unittest
from locker import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class.
    '''

    def setUp(self):
        self.new_user = User("Raymond", "0222d082njknjdk")

    def tearDown(self):
        '''
        Teardown method that does clean up after each test case has run
        '''
        
        User.users_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized
        '''
        assert self.new_user.username == "Raymond"
        assert self.new_user.password == "0222d082njknjdk"

    def test_register_user(self):
        '''
        test_register_user test case to test if a user is registered in the users list
        '''
        self.new_user.register_user() # registering user
        
        assert len(User.users_list) == 1
