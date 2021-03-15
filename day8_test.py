import unittest
from day8 import part_1, part_2

input_file = open("day8_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_1 = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_1)
        self.assertEqual(result, 5)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 1586)

class Part2Tests(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_1)
        self.assertEqual(result, 8)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 703)


if __name__ == '__main__':
    unittest.main()