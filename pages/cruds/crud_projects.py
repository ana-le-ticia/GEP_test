from utils.imports import *
from ..BasePage import BasePage
from utils.project_locators import ProjectLocators

class Projects(BasePage):
    def __init__(self) -> None:
        super().__init__()
        self.locator = ProjectLocators()
        
    def adicionar_projeto(self, nome_proj: str, sigla_proj: str, status: str, data_inicio: str, data_fim: str, coordenador: str, descricao: str, usuario: str, maquina: str, turno: str):
        
        self.wait_to_click(self.locator.PROJECT_BTN)
        self.click_element(self.locator.PROJECT_BTN)
        
        self.wait_to_click(self.locator.PROJECT_ADD_BTN)
        self.click_element(self.locator.PROJECT_ADD_BTN)
        
        self.wait(self.locator.PROJECT_NAME)
        self.write(self.locator.PROJECT_NAME, nome_proj)
        
        self.wait(self.locator.PROJECT_SIGLA)
        self.write(self.locator.PROJECT_SIGLA, sigla_proj)
        
        self.wait(self.locator.PROJECT_STATUS)
        self.write(self.locator.PROJECT_STATUS, status)
        
        self.wait(self.locator.START_DATE)
        self.write(self.locator.START_DATE, data_inicio)
        
        self.wait(self.locator.CLOSE_DATE)
        self.write(self.locator.CLOSE_DATE, data_fim)
        
        self.wait(self.locator.COORDENADOR)
        self.write(self.locator.COORDENADOR, coordenador)
        
        self.wait(self.locator.DESCRICAO)
        self.write(self.locator.DESCRICAO, descricao)
        
        self.wait_to_click(self.locator.ADD_MEMBER_BTN)
        self.click_element(self.locator.ADD_MEMBER_BTN)
        
        self.wait(self.locator.USER)
        self.write(self.locator.USER, usuario)
        
        self.wait(self.locator.MAQUINA)
        self.write(self.locator.MAQUINA, maquina)
        
        self.wait(self.locator.TURNO)
        self.write(self.locator.MAQUINA, turno)
        