from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        login = LoginPage(page)

        login.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

        browser.close()