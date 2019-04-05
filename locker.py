#!/usr/gin/env python3

class User:
    '''
    Class that generates new instances of user
    '''
    users_list = []
    
    def __init__(self, username, password):
        self.username = username
        self.password = password