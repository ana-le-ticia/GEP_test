from pages.base_page import BasePage
from utils.machines_locators import MachineLocators

class CrudMachines(BasePage):
    def __init__(self, browser) -> None:
        self.locator = MachineLocators()
        super().__init__(browser)
        
    def adicionar_maquina(self, patrimonio: str, sigla_sala: str, baia: str, maquina_str: str, descricao: str):
        
        self.wait_to_click(self.locator.COMPUTADORES_PATH)
        computadores = self.locate_element(self.locator.COMPUTADORES_PATH)
        self.click_element(computadores)

        self.wait_to_click(self.locator.ADD_BTN)
        add_maquina_btn = self.locate_element(self.locator.ADD_BTN)
        self.click_element(add_maquina_btn)

        self.wait(self.locator.PATRIMONIO_PATH)
        patrimony = self.locate_element(self.locator.PATRIMONIO_PATH)
        self.write(patrimony, patrimonio)

        self.wait(self.locator.SALA_INPUT_PATH)
        room = self.locate_element(self.locator.SALA_INPUT_PATH)
        self.write(room, sigla_sala)

        self.wait(self.locator.ESPACO_INPUT_PATH)
        space = self.locate_element(self.locator.ESPACO_INPUT_PATH)
        self.write(space, baia)
        
        self.wait(self.locator.MAQUINA_INPUT_PATH)
        machine = self.locate_element(self.locator.MAQUINA_INPUT_PATH)
        self.write(machine, maquina_str)
        
        self.wait(self.locator.DESCRIPTION_INPUT_PATH)
        description = self.locate_element(self.locator.DESCRIPTION_INPUT_PATH)
        self.write(description, descricao)
        
        self.wait_to_click(self.locator.SAVE_BTN)
        save_btn = self.locate_element(self.locator.SAVE_BTN)
        self.click_element(save_btn)
        
    def deletar_maquina(self):
        
        self.wait_to_click(self.locator.COMPUTADORES_PATH)
        computadores = self.locate_element(self.locator.COMPUTADORES_PATH)
        self.click_element(computadores)
        
        self.wait_to_click(self.locator.DELETE_BTN_PATH)
        delete_btn = self.locate_element(self.locator.DELETE_BTN_PATH)
        self.click_element(delete_btn)
        
        self.wait_to_click(self.locator.CONFIRM_BTN)
        confirm_btn = self.locate_element(self.locator.CONFIRM_BTN)
        self.click_element(confirm_btn)