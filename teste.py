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
        
        
        
# gep = GepPage()

# gep.open_page()
# sleep(2)
# gep.login_gep_page()
# sleep(3)
# gep.adicionar_sala('laboratorio latim', 'latim', 'baia01', 'b01')
# sleep(3)
# gep.adicionar_maquina('987643', 'latim', 'baia01', 'PC1', 'computador 01 latim')
# sleep(3)
# gep.adicionar_sala('laboratorio 2', 'lasic2', 'baia01', 'b01')
# sleep(3)
# gep.adicionar_maquina('789012', 'lasic2', 'baia01', 'PC02', 'computador 01 lasic')
# sleep(3)
# gep.deletar_maquina()
