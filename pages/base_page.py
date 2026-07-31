class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def wait(self, milliseconds=1000):
        self.page.wait_for_timeout(milliseconds)