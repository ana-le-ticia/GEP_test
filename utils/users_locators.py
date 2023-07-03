from selenium.webdriver.common.by import By

class UsersLocators():
    USERS_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[5]')
    ADD_BTN_PATH = (By.ID,'Add')
    NAME_BOX_PATH = (By.ID,'user-name-textfield')
    EMAIL_BOX_PATH = (By.ID,'user-email-textfield')
    REGISTRATION_BOX_PATH = (By.ID,'user-registration_number-textfield')
    PHONE_BOX_PATH = (By.ID,'user-phone-textfield')
    USER_TYPE_PATH = (By.ID,'user-user_type-autocomplete')
    ACCESS_LEVEL_USER_BTN_PATH = (By.XPATH,'//*[@id="checkbox-user-login"]/button')
    USER_LEVEL_BOX_PATH = (By.ID,'user_level')
    SAVE_BTN_PATH = (By.ID,'save-bnt')