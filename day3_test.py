import unittest
from day3 import part_1, part_2

input_file = open("day3_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_input = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_input)
        self.assertEqual(result, 7)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 225)

class Part2Test(unittest.TestCase):
    def test_part_2_example_input(self):
        result = part_2(example_input)
        self.assertEqual(result, 336)
    
    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 1115775000)

if __name__ == '__main__':
    unittest.main()