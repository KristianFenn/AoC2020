import unittest
from day14 import part_1, part_2, generate_floating_permutations, apply_floating_mask

input_file = open("day14_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_input = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_example_input(self):
        result = part_1(example_input)
        self.assertEqual(result, 165)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 11884151942312)

part_2_example_input = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()

class Part2Tests(unittest.TestCase):
    def test_floating_permutations(self):
        bit_array = [x for x in "000000000000000000000000000000X1101X"]
        result = generate_floating_permutations(bit_array)
        expected_results = [list(x) for x in [
            "000000000000000000000000000000011010",
            "000000000000000000000000000000011011",
            "000000000000000000000000000000111010",
            "000000000000000000000000000000111011"
        ]]
        assert len(result) == 4
        assert result == expected_results

    def test_apply_floating_mask(self):
        result = apply_floating_mask(42, "000000000000000000000000000000X1001X")
        assert len(result) == 4
        assert 26 in result
        assert 27 in result
        assert 58 in result
        assert 59 in result

    def test_part_2_example_input(self):
        result = part_2(part_2_example_input)
        self.assertEqual(result, 208)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 2625449018811)
    