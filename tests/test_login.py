import pytest
from pages.login_page import LoginPage

import json

@pytest.mark.smoke
def test_login(page):

    with open("testdata/login_data.json") as f:

        data = json.load(f)

    login = LoginPage(page)

    valid_user = data["users"][0]

    login.login(
        valid_user["username"],
        valid_user["password"]
    )

    assert "inventory" in page.url