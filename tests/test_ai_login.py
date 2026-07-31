from ai.ai_helper import get_login_credentials
from pages.login_page import LoginPage


def test_ai_login(page):

    credentials = get_login_credentials()

    login = LoginPage(page)

    login.login(
        credentials["username"],
        credentials["password"]
    )

    assert "inventory" in page.url