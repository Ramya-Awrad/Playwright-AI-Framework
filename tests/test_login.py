from pages.login_page import LoginPage

import json


def test_login(page):

    with open("testdata/login_data.json") as f:

        data = json.load(f)

    login = LoginPage(page)

    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    assert "inventory" in page.url