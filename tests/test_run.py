import sys
import unittest

sys.path.append(r"C:\Users\HaruChungHee\Documents\trabalhos letícia 2019-2026\GEP_Test")

from tests.test_login_success import LoginSuccess
from tests.test_add_room import AddRoom
from tests.test_add_room_wo_sigla import AddRoomWithOutSigla
from tests.test_delete_room import DeleteRoom
from tests.test_add_machine import AddMachine
from tests.test_delete_machine import DeleteMachine

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginSuccess))
suite.addTest(unittest.makeSuite(AddRoom))
suite.addTest(unittest.makeSuite(AddMachine))
suite.addTest(unittest.makeSuite(DeleteMachine))
suite.addTest(unittest.makeSuite(DeleteRoom))
suite.addTest(unittest.makeSuite(AddRoomWithOutSigla))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()                                                                              
    runner.run(suite)