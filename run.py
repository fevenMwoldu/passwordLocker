#!/usr/bin/env python3.7
import sys
from locker import User, Credential
import clipboard
from prettytable import PrettyTable

def println(s):
    print('')
    print(bcolors.OKGREEN + 'Info: ' + s + bcolors.ENDC)

def print_error(msg):
    print('')
    print(bcolors.FAIL + 'Error: ' + msg + bcolors.ENDC)    

def read(s):
    return input(bcolors.OKBLUE + s + ': ' + bcolors.ENDC)

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

def display_credentials(username):
    return Credential.display_credentials(username)



def find_credential(username, siteName):
    return Credential.find_by_sitename(username, siteName)



def welcomeMessage():
    '''
    A function to display welcome banner
    '''
    print(bcolors.HEADER + " ____                                     _   _               _             " + bcolors.ENDC)
    print(bcolors.HEADER + "|  _ \ __ _ ___ _____      _____  _ __ __| | | |    ___   ___| | _____ _ __ " + bcolors.ENDC)
    print(bcolors.HEADER + "| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |   / _ \ / __| |/ / _ \ '__|" + bcolors.ENDC)
    print(bcolors.HEADER + "|  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |_| |__| (_) | (__|   <  __/ |   " + bcolors.ENDC)
    print(bcolors.HEADER + "|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_(_)_____\___/ \___|_|\_\___|_|   " + bcolors.ENDC)
    print('\n')


def main():
    '''
    The main function that drives user interactivity with the app
    '''
    welcomeMessage()

    current_menu = "login"

    while True:
        choice = showMenu(current_menu)

        current_menu = handleAction(current_menu, choice)

        if(current_menu == 'ex'):
            break


def handleAction(menu, choice):
    '''
    a function to handle menu actions
    '''
    result = menu

    if menu == "login":
        result = handleLoginMenu(choice)
    elif menu == "main":
        result = handleMainMenu(choice)

    return result


def handleLoginMenu(choice):
    '''
    A function to handle login menu
    '''
    result = "login"

    if choice == 1:
        result = handleLogin()
    elif choice == 2:
        result = handleSignUp()
    elif choice == 3:
        result = handleExit()

    return result


def handleLogin():
    '''
    A function that handles our login for our existing user
    '''
    global current_user
    result = "login"

    while True:
        println('Login')

        username = read('Username')
        password = read('Password')

        if User.authenticate(username, password) == True:
            current_user=username
            result = "main"
            break
        else:
            print_error('Invalid username/password. Please try again.')
    

    return result


def handleSignUp():
    '''
    A function that will handle our signup for a new user
    '''
    result = "login"

    println('Sign Up')

    while True:
        username = read('Username')

        if len(username) == 0:
            print_error("Empty username is not allowed. Please enter valid username.")
        if User.user_exist(username) == True:
            print_error("The username {0} is already taken. Please enter another name.".format(username))
        else:
            break

    while True:
        password = read('Password')  

        if len(password) == 0:
            print_error("Empty password is not allowed. Please enter valid password.")
        else:
            break

    user = User(username, password)   

    save_user(user)

    return result

def handleExit():
    '''
    A function to handle exit action
    '''
    println("Bye")
    return 'ex'



def handleMainMenu(choice):
    '''
    A function that will handle our main menu, so that the user can choose
    '''
    result = "main"

    if choice == 1:
        result = handleStoreExistingCredential()
    elif choice == 2:
        result = handleCreateNewCredential() 
    elif choice == 3:
        result = handleViewCredential()
    elif choice == 4:
        result = handleSiteLogin()
    elif choice == 5:
        result = handleDeleteCredential()
    elif choice == 6:
        result = handleLogout()

    return result

def handleSiteLogin():
    global current_user
    result = "main"

    site_name = read('Site name')

    credentials = find_credential(current_user, site_name)

    if len(credentials) > 0:
        clipboard.copy(credentials[0].password)
        println('The password for site: {0}, account: {1} is copied to clip board.'.format(site_name, credentials[0].user_account))
    else:
        println('No credential was found for site: {0}.'.format(site_name))

    return result

def handleStoreExistingCredential():
    '''
    A function for storing the existing credentials of a user
    '''
    global current_user
    result='main'
    
    account_name=read('Account name')
    site_name=read('Site name')
    password=read('Password')

    credential=Credential(current_user,site_name,account_name,password)
    save_credential(credential)

    return result

def handleCreateNewCredential():
    '''
    A function that will create new credentials for logged user
    '''
    global current_user
    result='main'
    account_name=read('Account name')
    site_name=read('Site name')
    password=read('Enter password manually or Enter Y for generated password')

    if password == 'Y':
        password=Credential.generated_pass()
        clipboard.copy(password)
        print('The generated password is copied to clipboard.')

    credential=Credential(current_user,site_name,account_name,password)
    save_credential(credential)
    return result

def handleViewCredential():
    '''
    A function that will let us see out credentials
    '''
    global current_user
    result='main'
    show_password=read("Show passwords? [Y/N]")

    println('Your credentials are:')

    credentials = display_credentials(current_user)   

    t = PrettyTable(['Site', 'Account', 'Password'])
    
    for credential in credentials:
        if show_password in ["Y", "y"]:
            t.add_row([credential.user_site,credential.user_account,credential.password])
        else:
            t.add_row([credential.user_site,credential.user_account,"****"])

    print(t)

    return result

def handleDeleteCredential():
    '''
    A function that deletes a credential by selecting the site name
    '''
    result='main'
    site_name = read('choose which site to be deleted')
    
    credentials = find_credential(current_user, site_name)

    for cred in credentials:
        Credential.delete_credential(cred)

    println('Deleted {0} matching credentials.'.format(len(credentials)))
    
    return result

def handleLogout():
    '''
    A function that logs out from the users credential
    '''
    global current_user
    result='login'
    current_user = None
    
    return result
    

current_user = None

menus = {
    "main": [
        'Store existing account credential', #A menu dictionary with value and key given
        'Create new account credential',
        'View account credentials',
        'I want to login to a site',        
        'Delete account credential',
        'Logout'
    ],
    "login": [
        "Log in(existing user)",
        "Sign up(new user)",
        "Exit"
    ]
}


def showMenu(menu_name):
    '''
    A function tha displays menu and prompts user to select an option
    '''
    if(menu_name not in menus):
        raise ValueError(
            'Unknown menu name. Please provide one of the available menu names.')

    menu = menus[menu_name]

    ln = len(menu)

    if(ln < 1):
        raise ValueError('Menu list should have at least one item.')

    println("what would you like to do, choose one number : \n")
    for i in range(ln):
        print("{0}{1}{2}) {3}{4}{5}".format(bcolors.UNDERLINE, i+1, bcolors.ENDC, bcolors.BOLD, menu[i], bcolors.ENDC))

    while True:
        try:
            choice = int(input(bcolors.OKGREEN + '\n> ' + bcolors.ENDC))
            if(choice > 0 and choice <= ln):
                return choice
            else:
                print_error('You entered invalid menu item. Please try again.\n')
        except ValueError:
            print_error('You entered invalid menu item. Please try again.\n')

def loadTestData():
    '''
    A function to load test data for development
    '''
    save_user(User('fev', '123'))
    save_credential(Credential('fev', 'Facebook', 'fev', 'feb4fev'))
    save_credential(Credential('fev', 'Facebook', 'fev2', 'feb4fev2'))
    save_credential(Credential('fev', 'Gmail', 'fev', 'gm4fev'))

    save_user(User('sim', '456'))
    save_credential(Credential('sim', 'Facebook', 'sim', 'feb4sim'))
    save_credential(Credential('sim', 'Gmail', 'sim', 'gm4sim'))    
    save_credential(Credential('sim', 'Instagram', 'sim', 'insta4sim'))

def testMenu():
    '''
    A function to test how the menu functions
    '''
    current_menu = sys.argv[1]
    choice = showMenu(current_menu)
    println('Your choice is: {0}'.format(current_menu[choice-1]))

class bcolors:
    '''
    Color escape sequences to print colored text in console.
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    '''
    This is the app entry point
    '''
    #loadTestData()
    main()
