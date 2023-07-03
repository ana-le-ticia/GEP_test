from pages.cruds.crud_rooms import CrudRooms
from test_base import TestBase
from utils.verify_text_locators import VerifyText

class DeleteRoom(TestBase):
    def test_delete_room(self):
        self.locator = VerifyText()
        self.delete_room = CrudRooms(self.browser)
        
        
        self.delete_room.deletar_sala()
        print('ok')
        #self.delete_room.verify_text('Sala deletada com sucesso',self.locator.SALA_DELETADA)
        
        #self.assertIn('inventory', self.browser.current_window_handle)