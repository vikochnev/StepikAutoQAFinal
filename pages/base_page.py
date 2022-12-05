class BasePage:
    """Base Page Object class for inheritance"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
