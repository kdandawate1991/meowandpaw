
from ui_testing.page.base_page import BasePage


class ProductsPage(BasePage):
    LO_HI_FILTER = '[data-test="product-sort-container"]'
    INVENTORY_LIST = '[data-test="inventory-item"]'
    ADD_TO_CART_BUTTON = '[data-test^="add-to-cart-"]'
    CHECK_CART_ITEMS = '[data-test^="remove-"]'
    CART = '[data-test="shopping-cart-link"]'

    def __init__(self, page):
        super().__init__(page)

    def filter_products_lo_hi(self):
        self.page.select_option(self.LO_HI_FILTER, 'lohi')

    def add_first_2_items(self):
        items = self.page.query_selector_all(self.INVENTORY_LIST)[:2]
        for item in items:
            add_to_cart_button = item.query_selector(self.ADD_TO_CART_BUTTON)
            if add_to_cart_button:
                add_to_cart_button.click()
        assert len(self.page.query_selector_all(self.CHECK_CART_ITEMS)) == 2

    def go_to_cart(self):
        self.page.click(self.CART)
