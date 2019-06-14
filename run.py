#!/usr/bin/env python3.7
from locker import User,Credential
def create_user(fname,password):
    '''
    function to create a new user
    '''
    new_user=User(fname,password)
    return new_user
def create_account(userName,siteName,accountName,Cpassword):
    '''
    Function to create a new credential account
    '''
    new_account=Credential(userName,siteName,accountName,Cpassword)
    return new_account
def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()
def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential
def generated_pwd(pwd):
    '''
    Function to call the generated password
    '''
    pwd.generated_pwd()

def del_user(user):
    '''
    Function to delete users
    '''
    user.del_user()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    
    while True:

                  print("Use these short codes : ca - create an account, log - logging in, ex -exit the user list")
                  short_code = input().lower()
                  if short_code == 'ca':
                            print("for creating a user submit username and password")
                            print("Username:")
                            fname = input()
                            print("Password")
                            password=input()
                            save_user(create_user(fname,password)) # create and save new users with username and password.
                            print ('\n')
                            print(f"New Contact {fname} {password} created")
                            print ('\n')
                  elif short_code == 'log':
                       print("for creating an account submit username,site_name,account_name and password")
                       print("Username:")
                       userName=input()
                       print("site name")
                       siteName=input()
                       print("account name")
                       accountName=input()
                       print("you credential password:")
                       print("Do you want a generated password? if Yes: print Y")
                       Cpassword=input()
                       if Cpassword =='Y':
                           print("here is the generated password:")
                           generated_pwd() #calling the function that will generate us a randomly generated password
                       else:
                            Cpassword=input()
                       save_credential(create_account(userName,siteName,accountName,Cpassword)) #create and save new credentials
                       print('\n')
                       print(f"New credentials {userName}{siteName}{accountName}{Cpassword} are created")
                       print('\n')
                       
                       
                       


                    
                  #elif expression:
                    #pass
                
                  elif short_code == 'ex':
                        print("Bye .......")
                        break
                       #pass                           
                  else:
                      print("continue working")
            








if __name__ == '__main__':
    main()
