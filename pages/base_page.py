from abc import ABC
from utils.imports import *

class BasePage(ABC):
    def __init__(self, browser) -> None:
        self.browser = browser
        self.url = 'http://localhost:3000'
        
    def open_page(self):
        self.browser.get(self.url)
    
    def locate_element(self, locator):
        return self.browser.find_element(*locator)
         
    def write(self, element, key: str):
        element.send_keys(key)
        
    def write_to_enter(self, element, key: str):
        element.send_keys(key, Keys.ENTER)

    def click_element(self, element):
        element.click()
        
    def wait(self, element_path):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((element_path))
        )
        return bool(element)
    
    def wait_to_click(self, element_path):
        element = WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable((element_path))
        )
        return bool(element)
    
    def verify_text(self, text: str, element_path):
        self.wait(element_path)
        element_text = self.locate_element((element_path)).text
        assert element_text == text, f'Erro'
        