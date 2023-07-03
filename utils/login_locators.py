from selenium.webdriver.common.by import By

class LoginLocators():
    GOOGLE_BTN_PATH = (By.ID,'google-btn')
    EMAIL_BOX_PATH = (By.ID,'identifierId')
    PASSWORD_BOX_PATH = (By.XPATH,'//*[@type="password"]')