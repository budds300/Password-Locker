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
          
    def test_user_exists(self):
        '''
        Test_find_by_username is used to test if it's possible to find an existing username
        '''
        self.new_user.save()
        test_user = User('Tamminga','0000') # new user
        test_user.save()
        
        exist_user = User.user_exists('Tamminga')
        self.assertTrue(exist_user)
        
    def test_user_display (self):
        '''
        Test_user_display is to test if the display is working accordingly
        '''
        self.assertEqual(User.display_user(),User.user_list)       
        
class TestCredentials(unittest.TestCase):
    ''' 
      Test class that defines test cases for the Credential class
   Args:
       unittest.TestCase: TestCase class helping to create test cases
   '''
    def setUp(self):
        '''
        
        Set up method to run before each test cases.
        '''
        self.new_user = Credentials('Github','budds300','opensaysme') # create new credentials
    
    Credentials.credential_list = []
    
    def tearDown(self):
        ''' 
        clears tests after a test has been run
        '''
        
        Credentials.credential_list=[]
    
    def test_init_credentials(self):
        ''' 
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.account_name,"Github")
        self.assertEqual(self.new_user.username,"budds300")
        self.assertEqual(self.new_user.password,"opensaysme")
        
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object has been saved into the credentials list
        '''
        self.new_user.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
       
    def test_save_multiple_credentials(self):
        ''' 
        
        '''
        self.new_user.save_credential()
        new_credentials = Credentials('Facebook','Tamminga','knockknock')
        new_credentials.save_credential()
        
        self.assertEqual(len(Credentials.credential_list),2)
        
    def test_delete_credentials (self):
        ''' 
        tests if we can delete a credential from our credentials list
        '''
        self.new_user.save_credential()
        new_credentials=Credentials('Google','budds300','whatdoyouthink?')
        new_credentials.save_credential()
        
        self.new_user.delete_credential()
        self.assertEqual(len(Credentials.credential_list),1) 
        
    def test_find_credentials_by_username(self): 
        ''' 
        to check if we can find a credential by the account name and display more information about it
        '''
        self.new_user.save_credential()
        new_credentials=Credentials('Google','budds300','whatdoyouthink?')  
        new_credentials.save_credential()
        
        found_credentials = Credentials.find_account_name("Google")
        self.assertEqual(found_credentials.password,new_credentials.password)
        
    def test_exists_credentials (self):
        ''' 
        checks if we can return a boolean if we cannot find the credentials
        '''
        
        self.new_user.save_credential()
        new_credentials=Credentials('Google','budds300','whatdoyouthink?')  
        new_credentials.save_credential()
        
        existing_credentials= Credentials.credential_exist("Google")
        self.assertTrue(existing_credentials)
        
    def test_display_credentials (self):
        '''
        returns a list of all credentials saved 
        '''
        self.assertEqual(Credentials.display_credential(),Credentials.credential_list)
       
    def test_copy_account_name(self):
        '''
        test to confirm we are copying the account name from a found credentials
        '''

        self.new_user.save_credential()
        Credentials .copy_account_name("Facebook")

        self.assertEqual(self.new_credential.account_name,pyperclip.paste())

          
if __name__ == '__main__':
    unittest.main()
