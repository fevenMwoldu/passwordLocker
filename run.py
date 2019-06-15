#!/usr/bin/env python3.7
from locker import User, Credential


def create_user(fname, password):
    '''
    function to create a new user
    '''
    new_user = User(fname, password)
    return new_user


def create_account(userName, siteName, accountName, Cpassword):
    '''
    Function to create a new credential account
    '''
    new_account = Credential(userName, siteName, accountName, Cpassword)
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
    credential.save_credential()


def generated_pass():
    '''
    Function to call the generated password
    '''
    return Credential.generated_pass()


def del_user(user):
    '''
    Function to delete users
    '''
    user.del_user()


def main():
    print("Hello Welcome to the user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        short_code = mainPrompt()
        if short_code == 'ca':
            createAccount()
        elif short_code == 'log':
            login()

        elif short_code == 'ex':
            print("Bye .......")
            break            
        else:
            print("continue working")


def mainPrompt():
    print("Use these short codes : ca - create an account, log - logging in, ex -exit the user list")
    short_code = input().lower()
    return short_code


def createAccount():
    print("for creating a user submit username and password")
    print("Username:")
    fname = input()
    print("Password")
    password = input()
    # create and save new users with username and password.
    save_user(create_user(fname, password))
    print('\n')
    print(f"New Contact {fname} {password} created")
    print('\n')


def login():
    print(
        "for creating an account submit username,site_name,account_name and password")
    print("Username:")
    userName = input()
    print("site name")
    siteName = input()
    print("account name")
    accountName = input()
    print("you credential password:")
    print("Do you want a generated password? if Yes: print Y")
    Cpassword = input()

    if Cpassword == 'Y':
        # calling the function that will generate us a randomly generated password
        Cpassword = generated_pass()
        print(f"here is the generated password :{Cpassword}")

    # create and save new credentials
    save_credential(create_account(
        userName, siteName, accountName, Cpassword))
    print('\n')
    print(
        f"New credentials {userName} {siteName} {accountName} {Cpassword} are created")
    print('\n')


if __name__ == '__main__':
    main()
