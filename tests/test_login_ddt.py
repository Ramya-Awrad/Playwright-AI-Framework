import json
import pytest

from pages.login_page import LoginPage


with open("testdata/login_data.json") as f:
    users = json.load(f)["users"]


@pytest.mark.parametrize("user", users)
def test_login_data_driven(page, user):

    login = LoginPage(page)

    login.login(user["username"], user["password"])

    if user["expected"] == "success":
        assert "inventory" in page.url

    else:
        assert "Epic sadface" in login.get_error_message()