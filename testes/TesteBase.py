from pages.Login import Login
import unittest
from utils.imports import *

s = Service(GeckoDriverManager().install())

class TesteBase(unittest.TestCase):
    
    def setUp(self):
        self.webdriver = webdriver.Firefox(service=s)
        self.wait = WebDriverWait(self.webdriver, 10)
        self.login = Login()
        self.login.open_page()
        self.login.login_gep_page()
        
    def tearDown(self):
        self.login.browser.quit()
