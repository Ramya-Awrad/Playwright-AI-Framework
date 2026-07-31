from pages.base_page import BasePage
from locators.inventory_locators import InventoryLocators


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def add_backpack_to_cart(self):
        self.click(InventoryLocators.BACKPACK)

    def open_cart(self):
        self.click(InventoryLocators.CART)