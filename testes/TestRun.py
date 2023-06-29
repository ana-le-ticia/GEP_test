import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from pages.Login import Login

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Login))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)