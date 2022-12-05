import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, "
                          "ru, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def language_switch(request):
    language = request.config.getoption("language")
    match language:
        case 'ar':
            print(f'\nOpening page in arabian')
            return 'ar'
        case 'ca':
            print(f'\nOpening page in catalan')
            return 'ca'
        case 'cs':
            print(f'\nOpening page in czech')
            return 'cs'
        case 'da':
            print(f'\nOpening page in danish')
            return 'da'
        case 'de':
            print(f'\nOpening page in deutsch')
            return 'de'
        case 'en-gb':
            print(f'\nOpening page in english(GB)')
            return 'en-gb'
        case 'el':
            print(f'\nOpening page in greek')
            return 'el'
        case 'es':
            print(f'\nOpening page in spanish')
            return 'es'
        case 'fi':
            print(f'\nOpening page in finnish')
            return 'fi'
        case 'fr':
            print(f'\nOpening page in french')
            return 'fr'
        case 'it':
            print(f'\nOpening page in italian')
            return 'it'
        case 'ko':
            print(f'\nOpening page in korean')
            return 'ko'
        case 'nl':
            print(f'\nOpening page in dutch')
            return 'nl'
        case 'pl':
            print(f'\nOpening page in polish')
            return 'pl'
        case 'pt':
            print(f'\nOpening page in portuguese')
            return 'pt'
        case 'pt-br':
            print(f'\nOpening page in portuguese-brazilian')
            return 'pt-br'
        case 'ro':
            print(f'\nOpening page in romanian')
            return 'ro'
        case 'ru':
            print(f'\nOpening page in russian')
            return 'ru'
        case 'sk':
            print(f'\nOpening page in slovenian')
            return 'sk'
        case 'uk':
            print(f'\nOpening page in ukranian')
            return 'uk'
        case 'zh-cn':
            print(f'\nOpening page in simplified chinese')
            return 'zh-cn'
        case _:
            raise pytest.UsageError("--language is incorrect")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    match browser_name:
        case "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome()
        case "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
