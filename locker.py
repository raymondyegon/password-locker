#!/usr/gin/env python3


class User:
    '''
    Class that generates new instances of user
    '''
    users_list = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_user(self):
        '''
        register_user method to register new user to the users_list
        '''
        user_details = {self.username: self.password}
        User.users_list.update(user_details)

    # @classmethod
    # def delete_user(cls, username):
    #     '''
    #     delete_user method to delete a user from the users_list
    #     '''

    #     for key in User.users_list.keys():
    #         if key == username:
    #             del [User.users_list[key]]

    @classmethod
    def user_exist(cls, username):
        '''
        Method to check if a user exist in the users_list

        Args :
            username : the username to search if it exists

        Returns :
            Boolean : True or False depending if the user exists
        '''
        if username in cls.users_list:
            return True
        else :
            return False


class Credentials:
    '''
    Class that generates new instance of credentials
    '''
    credential_list = {}
    platforms = []
    
    def __init__(self, account):
        self.account = account
    
    def register_platform(self):
        '''
         A method to register a new social media account to platforms
        '''
        Credentials.platforms.append(self)
    
    def delete_platform(self):
        '''
        A method to delet a social media platform
        '''
        
        Credentials.platforms.remove(self)