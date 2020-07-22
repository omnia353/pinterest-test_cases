from test_cases.base_tests import BaseTest
from parameterized import parameterized
import time


class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url()

    def test001_login_correct(self):
        """
        Login with valid data
        """
        self.login_page.login(username=self.base_selenium.email, password=self.base_selenium.password)
        self.base_selenium.LOGGER.info('Login succeded and go to home page.')
        self.assertIn('Welcome, Omnia!', self.base_selenium.get_text(element='home:header'))

    @parameterized.expand([
        ('xxxxxxx', 'xxxxxxx'),
        ('xx@yahoo.com', ''),
    ])
    def test002_login_incorrect_data(self, username, password):
        """
        Login with non-valid data
        """
        self.login_page.login(username=username, password=password)
        text = self.base_selenium.get_text(element='login:title')
        self.base_selenium.LOGGER.info('succed to fail to login.')
        self.assertEqual('Get your next', text)
