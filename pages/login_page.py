from locators.login_locators import LoginLocators


class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):

        self.page.fill(LoginLocators.USERNAME, username)

        self.page.fill(LoginLocators.PASSWORD, password)

        self.page.click(LoginLocators.LOGIN_BUTTON)