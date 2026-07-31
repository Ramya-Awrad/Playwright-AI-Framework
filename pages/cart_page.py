from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def is_product_present(self):
        return self.get_text(CartLocators.PRODUCT_NAME)