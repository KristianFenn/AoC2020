import unittest
from day12 import part_1, part_2

input_file = open("day12_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_input = """\
F10
N3
F7
R90
F11
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_input)
        self.assertEqual(result, 25)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 582)

class Part2Tests(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_input)
        self.assertEqual(result, 286)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 52069)