#!/usr/bin/env python3.7
import sys
from locker import User, Credential
import clipboard

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


def display_user():
    return User.display_users()

def display_credentials():
    return Credential.display_credentials()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    return credential.delete_credential()

def find_credential(siteName):
    return Credential.find_by_sitename(siteName)



def welcomeMessage():
    print("==========================================================")
    print("==================Password Locker App=====================")
    print("==========================================================")
    print('\n')


def main():

    welcomeMessage()

    current_menu = "login"

    while True:
        choice = showMenu(current_menu)

        current_menu = handleAction(current_menu, choice)

        if(current_menu == 'ex'):
            break


def handleAction(menu, choice):
    result = menu

    if menu == "login":
        result = handleLoginMenu(choice)
    elif menu == "main":
        result = handleMainMenu(choice)

    return result


def handleLoginMenu(choice):
    result = "login"

    if choice == 1:
        result = handleLogin()
    elif choice == 2:
        result = handleSignUp()

    return result


def handleLogin():
    result = "login"

    while True:
        print('Login')

        username = input('Username: ')
        password = input('Password: ')

        if User.authenticate(username, password) == True:
            current_user=username
            result = "main"
            break
        else:
            print('Invalid username/password. Please try again.')
    

    return result


def handleSignUp():
    result = "login"

    print('Sign Up')

    while True:
        username = input('Username: ')

        if len(username) == 0:
            print("Empty username is not allowed. Please enter valid username.")
        if User.user_exist(username) == True:
            print("The username {0} is already taken. Please enter another name.".format(username))
        else:
            break

    while True:
        password = input('Password: ')  

        if len(password) == 0:
            print("Empty password is not allowed. Please enter valid password.")
        else:
            break

    user = User(username, password)   

    save_user(user)

    return result


def handleMainMenu(choice):
    result = "main"

    if choice == 1:
        result = handleStoreExistingCredential()
    elif choice == 2:
        result = handleCreateNewCredential() 
    elif choice == 3:
        result = handleViewCredential()
    elif choice == 4:
        result = handleDeleteCredential()
    elif choice == 5:
        result = handleLogout()

    return result

def handleStoreExistingCredential():
    result='main'
    
    account_name=input("Account name: ")
    site_name=input("Site name: ")
    password=input("Password: ")

    credential=Credential(current_user,site_name,account_name,password)
    save_credential(credential)

    return result

def handleCreateNewCredential():
    result='main'
    account_name=input("Account name: ")
    site_name=input("Site name: ")
    password=input("Enter password manually or Enter Y for generated password: ")

    if password == 'Y':
        password=Credential.generated_pass()
        clipboard.copy(password)
        print('The generated password is copied to clipboard.')

    credential=Credential(current_user,site_name,account_name,password)
    save_credential(credential)
    return result

def handleViewCredential():
    result='main'
    show_password=input("Show passwords? [Y/N] ")
    
    for credential in display_credentials():
        if show_password in ["Y", "y"]:
            print('{0}\t\t{1}\t\t{2}'.format(credential.user_site,credential.user_account,credential.password))
        else:
            print('{0}\t\t{1}\t\t{2}'.format(credential.user_site,credential.user_account,"*****"))

    return result

def handleDeleteCredential():
    result='main'
    credential_todelete=input("choose which credential to be deleted: ")
    search_credential=find_credential(credential_todelete)
    search_credential.del_credential()
    return result

def handleLogout():
    result='main'
    print("Bye")
    return result

current_user = None

menus = {
    "main": [
        'Store existing account credential',
        'Create new account credential',
        'View account credential',
        'Delete account credential',
        'Logout'
    ],
    "login": [
        "Log in(existing user)",
        "Sign up(new user)"
    ],
    "other": [

    ]
}


def showMenu(menu_name):
    if(menu_name not in menus):
        raise ValueError(
            'Unknown menu name. Please provide one of the available menu names.')

    menu = menus[menu_name]

    ln = len(menu)

    if(ln < 1):
        raise ValueError('Menu list should have at least one item.')

    print("what would you like to do, choose one number : \n")
    for i in range(ln):
        print("{0}) {1}".format(i+1, menu[i]))

    while True:
        try:
            choice = int(input('\n> '))
            if(choice > 0 and choice <= ln):
                return choice
            else:
                print('\nYou entered invalid menu item. Please try again.\n')
        except ValueError:
            print('\nYou entered invalid menu item. Please try again.\n')


def testMenu():
    current_menu = sys.argv[1]
    choice = showMenu(current_menu)
    print('Your choice is: {0}'.format(current_menu[choice-1]))


if __name__ == '__main__':
    main()
