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