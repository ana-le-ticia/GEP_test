from utils.imports import *
from ..BasePage import BasePage
from utils.users_locators import UsersLocators

class Users(BasePage):

    def __init__(self) -> None:
        super().__init__()
        self.locator = UsersLocators()

    def adicionar_user(self, nome: str, email: str, matricula: str, telefone: str, tipo_usuario: str, nivel_acesso: str):
        
        self.wait_to_click(self.locator.USERS_PATH)
        self.click_element(self.locator.USERS_PATH)
        
        self.wait(self.locator.NAME_INPUT_PATH)
        self.write(self.locator.NAME_INPUT_PATH, nome)

        self.wait(self.locator.EMAIL_INPUT_PATH)
        self.write(self.locator.EMAIL_INPUT_PATH, email)

        self.wait(self.locator.MATRICULA_INPUT_PATH)
        self.write(self.locator.MATRICULA_INPUT_PATH, matricula)
        
        self.wait(self.locator.PHONE_INPUT_PATH)
        self.write(self.locator.PHONE_INPUT_PATH, telefone)

        self.wait(self.locator.USER_TYPE_INPUT_PATH)
        self.write(self.locator.USER_TYPE_INPUT_PATH, user)

        self.wait_to_click(self.locator.ACCESS_LEVEL_BTN_PATH)
        self.click_element(self.locator.ACCESS_LEVEL_BTN_PATH)

        self.wait_to_click(self.locator.ACCESS_LEVEL_BTN_PATH)
        self.click_element(self.locator.ACCESS_LEVEL_BTN_PATH)