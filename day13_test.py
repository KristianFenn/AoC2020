import unittest
from day13 import part_1,part_2

input_file = open("day13_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_input = """\
939
7,13,x,x,59,x,31,19
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_input)
        self.assertEqual(result, 295)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 3385)

class Part2Tests(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_input)
        self.assertEqual(result, 1068781)

    def test_part_2_second_example(self):
        result = part_2(["123", "17,x,13,19"])
        self.assertEqual(result, 3417)

    def test_part_2_third_example(self):
        result = part_2(["123", "67,7,59,61"])
        self.assertEqual(result, 754018)

    def test_part_2_fourth_example(self):
        result = part_2(["123", "67,x,7,59,61"])
        self.assertEqual(result, 779210)

    def test_part_2_fifth_example(self):
        result = part_2(["123", "67,7,x,59,61"])
        self.assertEqual(result, 1261476)

    def test_part_2_sixth_example(self):
        result = part_2(["123", "1789,37,47,1889"])
        self.assertEqual(result, 1202161486)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 600689120448303)