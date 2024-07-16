import pytest
import logging
from ui_testing.page.base_page import BasePage
from ui_testing.page.products_page import ProductsPage
from ui_testing.page.checkout_page import CheckoutProcess
logger = logging.getLogger(__name__)


@pytest.mark.ui
def test_pets_website(page):
    """end-to-end test to validate all actions from logging in, filtering, adding to cart and checkout"""
    base_page = BasePage(page)
    products_page = ProductsPage(page)
    checkout_process = CheckoutProcess(page)

    logger.info('LOGIN')
    base_page.login_to_saucedemo()

    logger.info('FILTER PRODUCTS FROM LOW TO HIGH')
    products_page.filter_products_lo_hi()

    logger.info('ADD FIRST 2 ITEMS TO CART')
    products_page.add_first_2_items()

    logger.info('GO TO CART')
    products_page.go_to_cart()

    logger.info('CHECKOUT')
    checkout_process.checkout()

    logger.info('FILL SHIPPING FORM')
    checkout_process.fill_form(first_name='Kavita', last_name='Dan', postal_code='2155')

    logger.info('CONTINUE AND FINISH CHECKOUT')
    checkout_process.complete_checkout()
