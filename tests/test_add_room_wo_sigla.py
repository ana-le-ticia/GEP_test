from pages.cruds.crud_rooms import CrudRooms
from test_base import TestBase
from pages.base_page import BasePage
from utils.verify_text_locators import VerifyText

class AddRoomWithOutSigla(TestBase):
    def test_add_room(self):
        self.locator = VerifyText()
        self.add_room = CrudRooms(self.browser)
        self.base = BasePage(self.browser)
        
        self.add_room.adicionar_sala('laboratorio de desenvolvimento', '', 'laboratorio de desenvolvimento de software e pesquisa', 'Baia01', 'B01', 'primeira baia')
        self.base.verify_text('Campo obrigatório',self.locator.SIGLA_CAMPO_OBRIGATORIO)
        print('ok')