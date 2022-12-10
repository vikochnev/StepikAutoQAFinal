from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def click_on_element(self, *element):
        """Clicks on located element"""
        self.browser.find_element(*element).click()

    def get_element_text(self, *element):
        """Gets text from located element"""
        text = self.browser.find_element(*element).text
        return text

    def get_language(self):
        """Gets language option from page"""
        lang = self.browser.find_element(*BasePageLocators.LANGUAGE_LOCATOR).get_attribute("lang")
        return lang

    def go_to_login_page(self):
        """Opens Login/Register page by clicking on "Log in or register "button"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        """Opens Basket page by clicking on "View basket" button"""
        basket_button = BasePageLocators.BASKET_PAGE_LOCATOR
        lang = self.get_language()
        link = self.browser.find_element(basket_button[0], basket_button[1][0] + lang + basket_button[1][1])
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        """Checks if element disappeared"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        """Checks if element is present"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Checks if element is not present"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

    def open(self):
        """Opens web page"""
        self.browser.get(self.url)

        return False

    def send_keys_to_element(self, *element, keys):
        """Inputs into located field"""
        self.browser.find_element(*element).send_keys(keys)

    def assert_authorized_user(self):
        """Checks if user icon is present"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def assert_login_link(self):
        """Checks if login link is present"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
