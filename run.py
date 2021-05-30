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

def main():
    print('Hello Wlcome to your User List. What is your name?')
    user_name= input()
    print(f'Hello {user_name}. What do you like to do?')
    print('\n')
    
    while True:
        print("Use these short codes: ca - create a new user, si - sign in to your account , dc - display credentials, fa - find account, fu - find a user, cc - create a new credential, gp - generat a new password, da - delete account, ex - exit user list")
        in_short_code = input().lower()
        
        
        if in_short_code == 'ca':
            print('Create a new account by following the steps below:')
            print('Enter a username')
            username = input()
            print('Enter password')
            password = input()
            
            save_user(create_user(username,password))
            print('\n')
            print(f'Thankyou {username}, you may now proceed to open your account')
            print('\n')
            
        elif in_short_code == 'si':
            print('\n')
            print('Enter your account username')
            username= input()
            print('Enter password')
            password = input()
            if check_existing_user(username):
                save_user= find_user(username)
                print(f'Welcome to your account {saved_user.username}')
                print('\n')
                
        elif in_short_code == 'fu':
            print(" \n Enter any username to find user: \n")
            search_username = input()
            if check_existing_user(search_username):
                search_user= find_user(search_username)
                print(f'{search_user.username}')
                print(f'Password .....{search_user.password}')
                
            else:
                print("Sorry, This account doesn't exist!")
                
        elif in_short_code == 'ex':
            print("Try again later,Goodbye!...")
            break
        
        elif in_short_code == 'cc':
            print("\n Follow the following steps to create a new credential \n")
            print("Enter the account name i.e Instagram/Twitter/Facebook/tiktok/Snapchat")
            account_name= input()
            print("Enter your username for the new account:")
            username = input()
            print("Enter password")
            password = input()
            save_credential(create_credential(account_name, username,password))
            print("\n")
            print(f"You have sccessfylly created a new credential for your new {account_name} account \n")
            
        elif in_short_code== "gp":
            alpha= string.ascii_letters + string.digits
            password= ''.join(choice(alpha) for i in range(8))
            print(f'Your new generated password is: {password}\n')
            
        elif in_short_code == 'dc':
            print('\n')
            if display_credential():
                print('Below is a list of all credentials: \n \n')
                for credential in display_credential():
                    print(f'Name of Account:{credential.account_name}')
                    print (f'Username:{credential.username}')
                    print(f'Password: {credential.password}')
                    print('\n')
                    
            else:
                print('\n Sorry, You do not have any credentials to display')
                
        elif in_short_code== 'fa':
            print('Enter name of account you would wish to search for')
            search_account_name = input()
            if check_credential_existing(search_account_name):
                search_credentials = find_credentials(search_account_name)
                print(f'Name of the account: {search_account_name}')
                print(f'Account Username: {search_credentials.username}')
                print(f'Account Password: {search_credentials.password}')
                
            else:
                print("Sorry, The entered credential does not exist")
                
        elif in_short_code == 'da':
            print("Which account do you wish to delete?")
            delete_account_name=input()
            if check_credential_existing(delete_account_name):
                search_delete_credential = find_credential(delete_account_name)
                delete_credential(search_delete_credential)
                
                print(f"Your {delete_account_name} credentials have been successfully deleted")
                
            else:
                print("Sorry , Credential does not exist")
                
        elif in_short_code == 'ex':
            print("Goodbye ...")
            break
        
        else:
            print("short code not found,Please use the short codes")
            
            
if __name__ == '__main__':
    main()
                    
                
                    
            
            
