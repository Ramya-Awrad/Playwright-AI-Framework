from locators.login_locators import LoginLocators
from utils.logger import get_logger

logger = get_logger()


class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        logger.info("Entering Username")

        self.page.fill(LoginLocators.USERNAME, username)

        logger.info("Entering Password")

        self.page.fill(LoginLocators.PASSWORD, password)

        logger.info("Clicking Login Button")

        self.page.click(LoginLocators.LOGIN_BUTTON)