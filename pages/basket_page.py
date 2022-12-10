from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_amount_of_items_in_basket(self):
        number_of_items = self.browser.find_elements(*BasketPageLocators.ITEMS_IN_BASKET)
        return len(number_of_items)

    def assert_is_basket_empty(self):
        assert self.check_amount_of_items_in_basket() == 0, f'Basket is not empty when should be'

    def assert_basket_empty_message(self):
        lang = self.get_language()
        message_should_be = BasketPageLocators.BASKET_IS_EMPTY_LANGUAGES[lang]
        message =self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR).text
        assert message_should_be in message, \
            f'Basket is not empty message is invalid: {message_should_be} instead of: {message}:'
