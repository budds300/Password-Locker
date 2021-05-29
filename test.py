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
       
    def test_init(self):
         '''
        test_init test case to test if the object is initialized properly
        '''
        
         self.assertEqual(self.new_user.username, "Tamminga-Givondo")
         self.assertEqual(self.new_user.password,'123456007psych')
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]
        
    def test_save_username(self):
         '''
        test_save_username test case to test if the username object is saved into
         the user list
        '''
         self.new_user.save()
         self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_username(self):
        '''
        test_save_multiple username test case is to test if multiple username objects are saved into the user list
        '''
        self.new_user.save()
        test_save = User("Budds",'5432juan')
        test_save.save()
        self.assertEqual(len(User.user_list),2)
         
    def test_delete_username(self):
          '''
        test_delete_user to test if it's possible to remove a user from user_list
        '''
          self.new_user.save()
          test_user = User("Tamminga","000")# adds a contact
          test_user.save()
          self.new_user.delete()
          self.assertEqual(len(User.user_list),1)
          
          def test_find_user
if __name__ == '__main__':
    unittest.main()
