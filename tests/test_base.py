from pages.login_page import LoginPage
from selenium import webdriver
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        
        self.login = LoginPage(self.browser)
        
        self.login.open_page()
        self.login.login_gep()
        
        
    def tearDown(self):
        self.browser.close()    