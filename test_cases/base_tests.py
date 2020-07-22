from unittest import TestCase
from framework.base_selenium import BaseSelenium
from pages.login_page import Login
from pages.home_page import HomePage


class BaseTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_selenium = BaseSelenium()
        self.login_page = Login()
        self.home_page = HomePage()

    def setUp(self):
        self.base_selenium.get_driver()

    def tearDown(self):
        self.base_selenium.quit_driver()
