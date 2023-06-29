# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support.color import Color
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from time import sleep

# s = Service(GeckoDriverManager().install())

    #verifica um texto
    # def verify_text(self, element_path):
    #     self.wait(element_path)
    #     element_text = self.locate_element((element_path)).text
    #     assert element_text == 'Computador cadastrado com sucesso', f'Erro ao cadastrar a maquina'
        
    # #verifica a cor de um texto
    # def verify_text_color(self, element_path):
    #     self.wait(element_path)
    #     red_color = Color.from_string('#FF0000')
    #     text_color = Color.from_string(self.locate_element((element_path)).value_of_css_property('color'))
    #     assert text_color == red_color, f'Alert message: cor do elemento nao é vermelha'
        
    # #deletar uma maquina
    # def deletar_maquina(self):
        # self.BIN_BTN_PATH = (By.ID,'humbertoTomeSeuId0')
        # self.CONFIRM_BTN_PATH = (By.ID,'confirm-btn') 
        
        # self.wait_to_click(self.BIN_BTN_PATH)
        # self.click_element(self.BIN_BTN_PATH)
        
        # self.wait_to_click(self.CONFIRM_BTN_PATH)
        # self.click_element(self.CONFIRM_BTN_PATH)
        
        
        


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

    def wait(self, element_path):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((element_path))
        )
        return bool(element)
    
    def wait_to_click(self, element_path):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((element_path))
        )
        return bool(element)
    
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
        
        self.wait_to_click(self.GOOGLE_BTN_PATH)
        self.click_element(self.GOOGLE_BTN_PATH)

        self.wait(self.EMAIL_BOX_PATH)
        self.write(self.EMAIL_BOX_PATH,'ana.maciel05@aluno.ifce.edu.br')
        self.click_element(self.NEXT_BTN01_PATH)
        self.write(self.PASSWORD_BTN_PATH,'230804_Le')
        self.click_element(self.NEXT_BTN02_PATH)
        
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
        

gep = GepPage()

gep.open_page()
sleep(2)
gep.login_gep_page()
sleep(3)
gep.adicionar_sala('laboratorio latim', 'latim', 'baia01', 'b01')
sleep(3)
gep.adicionar_maquina('987643', 'latim', 'baia01', 'PC1', 'computador 01 latim')
sleep(3)
gep.adicionar_sala('laboratorio 2', 'lasic2', 'baia01', 'b01')
sleep(3)
gep.adicionar_maquina('789012', 'lasic2', 'baia01', 'PC02', 'computador 01 lasic')
sleep(3)
gep.deletar_maquina()

