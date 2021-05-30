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
     return User.find_user(username) 
def check_existing_user(username):
      '''
    Function that check if a user exists with that username and return a Boolean
    '''
      return User.user_exist(username)
  
def create_credentials(account_name, username, password):
    ''' 
    Function that creates a new credential
    '''
    new_credential = Credentials(account_name, username,password)
    return new_credential

def save_credential(account_name):
    ''' 
    saves a credential
    '''
    Credential.save_credential(account_name)
    
def delete_credential(account_name):
    ''' 
    deletes a credential
    '''
    Credentials.delete(account_name)
    
def find_credential(account_name):
    ''' 
    finds a credential by account name and returns the credential
    '''
    return Credentials.find_credential(account_name)

def check_credential_existing(account_name):
    '''
    chechs if a credential exists with that account_name and retruns a boolean value
    '''
    return Credentials.exists(account_name)
def display_credential():
    ''' 
    returns all saved credentials
    '''
    return Credentials.display_credential()

def
