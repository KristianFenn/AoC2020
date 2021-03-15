import unittest
from day2 import part_1, part_2

input_file = open("day2_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        result = part_1(test_input)
        self.assertEqual(result, 2)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 410)

class Part2Test(unittest.TestCase):
    def test_part_2_example_input(self):
        test_input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        result = part_2(test_input)
        self.assertEqual(result, 1)
    
    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 694)

if __name__ == '__main__':
    unittest.main()