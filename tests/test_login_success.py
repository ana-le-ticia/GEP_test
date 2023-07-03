from test_base import TestBase
from time import sleep

class LoginSuccess(TestBase):
    def test_login_success(self):
        
        sleep(5)
        current_url = self.browser.current_url
        self.assertIn('localhost:3000', current_url, "Not on the right webpage")
        print(current_url)
        
        
        