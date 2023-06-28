from selenium.webdriver.common.by import By

class RoomsLocators():
    SALA_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[2]')
    ADD_BTN = (By.ID,'Add')
    NOME_SALA_PATH = (By.ID,'name-room-textfield')
    SIGLA_PATH = (By.ID,'abbreviation-room-textfield')
    ADD_BAIA_PATH = (By.ID,'add-space-btn')
    ESPACO_PATH = (By.ID,'space-room-textfield-0')
    SIGLA_ESPACO_PATH = (By.ID,'abbreviation-room-textfield-0')
    SAVE_BTN = (By.ID,'save-bnt')