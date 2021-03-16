import unittest
from day11 import SeatSim, OccupancyMode, part_1, part_2

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

class Part2Tests(unittest.TestCase):
    def test_part_2_first_example(self):
        result = part_2(example_1)
        self.assertEqual(result, 26)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 2214)

adj_iterations = [
"""\
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
""".splitlines(),
"""\
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
""".splitlines(),
"""\
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
""".splitlines(),
"""\
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
""".splitlines(),
"""\
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
]

los_iterations = [
"""\
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
""".splitlines(),
"""\
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
""".splitlines(),
"""\
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
""".splitlines(),
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
""".splitlines(),
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""".splitlines(),
"""\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
""".splitlines()
]

class IterationTests(unittest.TestCase):
    def test_adjacent_iteration_1(self):
        expected_tiles = [list(x) for x in adj_iterations[0]]

        sim = SeatSim(example_1, OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_adjacent_iteration_2(self):
        expected_tiles = [list(x) for x in adj_iterations[1]]

        sim = SeatSim(adj_iterations[0], OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_adjacent_iteration_3(self):
        expected_tiles = [list(x) for x in adj_iterations[2]]

        sim = SeatSim(adj_iterations[1], OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_adjacent_iteration_4(self):
        expected_tiles = [list(x) for x in adj_iterations[3]]

        sim = SeatSim(adj_iterations[2], OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_adjacent_iteration_5(self):
        expected_tiles = [list(x) for x in adj_iterations[4]]

        sim = SeatSim(adj_iterations[3], OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)

    def test_adjacent_iteration_6(self):
        expected_tiles = [list(x) for x in adj_iterations[4]]

        sim = SeatSim(adj_iterations[4], OccupancyMode.ADJACENCY)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_1(self):
        expected_tiles = [list(x) for x in los_iterations[0]]

        sim = SeatSim(example_1, OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_2(self):
        expected_tiles = [list(x) for x in los_iterations[1]]

        sim = SeatSim(los_iterations[0], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_3(self):
        expected_tiles = [list(x) for x in los_iterations[2]]

        sim = SeatSim(los_iterations[1], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_4(self):
        expected_tiles = [list(x) for x in los_iterations[3]]

        sim = SeatSim(los_iterations[2], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_5(self):
        expected_tiles = [list(x) for x in los_iterations[4]]

        sim = SeatSim(los_iterations[3], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_6(self):
        expected_tiles = [list(x) for x in los_iterations[5]]

        sim = SeatSim(los_iterations[4], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
    
    def test_los_iteration_7(self):
        expected_tiles = [list(x) for x in los_iterations[5]]

        sim = SeatSim(los_iterations[5], OccupancyMode.LINE_OF_SIGHT)
        sim.run_iteration()

        self.assertEqual(expected_tiles, sim.tiles)
