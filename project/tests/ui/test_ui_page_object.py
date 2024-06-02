import pytest
from modules.ui.page_objects.sign_in_page import SignInPage
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui 
def test_sign_in_GitHub_wrong_name():
    signin = SignInPage()
    signin.go_to("https://github.com/login")

    signin.try_sign_in_GitHub("wrongmail@wrong.com", "wrongpassword")
    signin.check_title("Sign in to GitHub · GitHub")
    signin.close()

@pytest.mark.uiAmazon
def test_can_go_to_sign_in_Amazon():
    pageMonkey = SignInPage()
    pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
    pageMonkey.check_title("Amazon.com.Spend less. Smile more")
    pageMonkey.find_sign_in_Amazon()
    pageMonkey.check_title("Amazon Sign-In")
    pageMonkey.close()

@pytest.mark.uiAmazon
def test_can_go_to_cart_Amazon():
    pageMonkey = SignInPage()
    pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
    pageMonkey.check_title("Amazon.com.Spend less. Smile more")
    pageMonkey.find_and_click(By.ID, "nav-cart-count")
    pageMonkey.check_title("Amazon.com Shopping cart")
    pageMonkey.close()

@pytest.mark.uiAmazon
def test_can_get_page_language():
    pageMonkey = SignInPage()
    pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
    language = pageMonkey.find_language()
    assert language == "en-us"
    pageMonkey.close()

@pytest.mark.uiAmazon
def test_can_change_language_DE():
    pageMonkey = SignInPage()
    pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
    language = pageMonkey.find_language()
    assert language != "de-de"
    pageMonkey.find_and_click(By.CLASS_NAME, "icp-nav-flag")
    pageMonkey.find_and_click(By.XPATH, '/html/body/div[1]/div[1]/div/form/div[1]/div[1]/div[5]/div/label/i')
    pageMonkey.find_and_click(By.ID, "icp-save-button")
    time.sleep(2) # without this, page doesn't have time to load and fails the test
    language = pageMonkey.find_language()
    assert language == "de-de"
    pageMonkey.close()

@pytest.mark.uiAmazon
def test_can_get_cart_count():
    pageMonkey = SignInPage()     
    pageMonkey.go_to("https://www.amazon.com")
    count = pageMonkey.get_cart_count_Amazon()
    assert count == 0
    pageMonkey.close()

@pytest.mark.uiAmazon
def test_can_add_to_and_delete_from_cart():
    pageMonkey = SignInPage()     
    pageMonkey.go_to("https://www.amazon.com")
    count = pageMonkey.get_cart_count_Amazon()
    assert count == 0
    pageMonkey.go_to("https://www.amazon.com/Selenium-Python-Simplified-Beginners-Automation\
                     /dp/B08R77TV24/ref=sr_1_1?crid=UZ28IPZ6O8IP&dib=eyJ2IjoiMSJ9._\
                     4A3s8NzMzOkU7fXm-eYjItCju-rvvKEh60RlF2L78i8VQLTg0Q4u9kLn37jmvfIiQIGAonJo08U\
                     _wzLsCizyxuw5s9OYeh1U1GKU1_0nTqZbDJPo1woV-ionmDAZ-xM1EHu1Y4f4WYJxTEgDHTWj-\
                     27Jz60sDFovDlxgKWZsEW-Vg--XNybDZuhxuQoq2key1TN6WPGlkZzEyF3xgcQogo0pIWNXc6CB\
                     jBvk58PX00.bZWB_2IaSVpx7aMspzSJ1cxyavOZKcoEISVuVus_QYI&dib_\
                     tag=se&keywords=selenium+with+python&qid=1717333711&s=books&sprefix\
                     =selenium+with+python%2Cstripbooks-intl-ship%2C183&sr=1-1")
    pageMonkey.find_and_click(By.ID, "add-to-cart-button")
    count = pageMonkey.get_cart_count_Amazon()
    assert count != 0
    pageMonkey.find_and_click(By.ID, "nav-cart-count")
    time.sleep(3)    
    pageMonkey.find_and_click(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/div[1]/span[2]/span/input')
    time.sleep(2)
    count = pageMonkey.get_cart_count_Amazon()
    assert count == 0
    pageMonkey.close()
