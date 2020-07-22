from test_cases.base_tests import BaseTest
from parameterized import parameterized
import time


class HomeTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.base_selenium.get_url()
        self.login_page.login(username=self.base_selenium.email, password=self.base_selenium.password)

    @parameterized.expand(['dog','cats'])
    def test001_search_photo(self, word):
        """
        Validate that i can search with word
        """
        self.home_page.search_for_pics(word=word)
        url = self.base_selenium.get_current_url()
        self.assertIn(word, url)

    def test002_zoom_photo(self):
        """
        Check if i can zoom the photo
        """
        time.sleep(5)
        url1 = self.base_selenium.get_current_url()
        height = self.home_page.get_height()
        print(height)
        self.home_page.select_photo()
        url2 = self.base_selenium.get_current_url()
        self.base_selenium.LOGGER.info('Succeed in zooming into the photo.')
        self.assertNotEqual(url1, url2)

    def test002_zoom_photo(self):
        """
        Check if i can zoom the photo
        """
        h1 = self.home_page.get_height('1')
        self.home_page.select_photo()
        h2 = self.home_page.get_height('2')
        self.base_selenium.LOGGER.info('Succeed in zooming into the photo.')
        self.assertGreater(h2, h1)

    def test003_goto_following(self):
        """
          Check if i can navigate from home to following
        """
        self.home_page.navigate_to_following()
        url = self.base_selenium.get_current_url()
        self.assertIn('following', url)
        self.base_selenium.LOGGER.info('Navigate to the following page.')
