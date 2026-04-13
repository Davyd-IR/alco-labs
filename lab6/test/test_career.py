import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab_career import calculate_max_experience

class TestCareer(unittest.TestCase):

    def test_ex_1(self):
        pyramid = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(calculate_max_experience(pyramid), 12)

    def test_ex_2(self):
        pyramid = [
            [9999]
        ]
        self.assertEqual(calculate_max_experience(pyramid), 9999)

    def test_ex_3(self):
        pyramid = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(calculate_max_experience(pyramid), 3)

if __name__ == '__main__':
    unittest.main()