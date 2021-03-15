import unittest
from day10 import part_1, part_2

input_file = open("day10_input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

example_1 = """\
16
10
15
5
1
11
7
19
6
12
4
""".splitlines()


example_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".splitlines()

class Part1Tests(unittest.TestCase):
    def test_part_1_first_example(self):
        result = part_1(example_1)
        self.assertEqual(result, 35)

    def test_part_1_second_example(self):
        result = part_1(example_2)
        self.assertEqual(result, 220)

    def test_part_1_real_input(self):
        result = part_1(input)
        self.assertEqual(result, 2664)


class Part2Tests(unittest.TestCase):
    def test_part_2_first_example(self):
        result = part_2(example_1)
        self.assertEqual(result, 8)

    def test_part_2_second_example(self):
        result = part_2(example_2)
        self.assertEqual(result, 19208)

    def test_part_2_real_input(self):
        result = part_2(input)
        self.assertEqual(result, 148098383347712)



if __name__ == '__main__':
    unittest.main()