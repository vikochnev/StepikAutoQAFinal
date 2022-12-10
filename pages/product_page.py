import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def assert_product_name(self):
        product_name_should_be = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_PRODUCT)
        assert product_name == product_name_should_be, \
            f"Product in basket: {product_name}, should be: {product_name_should_be}"

    def assert_basket_total(self):
        product_price_should_be = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        total = self.get_element_text(*ProductPageLocators.BASKET_TOTAL)
        basket_amount = total.split()
        assert basket_amount[2] == product_price_should_be, \
            f"Basket total: {basket_amount[2]} should be: {product_price_should_be}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
