import pytest
from modules.ui.page_objects.sign_in_page import SignInPage

@pytest.mark.ui 
def test_sign_in_GitHub_wrong_name():
    signin = SignInPage()
    signin.go_to("https://github.com/login")
    signin.try_sign_in_GitHub("wrongmail@wrong.com", "wrongpassword")
    signin.check_title("Sign in to GitHub · GitHub")
    signin.close()

@pytest.mark.ui 
def test_sign_in_Amazon():
    signin = SignInPage()
    signin.go_to("https://www.amazon.com/ref=nav_logo")
    signin.check_title("Amazon.com.Spend less. Smile more")
    signin.find_sign_in_Amazon()
    signin.check_title("Amazon Sign-In")
    signin.close()
