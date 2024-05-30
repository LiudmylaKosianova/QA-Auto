import pytest
from modules.ui.page_objects.sign_in_page import SignInPage

#@pytest.mark.ui
def test_wrong_name_and_pass():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("wrongemail@wrongemail.com", "wrongpassword")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close()
