from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.logger import get_logger

logger = get_logger()


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):

        logger.info("Entering Username")
        self.fill(LoginLocators.USERNAME, username)

        logger.info("Entering Password")
        self.fill(LoginLocators.PASSWORD, password)

        logger.info("Clicking Login Button")
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()