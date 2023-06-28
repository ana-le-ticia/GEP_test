from selenium.webdriver.common.by import By

class MachineLocators():
    COMPUTADORES_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[3]')
    ADD_BTN = (By.ID,'Add')
    PATRIMONIO_PATH = (By.ID,'patrimony-textfield')
    SALA_INPUT_PATH = (By.ID,'room-name-textfield')
    ESPACO_INPUT_PATH = (By.ID,'space-name-textfield')
    MAQUINA_INPUT_PATH = (By.ID,'abbreviation-textfield')
    DESCRIPTION_INPUT_PATH = (By.ID,'description-textfield')
    SAVE_BTN = (By.ID,'save-bnt')