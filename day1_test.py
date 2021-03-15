import unittest
from day1 import part_1, part_2

input_file = open("day1_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        test_input = ["1721", "979", "366", "299", "675", "1456"]
        result = part_1(test_input)
        self.assertEqual(result, 514579)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 1014171)

class Part2Test(unittest.TestCase):
    def test_part_2_example_input(self):
        test_input = ["1721", "979", "366", "299", "675", "1456"]
        result = part_2(test_input)
        self.assertEqual(result, 241861950)
    
    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 46584630)

if __name__ == '__main__':
    unittest.main()