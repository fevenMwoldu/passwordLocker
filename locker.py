import random


class User:
    '''
    class that generates new instances of User
    '''

    user_list = []  # Empty user list

    def __init__(self, first_name, password):
        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.first_name = first_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user information from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


class Credential:
    '''
    class that generates new instances of Credentials
    '''

    credentials_list = []  # Empty credential list

    def __init__(self, user_name, user_site, user_account, password):
        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.user_name = user_name
        self.user_site = user_site
        self.user_account = user_account
        self.password = password

    def save_credential(self):
        '''
        save_credential method saves credential objects into creddentials_list
        '''
        Credential.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved user's credential information from the credential_list
        '''
        Credential.credentials_list.remove(self)

    
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the list of users credentials
        '''
        return cls.credentials_list

   

    @classmethod
    def generated_pass(cls):
        '''
        Generateing a password with random
        '''
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = 8
        p = "".join(random.sample(s, passlen))

        return p
