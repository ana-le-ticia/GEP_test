from pages.base_page import BasePage
from utils.projects_locators import ProjectLocators

class CrudProject(BasePage):
    def __init__(self, browser) -> None:
        self.locator = ProjectLocators()
        super().__init__(browser)
        
    def adicionar_projeto(self, name: str, sigla: str, status:str, start_date: str, close_date: str, coordenador: str, descricao: str, user: str, maquina: str):
        
        self.wait_to_click(self.locator.PROJETO_PATH)
        project = self.locate_element(self.locator.PROJETO_PATH)
        self.click_element(project)
        
        self.wait_to_click(self.locator.PROJECT_ADD_BTN_PATH)
        add_project_btn = self.locate_element(self.locator.PROJECT_ADD_BTN_PATH)
        self.click_element(add_project_btn)
        
        self.wait(self.locator.PROJECT_NAME_INPUT_PATH)
        project_name = self.locate_element(self.locator.PROJECT_NAME_INPUT_PATH)
        self.write(project_name, name)

        self.wait(self.locator.PROJECT_SIGLA_INPUT_PATH)
        project_sigla = self.locate_element(self.locator.PROJECT_SIGLA_INPUT_PATH)
        self.write(project_sigla, sigla)
        
        self.wait(self.locator.PROJECT_STATUS_INPUT_PATH)
        project_status = self.locate_element(self.locator.PROJECT_STATUS_INPUT_PATH)
        self.write(project_status, status)
        
        self.wait(self.locator.START_DATE_INPUT_PATH)
        start = self.locate_element(self.locator.START_DATE_INPUT_PATH)
        self.write(start, start_date)
        
        self.wait(self.locator.CLOSE_DATE_INPUT_PATH)
        close = self.locate_element(self.locator.CLOSE_DATE_INPUT_PATH)
        self.write(close, close_date)
        
        self.wait(self.locator.COORDENADOR_INPUT_PATH)
        coordinator = self.locate_element(self.locator.COORDENADOR_INPUT_PATH)
        self.write(coordinator, coordenador)
        
        self.wait(self.locator.DESCRIPTION_INPUT_PATH)
        description = self.locate_element(self.locator.DESCRIPTION_INPUT_PATH)
        self.write(description, descricao)
        
        self.wait_to_click(self.locator.ADD_MEMBER_BTN_PATH)
        add_member_btn = self.locate_element(self.locator.ADD_MEMBER_BTN_PATH)
        self.click_element(add_member_btn)
        
        self.wait(self.locator.USER_INPUT_PATH)
        user_input = self.locate_element(self.locator.USER_INPUT_PATH)
        self.write(user_input, user)
        
        self.wait(self.locator.MACHINE_INPUT_PATH)
        machine = self.locate_element(self.locator.MACHINE_INPUT_PATH)
        self.write(machine, maquina)
