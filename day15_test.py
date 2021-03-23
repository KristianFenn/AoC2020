import unittest
from day15 import day_15

example_input = [0, 3, 6]
input = [16, 11, 15, 0, 1, 7]

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = day_15(example_input, 2020)
        self.assertEqual(result, 436)

    def test_part_1_real_input(self):
        result = day_15(input, 2020)
        self.assertEqual(result, 662)

class Part2Tests(unittest.TestCase):
    def test_part_2_example_input(self):
        result = day_15(example_input, 30000000)
        self.assertEqual(result, 175594)

    def test_part_2_real_input(self):
        result = day_15(input, 30000000)
        self.assertEqual(result, 37312)