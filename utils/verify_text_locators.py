from selenium.webdriver.common.by import By

class VerifyText():
    SIGLA_CAMPO_OBRIGATORIO = (By.XPATH,'/html/body/div[3]/div/div[3]/form/div/div[1]/div[2]/div[2]/span')
    SALA_CRIADA = (By.XPATH,'//*[@id="11"]/div[1]/div[2]')
    SALA_DELETADA = (By.XPATH,'//*[@id="15"]')