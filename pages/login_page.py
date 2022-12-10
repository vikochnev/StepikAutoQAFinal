import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    @staticmethod
    def generate_email():
        """Generates email"""
        email = str(time.time()) + "@fakemail.org"
        return email

    @staticmethod
    def generate_password():
        """Generates password(not implemented properly yet)"""
        password = "QWEAasd1234151123"  # add proper generator when required
        return password

    def register_new_user(self, email, password):
        """Fills all corresponding fields and clicks on Submit button"""
        self.send_keys_to_element(*LoginPageLocators.REGISTER_EMAIL, keys=email)
        self.send_keys_to_element(*LoginPageLocators.REGISTER_PASSWORD, keys=password)
        self.send_keys_to_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM, keys=password)
        self.click_on_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)

    def assert_login_page(self):
        """Checks if current window is Login/Registration web page"""
        self.assert_login_url()
        self.assert_login_form()
        self.assert_register_form()

    def assert_login_url(self):
        """Checks if there is "login" substring in page url"""
        assert "login" in self.browser.current_url, "Current URL isn't login page URL "

    def assert_login_form(self):
        """Checks if login form is present"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def assert_register_form(self):
        """Checks if registration form is present"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"
