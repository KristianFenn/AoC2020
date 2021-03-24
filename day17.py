from collections import namedtuple
from copy import deepcopy

ACTIVE_CUBE = "#"
INACTIVE_CUBE = "."
        
def directions():
    for layer_offset in (-1, 0, 1):
        for row_offset in (-1, 0, 1):
            for col_offset in (-1, 0, 1):
                if layer_offset == 0 and row_offset == 0 and col_offset == 0:
                    continue
                yield Coordinate(layer_offset, row_offset, col_offset)

class Coordinate:
    def __init__(self, lay, row, col):
        self.lay = lay
        self.row = row
        self.col = col
    
    def __add__(self, other):
        return Coordinate(self.lay + other.lay, self.row + other.row, self.col + other.col)

class CubeSpace:
    def __init__(self, input, edge_offset):
        input_depth = 1
        input_height = len(input)
        input_width = len(input[0])

        self.depth = input_depth + (edge_offset * 2)
        self.height = input_height + (edge_offset * 2)
        self.width = input_width + (edge_offset * 2)

        self.cube_space = []
        for layer in range(self.depth):
            layer = []
            for _ in range(self.height):
                layer.append([INACTIVE_CUBE] * self.width)
            self.cube_space.append(layer)
        
        lay = edge_offset

        for row in range(edge_offset, edge_offset + input_height):
            for col in range(edge_offset, edge_offset + input_width):
                self.cube_space[lay][row][col] = input[row - edge_offset][col - edge_offset]
    
    def __getitem__(self, coord: Coordinate):
        return self.cube_space[coord.lay][coord.row][coord.col]
    
    def is_valid_coordinate(self, coordinate: Coordinate):
        return (coordinate.lay >= 0 and coordinate.lay < self.depth
            and coordinate.row >= 0 and coordinate.row < self.height
            and coordinate.col >= 0 and coordinate.col < self.width)
    
    def iterate(self):
        next_cube_space = deepcopy(self.cube_space)
        for lay in range(self.depth):
            for row in range(self.height):
                for col in range(self.width):
                    coord = Coordinate(lay, row, col)
                    cube = self[coord]
                    adjacent_coords = [coord + direction for direction in directions()]
                    adjacent_cubes = [self[co] for co in adjacent_coords if self.is_valid_coordinate(co)]
                    num_active_adjacents = len([cube for cube in adjacent_cubes if cube == ACTIVE_CUBE])
                    if cube == ACTIVE_CUBE and (num_active_adjacents < 2 or num_active_adjacents > 3):
                        next_cube_space[lay][row][col] = INACTIVE_CUBE
                    elif cube == INACTIVE_CUBE and num_active_adjacents == 3:
                        next_cube_space[lay][row][col] = ACTIVE_CUBE
        self.cube_space = next_cube_space
        
    def active_cubes(self):
        count = 0
        for lay in range(self.depth):
            for row in range(self.height):
                for col in range(self.width):
                    coord = Coordinate(lay, row, col)
                    if self[coord] == ACTIVE_CUBE:
                        count += 1
        return count

def part_1(input, cycles):
    cube_space = CubeSpace(input, cycles)

    for _ in range(cycles):
        cube_space.iterate()
    
    return cube_space.active_cubes()