import pytest

@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""

@pytest.mark.change
def test_change_name(user):
    user.name = "Carmin"
    assert user.name == "Carmin"

@pytest.mark.check
def test_name(user):
    assert user.name == "Liudmyla"

@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Kosianova"
    