from modules.ui.page_objects.base_page import BasePage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class SignInPage(BasePage):    
    #URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self,url):
        self.driver.get(url)

    def try_sign_in_GitHub(self, username, password):
        username_element = self.driver.find_element(By.ID, "login_field")
        username_element.send_keys(username)

        password_element = self.driver.find_element(By.ID, "password")
        username_element.send_keys(password)

        sign_in_element = self.driver.find_element(By.NAME, "commit")
        sign_in_element.click()
    
    def find_sign_in_Amazon(self):
        signin_element = self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
        signin_element.click()

    def find_and_click(self, identifier, value):
        signin_element = self.driver.find_element(identifier, value)
        signin_element.click()

    def check_title(self, title_expected):
        return self.driver.title == title_expected
    
    def find_language(self):
        element = self.driver.find_element(By.TAG_NAME, "html")
        language = element.get_attribute("lang")
        return language
    
    def get_cart_count_Amazon(self):
        element = self.driver.find_element(By.ID, 'nav-cart-count')
        count = int(element.text)
        return count


    



