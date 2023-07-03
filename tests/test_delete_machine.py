from pages.cruds.crud_machines import CrudMachines
from test_base import TestBase

class DeleteMachine(TestBase):
    def test_delete_room(self):
        self.delete_room = CrudMachines(self.browser)
        
        
        self.delete_room.deletar_maquina()
        print('ok')
        #self.delete_room.verify_text('Sala deletada com sucesso',self.locator.SALA_DELETADA)
        
        #self.assertIn('inventory', self.browser.current_window_handle)