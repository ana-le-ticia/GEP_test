from imports import *

class SeleniumComands():

    def __init__(self) -> None:
        self.browser = webdriver.Firefox(service=s)

    def find_el(self, locator):
        return self.browser.find_element(*locator)

    def write_key(self, locator, key: str):
        self.find_el(locator).send_keys(key)

    def click_element(self, locator):
        self.find_el(locator).click()