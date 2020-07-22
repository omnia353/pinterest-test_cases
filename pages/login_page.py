from pages.base_page import BasePage
import time

class Login(BasePage):

    def login(self, username, password):
        self.base_selenium.LOGGER.info('Fill in login form.')
        self.base_selenium.click(element='login:login_btn')
        self.base_selenium.LOGGER.info('Login {} : {}.'.format(username, password))
        time.sleep(5)
        self.base_selenium.write(element='login:e-mail_ip', txt=username)
        time.sleep(5)
        self.base_selenium.write(element='login:pass_ip', txt=password)
        time.sleep(5)
        self.base_selenium.click(element='login:confirm_login_btn')
