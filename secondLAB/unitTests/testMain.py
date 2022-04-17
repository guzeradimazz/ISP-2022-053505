import unittest
from main import main

class TestMain(unittest.TestCase):
    
    def test_menu(self):
        self.assertRaises(TypeError,main,1+'9k')
        self.assertRaises(TypeError,main,[2])
        self.assertRaises(TypeError,main,False)
