#!/usr/gin/env python3

class User:
    '''
    Class that generates new instances of user
    '''
    users_list = []
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def register_user(self):
        '''
        register_user method to register new user to the users_list
        '''
        User.users_list.append(self)
