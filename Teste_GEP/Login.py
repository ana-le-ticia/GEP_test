from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(GeckoDriverManager().install())

class SeleniumComands():

    def __init__(self) -> None:
        self.browser = webdriver.Firefox(service=s)

    def locate_element(self, locator):
        return self.browser.find_element(*locator)

    def write(self, locator, key: str):
        self.locate_element(locator).send_keys(key)

    def click_element(self, locator):
        self.locate_element(locator).click()
        
class GepPage(SeleniumComands):
    
    def __init__(self) -> None:
        self.browser = webdriver.Firefox(service=s)
        
    def open_page(self):
        self.url = 'http://localhost:3000'
        
        self.browser.get(self.url)
        self.browser.fullscreen_window()
        
    def login_gep_page(self):
        self.GOOGLE_BTN_PATH = (By.ID,'google-btn')
        self.EMAIL_BOX_PATH = (By.ID,'identifierId')
        self.NEXT_BTN01_PATH = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        self.PASSWORD_BTN_PATH = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        self.NEXT_BTN02_PATH = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        
        self.click_element(self.GOOGLE_BTN_PATH)
        sleep(2)
        self.write(self.EMAIL_BOX_PATH,'ana.maciel05@aluno.ifce.edu.br')
        sleep(2)
        self.click_element(self.NEXT_BTN01_PATH)
        sleep(2)
        self.write(self.PASSWORD_BTN_PATH,'230804_Le')
        sleep(2)
        self.click_element(self.NEXT_BTN02_PATH)
        sleep(3)
        
    #adicionar sala sem erros
    def adicionar_sala(self):
        self.SALA_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[2]')
        self.ADD_BTN = (By.ID,'Add')
        self.NOME_SALA_PATH = (By.ID,'name-room-textfield')
        self.SIGLA_PATH = (By.ID,'abbreviation-room-textfield')
        self.ADD_BAIA_PATH = (By.ID,'add-space-btn')
        self.ESPACO_PATH = (By.ID,'space-room-textfield-0')
        self.SIGLA_ESPACO_PATH = (By.ID,'abbreviation-room-textfield-0')
        self.SAVE_BTN = (By.ID,'save-bnt')
        
        self.click_element(self.SALA_PATH)
        sleep(2)
        self.click_element(self.ADD_BTN)
        sleep(2)
        self.write(self.SALA_PATH,'Laboratorio Latim')
        sleep(2)
        self.write(self.SIGLA_PATH,'LATIM')
        sleep(2)
        self.click_element(self.ADD_BAIA_PATH)
        sleep(2)
        self.write(self.ESPACO_PATH,'Baia01')
        sleep(2)
        self.write(self.SIGLA_ESPACO_PATH,'B01')
        sleep(2)
        self.click_element(self.SAVE_BTN)
        sleep(2)
        
    #adicionar maquina sem erros
    def adicionar_maquina(self):
        self.COMPUTADORES_PATH = (By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/a[3]')
        self.ADD_BTN = (By.ID,'Add')
        self.PATRIMONIO_PATH = (By.ID,'patrimony-textfield')
        self.SALA_INPUT_PATH = (By.ID,'room-name-textfield')
        self.ESPACO_INPUT_PATH = (By.ID,'space-name-textfield')
        self.MAQUINA_INPUT_PATH = (By.ID,'abbreviation-textfield')
        self.SAVE_BTN = (By.ID,'save-bnt')
        
        self.click_element(self.COMPUTADORES_PATH)
        sleep(2)
        self.click_element(self.ADD_BTN)
        sleep(2)
        self.write(self.PATRIMONIO_PATH,'123456')
        sleep(2)
        self.write(self.SALA_INPUT_PATH,'lasic')
        sleep(2)
        self.write(self.ESPACO_INPUT_PATH,'Baia01')
        sleep(2)
        self.write(self.MAQUINA_INPUT_PATH,'PC')
        sleep(2)
        self.click_element(self.SAVE_BTN)
        sleep(2)
            
    #verificação ao tentar adicionar sala 
        

gep = GepPage()

gep.open_page()
sleep(2)
gep.login_gep_page()
sleep(3)
gep.adicionar_sala()
sleep(2)
gep.adicionar_maquina()
sleep(4)