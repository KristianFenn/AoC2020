import unittest
from day5 import part_1, part_2

input_file = open("day5_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(["FBFBBFFRLR"])
        self.assertEqual(result, 357)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 980)

class Part2Test(unittest.TestCase):
    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 607)

if __name__ == '__main__':
    unittest.main()