import pytest
from modules.ui.page_objects.sign_in_page import SignInPage

@pytest.mark.ui 
def test_sign_in_wrong_name():
    signin = SignInPage()
    signin.go_to()
    signin.try_sign_in("wrongmail@wrong.com", "wrongpassword")
    signin.check_title("Sign in to GitHub · GitHub")
    signin.close()
