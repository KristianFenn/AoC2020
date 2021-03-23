import unittest
from day16 import part_1, part_2

input_file = open("day16_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()


example_input_1 = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example(self):
        result = part_1(example_input_1)
        self.assertEqual(result, 71)

    def test_part_1_real(self):
        result = part_1(input)
        self.assertEqual(result, 26988)

example_input_2 = """\
departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".splitlines()

class Part2Tests(unittest.TestCase):
    def test_part_2_example(self):
        result = part_2(example_input_2)
        self.assertEqual(result, 132)

    def test_part_2_real(self):
        result = part_2(input)
        self.assertEqual(result, 426362917709)
