import unittest
from day17 import directions, part_1

class DirectionsTests(unittest.TestCase):
    def test_directions_returns_all_directions(self):
        result = list(directions())
        self.assertEqual(len(result), 26)
        self.assertIn((-1, -1, -1), result)
        self.assertIn(( 0, -1, -1), result)
        self.assertIn(( 1, -1, -1), result)
        self.assertIn((-1,  0, -1), result)
        self.assertIn(( 0,  0, -1), result)
        self.assertIn(( 1,  0, -1), result)
        self.assertIn((-1,  1, -1), result)
        self.assertIn(( 0,  1, -1), result)
        self.assertIn(( 1,  1, -1), result)
        self.assertIn((-1, -1,  0), result)
        self.assertIn(( 0, -1,  0), result)
        self.assertIn(( 1, -1,  0), result)
        self.assertIn((-1,  0,  0), result)
        self.assertIn(( 1,  0,  0), result)
        self.assertIn((-1,  1,  0), result)
        self.assertIn(( 0,  1,  0), result)
        self.assertIn(( 1,  1,  0), result)
        self.assertIn((-1, -1,  1), result)
        self.assertIn(( 0, -1,  1), result)
        self.assertIn(( 1, -1,  1), result)
        self.assertIn((-1,  0,  1), result)
        self.assertIn(( 0,  0,  1), result)
        self.assertIn(( 1,  0,  1), result)
        self.assertIn((-1,  1,  1), result)
        self.assertIn(( 0,  1,  1), result)
        self.assertIn(( 1,  1,  1), result)
        self.assertNotIn(( 0,  0,  0), result)

input_file = open("day17_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_input = """\
.#.
..#
###
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example(self):
        result = part_1(example_input, 6)
        self.assertEqual(result, 112)

    def test_part_1_real(self):
        result = part_1(input, 6)
        self.assertEqual(result, 313)