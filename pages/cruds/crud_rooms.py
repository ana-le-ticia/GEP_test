from pages.base_page import BasePage
from utils.rooms_locators import RoomsLocators

class CrudRooms(BasePage):
    def __init__(self, browser) -> None:
        self.locator = RoomsLocators()
        super().__init__(browser)
    
    def adicionar_sala(self, nome_sala: str, sigla: str, descricao: str, baia: str, sigla_baia: str, descricao_baia: str):
        
        self.wait_to_click(self.locator.SALA_PATH)
        sala = self.locate_element(self.locator.SALA_PATH)
        self.click_element(sala)
        
        self.wait_to_click(self.locator.ADD_BTN)
        add_sala_btn = self.locate_element(self.locator.ADD_BTN)
        self.click_element(add_sala_btn)

        self.wait(self.locator.NOME_SALA_PATH)
        room_name = self.locate_element(self.locator.NOME_SALA_PATH)
        self.write(room_name, nome_sala)

        self.wait(self.locator.SIGLA_PATH)
        room_sigla = self.locate_element(self.locator.SIGLA_PATH)
        self.write(room_sigla, sigla)
        
        self.wait(self.locator.DESCRIPTION_PATH)
        description = self.locate_element(self.locator.DESCRIPTION_PATH)
        self.write(description, descricao)
        
        self.wait_to_click(self.locator.ADD_BAIA_PATH)
        add_baia_btn = self.locate_element(self.locator.ADD_BAIA_PATH)
        self.click_element(add_baia_btn)

        self.wait(self.locator.ESPACO_PATH)
        space = self.locate_element(self.locator.ESPACO_PATH)
        self.write(space, baia)

        self.wait(self.locator.SIGLA_ESPACO_PATH)
        space_sigla = self.locate_element(self.locator.SIGLA_ESPACO_PATH)
        self.write(space_sigla, sigla_baia)
        
        self.wait(self.locator.BAIA_DESCRIPTION)
        baia_description = self.locate_element(self.locator.BAIA_DESCRIPTION)
        self.write(baia_description, descricao_baia)

        self.wait_to_click(self.locator.SAVE_BTN)
        save_btn = self.locate_element(self.locator.SAVE_BTN)
        self.click_element(save_btn)
        
    def deletar_sala(self):
        
        self.wait_to_click(self.locator.SALA_PATH)
        sala = self.locate_element(self.locator.SALA_PATH)
        self.click_element(sala)
        
        self.wait_to_click(self.locator.DELETE_BTN)
        delete_btn = self.locate_element(self.locator.DELETE_BTN)
        self.click_element(delete_btn)
        
        self.wait_to_click(self.locator.CONFIRM_BTN)
        confirm_btn = self.locate_element(self.locator.CONFIRM_BTN)
        self.click_element(confirm_btn)