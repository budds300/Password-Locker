import string
import random
import choice
from users import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user= User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user() 
    
def find_user(username):
     '''
    Funtion that finds a user by a login and returns the user
    '''
     return User.user_exist(username)