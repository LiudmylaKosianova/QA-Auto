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

# @pytest.mark.uiAmazon
# def test_can_go_to_sign_in_Amazon():
#     pageMonkey = SignInPage()
#     pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
#     pageMonkey.check_title("Amazon.com.Spend less. Smile more")
#     pageMonkey.find_sign_in_Amazon()
#     pageMonkey.check_title("Amazon Sign-In")
#     pageMonkey.close()

# @pytest.mark.uiAmazon
# def test_can_go_to_cart_Amazon():
#     pageMonkey = SignInPage()
#     pageMonkey.go_to("https://www.amazon.com/ref=nav_logo")
#     pageMonkey.check_title("Amazon.com.Spend less. Smile more")
#     pageMonkey.find_and_click(By.ID, "nav-cart-count")
#     pageMonkey.check_title("Amazon.com Shopping cart")
#     pageMonkey.close()

# @pytest.mark.uiAmazon
# def test_can_change_language_DE():
#     singnin = SignInPage()
#     singnin.go_to("https://www.amazon.com/ref=nav_logo")
#     singnin.find_and_click(By.CLASS_NAME, "icp-nav-flag")
#     singnin.find_and_click(By.XPATH, '/html/body/div[1]/div[1]/div/form/div[1]/div[1]/div[5]/div/label/i')
#     singnin.find_and_click(By.ID, "icp-save-button")
#     time.sleep(3)
