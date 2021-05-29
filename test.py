import unittest
from user_file import User, Credentials
import pyperclip


class Test(unittest.TestCase):
    '''
   Test class that defines test cases for the user class
   Args:
       unittest.TestCase: TestCase class helping to create test cases
   '''
    def setUp(self):
        '''
        set up method to run befor each test cases.
        '''
        self.new_user = User('Tamminga-Givondo','123456007psych')# creates user object
        
