import pytest
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com/login")
        page.fill("input[name='username']", "valid_username")
        page.fill("input[name='password']", "valid_password")
        page.click("button[type='submit']")
        page.wait_for_url("https://example.com/dashboard")
        browser.close()

def test_login_failure():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com/login")
        page.fill("input[name='username']", "invalid_username")
        page.fill("input[name='password']", "invalid_password")
        page.click("button[type='submit']")
        assert page.locator("text='Invalid username or password'").is_visible()
        browser.close()