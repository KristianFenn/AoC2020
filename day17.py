from collections import namedtuple
from copy import deepcopy
from functools import cache

ACTIVE_CUBE = "#"
INACTIVE_CUBE = "."

def generate_directions(dimensions):
    offsets = [-1, 0, 1]
    output = [[-1], [0], [1]]
    
    for _ in range(dimensions - 1):
        new_output = []
        for direction in output:
            for offset in offsets:
                new_output.append([offset] + direction)
        output = new_output
    
    all_zero = [0] * dimensions
    output.remove(all_zero)

    return [tuple(x) for x in output]

def add_coordinates(coord_1, coord_2):
    result = ()

    for idx in range(len(coord_1)):
        result += (coord_1[idx] + coord_2[idx],)

    return result

class CubeSpace:
    def __init__(self, input, dimensions, edge_offset):
        input_height = len(input)
        input_width = len(input[0])

        min_magnitude = 1 + (edge_offset * 2)
        height = input_height + (edge_offset * 2)
        width = input_width + (edge_offset * 2)
        self.bounds = ([min_magnitude] * (dimensions - 2)) + [height, width]

        self.cube_space = [INACTIVE_CUBE] * width

        for bound in reversed(self.bounds[:-1]):
            new_cube_space = []
            for _ in range(bound):
                new_cube_space.append(deepcopy(self.cube_space))
            self.cube_space = new_cube_space

        for row in range(edge_offset, edge_offset + input_height):
            for col in range(edge_offset, edge_offset + input_width):
                coord = tuple([edge_offset] * (dimensions - 2) + [row, col])
                self[coord] = input[row - edge_offset][col - edge_offset]
        
        self.all_coords = self.generate_all_possible_coords()
        self.dimensions = dimensions
        self.adjacent_cache = {}
        self.directions = generate_directions(self.dimensions)
    
    def __getitem__(self, coord):
        target = self.cube_space
        for dim in coord:
            target = target[dim]
        return target
    
    def __setitem__(self, coord, val):
        target_list = self.cube_space
        for dim in coord[:-1]:
            target_list = target_list[dim]
        target_list[coord[-1]] = val

    @cache
    def is_valid_coordinate(self, coordinate):
        coord_and_bound = zip(coordinate, self.bounds)
        for coord,bound in coord_and_bound:
            if coord < 0 or coord >= bound:
                return False
        return True

    @cache
    def get_valid_adjacent_coordinates(self, coord):
        candidate_coords = [add_coordinates(coord, direction) for direction in self.directions]
        return [co for co in candidate_coords if self.is_valid_coordinate(co)]
    
    def generate_all_possible_coords(self):
        output = [[x] for x in range(self.bounds[-1])]
        for bound in reversed(self.bounds[:-1]):
            new_output = []
            for item in output:
                for dim_to_add in range(bound):
                    new_output.append([dim_to_add] + item)
            output = new_output
        return [tuple(x) for x in output]
        
    def active_cubes(self):
        count = 0
        for coord in self.all_coords:
            if self[coord] == ACTIVE_CUBE:
                count += 1
        return count

class CubeSpaceSimulator:
    def __init__(self, input, dimensions, edge_offset):
        self.cube_space = CubeSpace(input, dimensions, edge_offset)
        self.dimensions = dimensions
    
    def iterate(self):
        updates = []
        for coord in self.cube_space.all_coords:
            cube = self.cube_space[coord]
            adjacent_coords = [co for co in self.cube_space.get_valid_adjacent_coordinates(coord)]
            adjacent_cubes = [self.cube_space[co] for co in adjacent_coords]
            num_active_adjacents = len([cube for cube in adjacent_cubes if cube == ACTIVE_CUBE])
            if cube == ACTIVE_CUBE and (num_active_adjacents < 2 or num_active_adjacents > 3):
                updates.append((coord, INACTIVE_CUBE))
            elif cube == INACTIVE_CUBE and num_active_adjacents == 3:
                updates.append((coord, ACTIVE_CUBE))
        for coord,new_cube in updates:
            self.cube_space[coord] = new_cube

def day_17(input, dimensions, cycles):
    cube_space_sim = CubeSpaceSimulator(input, dimensions, cycles)

    for _ in range(cycles):
        cube_space_sim.iterate()
    
    return cube_space_sim.cube_space.active_cubes()
