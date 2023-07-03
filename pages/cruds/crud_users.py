from pages.base_page import BasePage
from utils.users_locators import UsersLocators

class CrudUsers(BasePage):
    def __init__(self, browser) -> None:
        self.locator = UsersLocators()
        super().__init__(browser)
        
    def adicionar_usuario(self, name: str, email: str, matricula: str, telefone: str, user_type: str):
        
        self.wait_to_click(self.locator.USERS_PATH)
        add_user_btn = self.locate_element(self.locator.USERS_PATH)
        self.click_element(add_user_btn)
        
        self.wait_to_click(self.locator.NAME_BOX_PATH)
        user_name = self.locate_element(self.locator.NAME_BOX_PATH)
        self.write(user_name, name)
        
        self.wait_to_click(self.locator.EMAIL_BOX_PATH)
        user_email = self.locate_element(self.locator.EMAIL_BOX_PATH)
        self.write(user_email, email)
        
        self.wait_to_click(self.locator.REGISTRATION_BOX_PATH)
        user_matricula = self.locate_element(self.locator.REGISTRATION_BOX_PATH)
        self.write(user_matricula, matricula)
        
        self.wait_to_click(self.locator.PHONE_BOX_PATH)
        user_telefone = self.locate_element(self.locator.PHONE_BOX_PATH)
        self.write(user_telefone, telefone)
        
        self.wait_to_click(self.locator.USER_TYPE_PATH)
        user_type = self.locate_element(self.locator.USER_TYPE_PATH)
        self.write(user_type, user_type)
        
        self.wait_to_click(self.locator.USER_LEVEL_BOX_PATH)
        user_level_btn = self.locate_element(self.locator.USER_LEVEL_BOX_PATH)
        self.click_element(user_level_btn)
        
        self.wait_to_click(self.locator.ACCESS_LEVEL_USER_BTN_PATH)
        user_access_level = self.locate_element(self.locator.ACCESS_LEVEL_USER_BTN_PATH)
        self.click_element(user_access_level)
        
        self.wait_to_click(self.locator.SAVE_BTN_PATH)
        save_btn = self.locate_element(self.locator.SAVE_BTN_PATH)
        self.click_element(save_btn)
        
        