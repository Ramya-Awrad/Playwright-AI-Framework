import json

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_product_to_cart(page):

    with open("testdata/login_data.json") as f:
        data = json.load(f)

    login = LoginPage(page)

    login.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory = InventoryPage(page)

    inventory.add_backpack_to_cart()

    inventory.open_cart()

    cart = CartPage(page)

    assert cart.is_product_present() == "Sauce Labs Backpack"