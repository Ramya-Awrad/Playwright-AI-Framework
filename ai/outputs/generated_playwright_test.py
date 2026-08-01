from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        username_input = page.locator("#user-name")
        password_input = page.locator("#password")
        login_button = page.locator("#login-button")

        username_input.fill("standard_user")
        password_input.fill("secret_sauce")
        login_button.click()

        assert "inventory.html" in page.url

        browser.close()

test_login()