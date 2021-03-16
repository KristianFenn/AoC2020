import unittest
from day11 import SeatSim, OccupancyMode, part_1

input_file = open("day11_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_1 = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_first_example(self):
        result = part_1(example_1)
        self.assertEqual(result, 37)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 2468)

example_1_iteration_1 = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
""".splitlines()

example_1_iteration_2 = """\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
""".splitlines()

example_1_iteration_3 = """\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
""".splitlines()

example_1_iteration_4 = """\
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
""".splitlines()

example_1_iteration_5 = """\
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
""".splitlines()


class IterationTests(unittest.TestCase):
    def test_iteration_1(self):
        expected_tiles = [list(x) for x in example_1_iteration_1]

        sim = SeatSim(example_1, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_iteration_2(self):
        expected_tiles = [list(x) for x in example_1_iteration_2]

        sim = SeatSim(example_1_iteration_1, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_iteration_3(self):
        expected_tiles = [list(x) for x in example_1_iteration_3]

        sim = SeatSim(example_1_iteration_2, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)


    def test_iteration_4(self):
        expected_tiles = [list(x) for x in example_1_iteration_4]

        sim = SeatSim(example_1_iteration_3, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_iteration_5(self):
        expected_tiles = [list(x) for x in example_1_iteration_5]

        sim = SeatSim(example_1_iteration_4, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)