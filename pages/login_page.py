from pages.base_page import BasePage
from utils.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, browser) -> None:
        self.locator = LoginLocators()
        super().__init__(browser)
        
    def login_gep(self):
        
        self.wait(self.locator.GOOGLE_BTN_PATH)
        google_btn = self.locate_element(self.locator.GOOGLE_BTN_PATH)
        self.click_element(google_btn)
        
        self.wait(self.locator.EMAIL_BOX_PATH)
        email_box = self.locate_element(self.locator.EMAIL_BOX_PATH)
        self.write_to_enter(email_box, 'ana.maciel05@aluno.ifce.edu.br')
        
        self.wait(self.locator.PASSWORD_BOX_PATH)
        password_box = self.locate_element(self.locator.PASSWORD_BOX_PATH)
        self.write_to_enter(password_box, '230804_Le')
                        
        
        
