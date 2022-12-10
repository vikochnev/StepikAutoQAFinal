import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators, LoginPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.LOGIN_URL
        page = LoginPage(browser, link)
        email = page.generate_email()
        password = page.generate_password()
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_URL
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_basket_button()
        page.assert_product_name()
        page.assert_basket_total()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.skip(reason="Doesn't require testing atm")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/",
                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.assert_product_name()
    page.assert_basket_total()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.assert_is_basket_empty()
    page.assert_basket_empty_message()
