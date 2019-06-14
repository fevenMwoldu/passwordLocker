import unittest # Importing the unittest module
from locker import User,Credential #Importing the user and credential classes

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("feven","mogos","fev@gmail.com") # create User object

    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
            '''
        User.user_list=[] 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"feven")
        self.assertEqual(self.new_user.last_name,"mogos")
        self.assertEqual(self.new_user.password,"fev@gmail.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
        '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
        self.new_user.save_user()
        test_user=User("fname","lname","abc123") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    

#codes here for the credentials part
class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases for the credential class.
        '''
        self.new_credential = Credential("feven","facebook","feven","123abc") # create credential object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
         
        Credential.credentials_list=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly for the credential class
        '''

        self.assertEqual(self.new_credential.user_name,"feven")
        self.assertEqual(self.new_credential.user_site,"facebook")
        self.assertEqual(self.new_credential.user_account,"feven")
        self.assertEqual(self.new_credential.password,"123abc")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the new credendial information is saved into
         the credenttial list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential infos
        to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential=Credential("feven","facebook","feven","123abc") #new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)

if __name__ == '__main__':
    unittest.main()
