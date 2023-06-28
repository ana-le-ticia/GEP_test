from selenium.webdriver.common.by import By

class UsersLocators():
    USERS_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[5]')
    ADD_BTN_PATH = (By.XPATH,'Add')
    NAME_INPUT_PATH = (By.ID,'user-name-textfield')
    EMAIL_INPUT_PATH = (By.ID,'user-email-textfield')
    MATRICULA_INPUT_PATH = (By.ID,'user-registration_number-textfield')
    PHONE_INPUT_PATH = (By.ID,'user-phone-textfield')
    USER_TYPE_INPUT_PATH = (By.ID,'user-user_type-autocomplete')
    ACCESS_LEVEL_BTN_PATH = (By.XPATH,'//*[@id="checkbox-user-login"]/button')
    SELECT_LEVEL_BOX_PATH = (By.XPATH,'//*[@id="level_acess_user_autocomplete"]/select')
    SAVE_BTN_PATH = (By.ID,'save-bnt')