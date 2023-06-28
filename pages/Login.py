from BasePage import BasePage
from utils.imports import *

class Login(BasePage):
    def __init__(self, driver) -> None:
        super().__init__()
        self.browser = driver
        self.ulr = 'http://localhost:3000'
    
    def open_page(self):
        self.browser.get(self.url)
        self.browser.fullscreen_window()
        
    def login_gep_page(self):
        self.GOOGLE_BTN_PATH = (By.ID,'google-btn')
        self.EMAIL_BOX_PATH = (By.ID,'identifierId')
        self.PASSWORD_BOX_PATH = (By.XPATH,'//*[@type="password"]')
        
        
        self.wait(self.GOOGLE_BTN_PATH)
        self.click_element(self.GOOGLE_BTN_PATH)
        
        self.wait(self.EMAIL_BOX_PATH)
        self.locate_element((self.EMAIL_BOX_PATH)).send_keys('ana.maciel05@aluno.ifce.edu.br', Keys.ENTER)

        self.wait(self.PASSWORD_BOX_PATH)
        self.locate_element((self.PASSWORD_BOX_PATH)).send_keys('230804_Le', Keys.ENTER)
    

    
    