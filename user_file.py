import pyperclip
import string



class Credentials:
    '''
    Class that generates new instances credentials
    '''
    credential_list = []  # empty credential list

    def __init__(self, account_name, username, password):
        '''
        __init__ method that helps us define properties for our objects.
            Args:
            account_name:New credentials account name.
            username: New credential username
            password: New credential password
            '''
        self.account_name =account_name
        self.username =username
        self.password =password

    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):
        '''
        This method deletes credential objects from credential list
        '''
        Credentials.credential_list.remove(self)

    @classmethod
    def find_account_name(cli, account_name):
        '''
        method that takes in the account name and returns a credential that matches that account name
            Args:
            account_name:Account name to search for
        Returns:
            Credentials of person that matches the account name
    '''
        for credential in cli.credential_list:
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
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        This method displays/returns the credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_account_name(cls, account):
        credential_found = Credentials.find_account_name(account)
        pyperclip.copy(credential_found.account_name)


class User:
    '''
     Generates details about users
     '''
    user_list = []
    
        

    def __init__(self, username, password):
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
        save user from user list
        '''
        User.user_list.append(self)

    

    def delete(self):
            '''
            delete_user method deletes a saved user from user_list
            '''
            User.user_list.remove(self)

    @classmethod
    def find_by_username(cil, username):
            '''
            takes in a username and returns a user that matches that username.
        Args:
            username: username that is searched for.
        Returns:
            user that matches the username.
            '''
            for user in cli.user_list:
                if user.username == username:
                    return user

    @classmethod
    def user_exists(cli, username):
            '''
            Method that checks if a user exists in the user_list.
            Args:
                username: Username to search if it exists
            Returns :
                Boolean: True or false depending on if the user exists or not
            '''
            for user in cli.user_list:
                if user.username == username:
                    return True

            return False

    @classmethod
    def display_user(cli):
            '''
            method which returns user list
        '''
            return cli.user_list
