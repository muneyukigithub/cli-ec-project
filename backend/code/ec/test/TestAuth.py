import sys
sys.path.append("/code/ec/app")

from unittest import TestCase
from unittest.mock import Mock,patch
from user import User
from auth import Auth
from model import UserModel


class TestAuth(TestCase):
    def setUp(self):
        self.user = Mock()
        self.auth = Auth(self.user)

    def test_signup(self):

        # user_input = "admin\npassword\ntest@test.com\n11122223333"
        userdata = {
            "username":"admin",
            "password":"password",
            "email":"email",
            "phonenumber":"phonenumber",
            "is_active":0,
            "role":0
        }

        with patch('auth.Auth.input_userdata',side_effect=[userdata]) as mock_input_userdata:
            with patch('auth.Auth.create_user') as mock_create_user:
                result = self.auth.signup()
                mock_input_userdata.assert_called_once()
                mock_create_user.assert_called_once()
                self.assertEqual(result,True)


    @patch('model.UserModel')
    @patch('auth.Auth.set_user',return_value=True)
    @patch('auth.Auth.input_logindata',return_value=("user","password"))
    @patch('auth.Auth.basic_authenticate')
    @patch('auth.Auth.create_session',return_value=True)
    def test_basic_login(self, mock_create_session, mock_basic_authenticate, mock_input_logindata,mock_set_user,mock_user_model):
        user = mock_user_model.return_value
        user.id = 1
        user.username = "testuser"
        mock_basic_authenticate.side_effect=lambda username,password:user
        
        self.auth.basic_login()
        mock_create_session.assert_called_once()
        mock_basic_authenticate.assert_called_once()
        mock_input_logindata.assert_called_once()
        mock_set_user.assert_called_once()