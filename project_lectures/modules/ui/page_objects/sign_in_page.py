from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_element = self.driver.find_element(By.ID, "login_field")
        login_element.send_keys(username)
        login_pass = self.driver.find_element(By.ID, "password")
        login_pass.send_keys(password)
        sign_in = self.driver.find_element(By.NAME, "commit")
        sign_in.click()

    def check_title(self, title_expected):
        return self.driver.title == title_expected