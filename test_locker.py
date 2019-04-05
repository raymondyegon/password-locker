import unittest
from locker import User
from locker import Credentials


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

        User.users_list = {}

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
        self.new_user.register_user()  # registering user

        assert len(User.users_list) == 1

    def test_register_multiple_user(self):
        '''
        test_register_multiple_user test case to register multiple users
        '''
        self.new_user.register_user()
        test_user = User("monday", "0934idn")

        test_user.register_user()
        assert len(User.users_list) == 2

    # def test_delete_user(self):
    #     '''
    #     test_delete_user test case to test if a user can delete
    #     '''
    #     self.new_user.register_user()
    #     test_user = User("monday", "12345678")

    #     test_user.register_user()

    #     User.delete_user("Raymond")  # deleting a user

    #     assert len(User.users_list) == 1

    def test_user_exist(self):
        '''
        test_user_exist test case to return boolean if we cannot find a user
        '''
        self.new_user.register_user()
        test_user = User("monday", "w12345678")
        test_user.register_user()

        user_exists = User.user_exist("monday")

        assert True == user_exists


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class.
    '''

    def setUp(self):
        self.new_credentials = Credentials("facebook")

    def tearDown(self):
        '''
        Teardown method that does clean up after each test case has run
        '''
        Credentials.platform = []
        Credentials.credentials_list = {}

    def test_init(self):
        '''
        test_init test case to test if the object is initialized
        '''
        assert self.new_credentials.account == "facebook"
