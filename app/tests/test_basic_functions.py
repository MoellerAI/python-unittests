import unittest
from src.basic_functions import add_two_numbers

class TestBasicFunctions(unittest.TestCase):
    
    def test_add_two_numbers(self):
        result = add_two_numbers(1,2)
        self.assertEqual(result, 3)
