import unittest
from locker import User
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
