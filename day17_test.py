import unittest
from day17 import generate_directions, day_17

class DirectionsTests(unittest.TestCase):
    def test_directions_returns_all_directions(self):
        result = list(generate_directions(3))
        self.assertEqual(len(result), 26)
        self.assertIn([-1, -1, -1], result)
        self.assertIn([ 0, -1, -1], result)
        self.assertIn([ 1, -1, -1], result)
        self.assertIn([-1,  0, -1], result)
        self.assertIn([ 0,  0, -1], result)
        self.assertIn([ 1,  0, -1], result)
        self.assertIn([-1,  1, -1], result)
        self.assertIn([ 0,  1, -1], result)
        self.assertIn([ 1,  1, -1], result)
        self.assertIn([-1, -1,  0], result)
        self.assertIn([ 0, -1,  0], result)
        self.assertIn([ 1, -1,  0], result)
        self.assertIn([-1,  0,  0], result)
        self.assertIn([ 1,  0,  0], result)
        self.assertIn([-1,  1,  0], result)
        self.assertIn([ 0,  1,  0], result)
        self.assertIn([ 1,  1,  0], result)
        self.assertIn([-1, -1,  1], result)
        self.assertIn([ 0, -1,  1], result)
        self.assertIn([ 1, -1,  1], result)
        self.assertIn([-1,  0,  1], result)
        self.assertIn([ 0,  0,  1], result)
        self.assertIn([ 1,  0,  1], result)
        self.assertIn([-1,  1,  1], result)
        self.assertIn([ 0,  1,  1], result)
        self.assertIn([ 1,  1,  1], result)
        self.assertNotIn([ 0,  0,  0], result)

example_input = """\
.#.
..#
###
""".splitlines()

input_file = open("day17_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

class Part1Tests(unittest.TestCase):
    def test_part_1_example(self):
        result = day_17(example_input, 3, 6)
        self.assertEqual(result, 112)

    def test_part_1_real(self):
        result = day_17(input, 3, 6)
        self.assertEqual(result, 313)

class Part2Tests(unittest.TestCase):
    def test_part_2_example(self):
        result = day_17(example_input, 4, 6)
        self.assertEqual(result, 848)

    def test_part_2_real(self):
        result = day_17(input, 4, 6)
        self.assertEqual(result, 2640)