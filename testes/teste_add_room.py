import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.imports import *
from TesteBase import TesteBase
from pages.cruds.crud_rooms import Rooms

class TesteAddRoom(TesteBase):
    
    def teste_add_room(self):
        self.crud = Rooms()
        
        self.crud.adicionar_sala()