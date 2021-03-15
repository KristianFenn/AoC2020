import unittest
from day6 import part_1, part_2

input_file = open("day6_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_1 = """\
abcx
abcy
abcz
""".splitlines()

example_2 = """\
abc

a
b
c

ab
ac

a
a
a
a

b
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_1(self):
        result = part_1(example_1)
        self.assertEqual(result, 6)

    def test_part_1_example_2(self):
        result = part_1(example_2)
        self.assertEqual(result, 11)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 6809)

class Part2Test(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_2)
        self.assertEqual(result, 6)
    
    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 3394)

if __name__ == '__main__':
    unittest.main()