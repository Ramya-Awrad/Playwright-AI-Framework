class CartPage:

    def __init__(self, page):
        self.page = page

    def is_product_present(self):

        return self.page.locator(".inventory_item_name").inner_text()