from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

import time

def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL_PROMO
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.assert_product_name()
    page.assert_basket_total()
