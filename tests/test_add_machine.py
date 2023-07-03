from pages.cruds.crud_machines import CrudMachines
from test_base import TestBase

class AddMachine(TestBase):
    def test_add_room(self):
        self.add_room = CrudMachines(self.browser)
        
        self.add_room.adicionar_maquina('88546237','lasic', 'Baia01', 'Comp01', 'Computador Letícia')
        print('ok')
    