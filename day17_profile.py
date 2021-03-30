import cProfile
from day17 import day_17


example_input = """\
.#.
..#
###
""".splitlines()

cProfile.run("day_17(example_input, 4, 6)")