# TEST OF CHARACTER FREQUENCY COUNTER EXCERCISE

import unittest
from excercise_2_rock_paper_scissors import rps

# AUTOMATED TEST, DO NOT MODIFIED
class TestStringMethods(unittest.TestCase):
    def test_player_1(self):
        self.assertEqual(rps('rock', 'scissors'), "Player 1 won!")
    
    def test_player_1(self):
        self.assertEqual(rps('scissors', 'rock'), "Player 2 won!")

    def test_draw(self):
        self.assertEqual(rps('rock', 'rock'), 'Draw!')

    def test_wrong(self):
        self.assertEqual(rps('rock', 'x'), 'Wrong input!')
        self.assertEqual(rps('x', 'rock'), 'Wrong input!')

if __name__ == '__main__':
    unittest.main()