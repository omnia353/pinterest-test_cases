from pages.base_page import BasePage
import time

class HomePage(BasePage):

    def search_for_pics(self, word):
        self.base_selenium.LOGGER.info('search for pictures under word  {} .'.format(word))
        self.base_selenium.write(element='home:search-bar', txt=word)
        time.sleep(7)
        self.base_selenium.click_enter(element='home:search-bar2')

    def get_height(self, no):
        text = 'home:picture{}'.format(no)
        return self.base_selenium.get_height(element=text)

    def select_photo(self):
        self.base_selenium.LOGGER.info('click on photo.')
        self.base_selenium.click(element='home:picture1')

    def navigate_to_following(self):
        self.base_selenium.click(element='home:following-btn')
