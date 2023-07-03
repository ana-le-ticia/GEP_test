from pages.cruds.crud_rooms import CrudRooms
from test_base import TestBase
#from utils.verify_text_locators import VerifyText

class AddRoom(TestBase):
    def test_add_room(self):
        #self.locator = VerifyText()
        self.add_room = CrudRooms(self.browser)
        
        self.add_room.adicionar_sala('laboratorio de desenvolvimento', 'lasic', 'laboratorio de desenvolvimento de software e pesquisa', 'Baia01', 'B01', 'primeira baia')
        print('ok')
        #self.add_room.verify_text('Sala cadastrada com sucesso',self.locator.SALA_CRIADA)