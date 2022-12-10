from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_amount_of_items_in_basket(self):
        """Checks how many items are currently in basket"""
        number_of_items = self.browser.find_elements(*BasketPageLocators.ITEMS_IN_BASKET)
        return len(number_of_items)

    def assert_is_basket_empty(self):
        """Checks if amount of items in basket is currently 0"""
        assert not self.check_amount_of_items_in_basket(), f'Basket is not empty when should be'

    def assert_basket_empty_message(self):
        """Checks if "Basket is empty message" is present, should work with multiple languages"""
        lang = self.get_language()
        message_should_be = BasketPageLocators.BASKET_IS_EMPTY_LANGUAGES[lang]
        message = self.get_element_text(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR)
        assert message_should_be in message, \
            f'Basket is not empty message is invalid: {message_should_be} instead of: {message}:'
