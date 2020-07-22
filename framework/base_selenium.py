from testconfig import config
from loguru import logger
from selenium import webdriver
from elements import elements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseSelenium:
    IMPLICITLY_WAIT = 30

    LOGGER = logger

    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.url = config['site']['url']
        self.email = config['account']['email']
        self.password = config['account']['pass']
        self.elements = elements

    def get_driver(self):
        self.driver = webdriver.Chrome(config['driverpath']['path'])
        self.driver.implicitly_wait(BaseSelenium.IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_url(self):
        self.driver.get(self.url)

    def _get_method_value(self, element):
        element_page, element_name = element.split(':')
        method = self.elements[element_page][element_name]['method'].upper()
        value = self.elements[element_page][element_name]['value']

        return method, value

    def _return_element(self, element):
        method, value = self._get_method_value(element)
        if method == 'NAME':
            element = self.driver.find_element_by_name(value)
        elif method == 'CLASS_NAME':
            element = self.driver.find_elements_by_class_name(value)[0]
        elif method == 'XPATH':
            element = self.driver.find_element_by_xpath(value)
        elif method == 'ID':
            element = self.driver.find_element_by_id(value)
        elif method == 'TAG_NAME':
            element = self.driver.find_elements_by_tag_name(value)[1]
        return element

    def wait_until_element_located(self, element):
        method, value = self._get_method_value(element)
        if method == 'xpath':
            self.wait.until(EC.visibility_of_element_located((By.XPATH, value)))
        else:
            self.wait.until(EC.visibility_of_element_located((getattr(By, method), value)))

    def write(self, element, txt):
        self.wait_until_element_located(element=element)
        self._return_element(element).send_keys(txt)

    def get_text(self, element):
        self.wait_until_element_located(element=element)
        txt = self._return_element(element).text
        return txt

    def submit(self, element):
        self._return_element(element).submit()

    def click(self, element):
        self._return_element(element).click()

    def get_current_url(self):
        return self.driver.current_url

    def click_enter(self, element):
        self._return_element(element).send_keys(Keys.ENTER)

    def get_height(self, element):
        return self._return_element(element=element).size.get('height')

    def quit_driver(self):
        self.driver.quit()
