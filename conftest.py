import json
import pytest
from playwright.sync_api import sync_playwright
from utils.screenshot import capture


@pytest.fixture(scope="function")
def page():

    with open("config/config.json") as f:
        config = json.load(f)

    with sync_playwright() as p:

        browser = getattr(p, config["browser"]).launch(
            headless=config["headless"]
        )

        page = browser.new_page()

        page.goto(config["url"])

        yield page

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            capture(page, item.name)