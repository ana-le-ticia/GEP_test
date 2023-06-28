from utils.imports import *

class BasePage():
    
    def init(self, driver) -> None:
        self.browser = driver
        
    def init(self, driver) -> None:
        self.browser = driver

    def locate_element(self, locator):
        return self.browser.find_element(*locator)

    def write(self, locator, key: str):
        self.locate_element(locator).send_keys(key)

    def click_element(self, locator):
        self.locate_element(locator).click()
        
    #explicit wait
    def wait(self, element_path):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((element_path))
        )
        return bool(element)
    
    def wait_to_click(self, element_path):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((element_path))
        )
        return bool(element)
        