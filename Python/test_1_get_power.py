# TEST OF MAX SELECTION EXCERCISE

import unittest
from excercise_1_get_power import get_power

# AUTOMATED TEST, DO NOT MODIFIED
class TestStringMethods(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(get_power(0), [1])
        self.assertEqual(get_power(1), [1, 2])
        self.assertEqual(get_power(4), [1, 2, 4, 8, 16])

if __name__ == '__main__':
    unittest.main()