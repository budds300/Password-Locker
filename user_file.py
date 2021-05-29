import pyperclip


class Credentials:
    '''
    Class that generates new instances credentials
    '''
    credential_list = []  # empty credential list

    def __init__(self, account_name, username, password):
        '''
        __init__ method that helps us define properties for our objects.
            Args:
            username: New credential username
            password: New credential password
            '''
        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):
        '''
        This method deletes credential objects from credential list 
        '''
        credential.credential_list.remove(self)

    @classmethod
    def find_account_name(cls, user_name):
        '''
        method that takes in the account name and returns a credential that matches that account name
            Args:
            account_name:Account name to search for 
        Returns:
            Credentials of person that matches the account name
    '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        This method checks if credentials exists
            Args:
            account_name:Account name to search if it exists
        Returns:
            Boolean:True or false depending on if the credential exists 
            '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True

        return False


    @classmethod
    def display_credential(cls):
        '''
        This method displays/returns the credential list
        '''
        return cls.credential_list


    @classmethod
    def copy_credential(cls, account_name):
        '''
        Method copys credentials
        '''
        credential_found = Credentials.find_account_name(account_name)
        pyperclip.copy(credential_found.account_name)
        
class User:
    '''
    Generates details about users
    '''
    user_list = []
    
    def _init_ (self, username, password):
        '''
         __init__ method for definition of object properties.
    Args:
        
        username:Username of the new user.
        password:Password of the new user.
    '''
        self.username = username
        self.password = password
        
    def save(self):
        ''' 
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
    def delete(self):
        '''
        delete_user method deletes a saved user from user_list
        '''
        User.user_list.remove(self)
    
    def find_user(cil,username):
        ''' '''
        for user in cli.user_list:
            if user.username == username:
                return user 
    def user_exists(cli,username):
        ''' '''
        for user in cli:
            if user.username == username:
                return True
            return False
    
    def copy_user(username):
        ''' '''
        user_found = User.find_user(username)
        pyperclip.copy(user_found.username)
            
