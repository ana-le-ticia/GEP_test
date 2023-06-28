from selenium.webdriver.common.by import By

class ProjectLocators():
    PROJECT_BTN = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[4]')
    PROJECT_ADD_BTN = (By.ID,'Add')
    PROJECT_NAME = (By.ID,'project-name')
    PROJECT_SIGLA = (By.ID,'project-abbreviation')
    PROJECT_STATUS = (By.ID,'project-status')
    START_DATE = (By.ID,'start-date-field')
    CLOSE_DATE = (By.ID,'end-date-field')
    COORDENADOR = (By.ID,'coordinator-autocomplete')
    DESCRICAO = (By.ID,'description')
    
    ADD_MEMBER_BTN = (By.ID,'add-member-button')
    USER = (By.ID,'name-user-autocomplete-0')
    MAQUINA = (By.ID,'machine-autocomplete-0')
    TURNO = (By.ID,'turn-autocomplete-0')