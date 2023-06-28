from utils.imports import *
from ..BasePage import BasePage
from utils.machine_locators import MachineLocators

class CrudMachines(BasePage):
    
    def __init__(self) -> None:
        super().__init__()
        self.locator = MachineLocators()
    
    def adicionar_maquina(self, patrimonio: str, sigla_sala: str, baia: str, maquina: str, descricao: str):
        
        self.wait_to_click(self.locator.COMPUTADORES_PATH)
        self.click_element(self.locator.COMPUTADORES_PATH)

        self.wait_to_click(self.locator.ADD_BTN)
        self.click_element(self.locator.ADD_BTN)

        self.wait(self.locator.PATRIMONIO_PATH)
        self.write(self.locator.PATRIMONIO_PATH, patrimonio)

        self.wait(self.locator.SALA_INPUT_PATH)
        self.write(self.locator.SALA_INPUT_PATH, sigla_sala)

        self.wait(self.locator.ESPACO_INPUT_PATH)
        self.write(self.locator.ESPACO_INPUT_PATH, baia)

        self.wait(self.MAQUINA_INPUT_PATH)
        self.write(self.MAQUINA_INPUT_PATH, maquina)
        
        self.wait(self.DESCRIPTION_INPUT_PATH)
        self.write(self.DESCRIPTION_INPUT_PATH, descricao)

        self.wait_to_click(self.SAVE_BTN)
        self.click_element(self.SAVE_BTN)