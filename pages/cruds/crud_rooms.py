from utils.imports import *
from ..BasePage import BasePage
from utils.room_locators import RoomsLocators

class Rooms(BasePage):
    
    def __init__(self) -> None:
        super().__init__()
        self.locator = RoomsLocators()
    
    def adicionar_sala(self, nome_sala: str, sigla: str, baia: str, sigla_baia: str):
        
        self.wait_to_click(self.locator.SALA_PATH)
        self.click_element(self.locator.SALA_PATH)
        
        self.wait_to_click(self.locator.ADD_BTN)
        self.click_element(self.locator.ADD_BTN)

        self.wait(self.locator.SALA_PATH)
        self.write(self.locator.SALA_PATH, nome_sala)

        self.wait(self.locator.SIGLA_PATH)
        self.write(self.locator.SIGLA_PATH, sigla)
        
        self.wait_to_click(self.locator.ADD_BAIA_PATH)
        self.click_element(self.locator.ADD_BAIA_PATH)

        self.wait(self.locator.ESPACO_PATH)
        self.write(self.locator.ESPACO_PATH, baia)

        self.wait(self.locator.SIGLA_ESPACO_PATH)
        self.write(self.locator.SIGLA_ESPACO_PATH, sigla_baia)

        self.wait_to_click(self.locator.SAVE_BTN)
        self.click_element(self.locator.SAVE_BTN)