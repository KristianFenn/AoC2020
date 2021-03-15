import unittest
from day9 import part_1, part_2

input_file = open("day9_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_1 = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_1, 5)
        self.assertEqual(result, 127)

    def test_part_1_real_input(self):
        result = part_1(input, 25)
        self.assertEqual(result, 257342611)

class Part2Tests(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_1, 5)
        self.assertEqual(result, 62)

    def test_part_2_real_input(self):
        result = part_2(input, 25)
        self.assertEqual(result, 35602097)

if __name__ == '__main__':
    unittest.main()