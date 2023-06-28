import unittest
from pages.cruds.crud_machines import CrudMachines
from pages.cruds.crud_rooms import Rooms
from Teste_GEP.Login import GepPage
suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(GepPage))
suite.addTest(unittest.makeSuite(CrudMachines))
suite.addTest(unittest.makeSuite(Rooms))

runner = unittest.TextTestRunner()
runner.run(suite)