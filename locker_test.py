import unittest  # Importing the unittest module
from locker import User, Credential  # Importing the user and credential classes


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("feven", "abc123")  # create User object

    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "feven")
        self.assertEqual(self.new_user.password, "abc123")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
        self.new_user.save_user()
        test_user = User("fname", "abc123")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("feven", "a1b1c1")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.user_list)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("feven", "a1b1c1")  # new user
        test_user.save_user()

        user_exists = User.user_exist("feven")

        self.assertTrue(user_exists)


# codes here for the credentials part
class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases for the credential class.
        '''
        self.new_credential = Credential(
            "feven", "facebook", "feven", "123abc")  # create credential object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credential.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly for the credential class
        '''

        self.assertEqual(self.new_credential.user_name, "feven")
        self.assertEqual(self.new_credential.user_site, "facebook")
        self.assertEqual(self.new_credential.user_account, "feven")
        self.assertEqual(self.new_credential.password, "123abc")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the new credendial information is saved into
         the credenttial list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credential infos
        to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "feven", "facebook", "feven", "123abc")  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list), 2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential of a user 
        '''
        self.new_credential.save_credential()
        test_credential = Credential(
            "feven", "facebook", "feven", "123abc")  # new Credential
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting credential of a user
        self.assertEqual(len(Credential.credentials_list), 1)

    def test_display_all_userCredentials(self):
        '''
        method that returns a list of all user credentials saved
        '''

        self.assertEqual(Credential.display_credentials("feven"),
                         Credential.credentials_list)

    def test_credentialSite_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credntial site.
        '''

        self.new_credential.save_credential()
        test_credential = Credential(
            "feven", "facebook", "feven", "123abc")  # new credential
        test_credential.save_credential()

        credentialSite_exists = Credential.credentialSite_exist("facebook")

        self.assertTrue(credentialSite_exists)

    def test_find_credential_by_sitename(self):
        '''
        test to check if we can find a users credential by sitename and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("feven", "Gmail", "feven", "123abc") # new credential
        test_credential.save_credential()

        found_credential = Credential.find_by_sitename("feven", "facebook")

        self.assertEqual(len(found_credential), 1)
        self.assertEqual(found_credential[0].user_name,test_credential.user_name)


if __name__ == '__main__':
    unittest.main()
