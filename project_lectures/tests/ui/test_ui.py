import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# @pytest.mark.ui  # for older chrome browser versions
# def test_incorrect_username():
#     driver = webdriver.Chrome(
#              service=Service("/home/carmin/Public/QA-Auto/project_lectures/"+
#                              "chromedriver"))
#     driver.get("https://github.com/login")
#     driver.close()


@pytest.mark.ui  
def test_incorrect_username():
    driver = webdriver.Chrome(
             service=Service(ChromeDriverManager().install()))
    driver.get("https://github.com/login")
    login_element = driver.find_element(By.ID, "login_field")
    login_element.send_keys("wrongaddress@wrongmai.com")
    login_pass = driver.find_element(By.ID, "password")
    login_pass.send_keys("wrongpassword")
    sign_in = driver.find_element(By.NAME, "commit")
    sign_in.click()
    time.sleep(3)
    driver.close()


