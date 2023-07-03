from selenium.webdriver.common.by import By

class ProjectLocators():
    PROJETO_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[4]')
    PROJECT_ADD_BTN_PATH = (By.ID,'Add')
    PROJECT_NAME_INPUT_PATH = (By.ID,'project-name')
    PROJECT_SIGLA_INPUT_PATH = (By.ID,'project-abbreviation')
    PROJECT_STATUS_INPUT_PATH = (By.ID,'project-status')
    START_DATE_INPUT_PATH = (By.ID,'start-date-field')
    CLOSE_DATE_INPUT_PATH = (By.ID,'end-date-field')
    COORDENADOR_INPUT_PATH = (By.ID,'coordinator-autocomplete')
    DESCRIPTION_INPUT_PATH = (By.ID,'description')
    
    ADD_MEMBER_BTN_PATH = (By.ID,'add-member-button')
    USER_INPUT_PATH = (By.ID,'name-user-autocomplete-0')
    MACHINE_INPUT_PATH = (By.ID,'machine-autocomplete-0')
    
    PROJECT_SAVE_BTN_PATH = (By.ID,'projects-submit')
    