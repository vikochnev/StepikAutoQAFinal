from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_PAGE_URL_PROMO = \
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_NAME = "The shellcoder's handbook"
    PRODUCT_PRICE = "£9.99"
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
