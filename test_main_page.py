import pytest

from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.assert_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.assert_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_URL
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.assert_is_basket_empty()
    page.assert_basket_empty_message()
