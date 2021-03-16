from enum import Enum
from itertools import chain
from copy import deepcopy
from collections import namedtuple

Cell = namedtuple('Cell', ['row', 'col', 'tile'])

TILE_FLOOR = "."
TILE_EMPTY_SEAT = "L"
TILE_OCCUPIED_SEAT = "#"

class OccupancyMode(Enum):
    ADJACENCY = 0
    LINE_OF_SIGHT = 1

def is_seat(tile):
    return tile == TILE_EMPTY_SEAT or tile == TILE_OCCUPIED_SEAT

class CellIterator:
    def __init__(self, tiles, height, width):
        self.tiles = tiles
        self.width = width
        self.height = height
        self.row = None
        self.col = None
    
    def __next__(self):
        if self.row == None:
            self.row = 0
            self.col = 0
        else:
            self.col += 1
            if self.col >= self.width:
                self.col = 0
                self.row += 1
            if self.row >= self.height:
                raise StopIteration()
        
        return Cell(self.row, self.col, self.tiles[self.row][self.col])

class SeatSim:
    tiles = []
    considered_seats = []
    height = 0
    width = 0
    unchanged_last_iteration = False
    occupancy_mode = OccupancyMode.ADJACENCY

    def __init__(self, input, occupancy_mode):
        self.height = len(input)
        self.width = len(input[0])
        self.tiles = [list(x) for x in input]
        self.considered_seats = [[None for col in range(self.width)] for row in range(self.height)]
        self.unchanged_last_iteration = False
        self.occupancy_mode = occupancy_mode

        self.calculate_considered_seats(occupancy_mode)

    def __iter__(self):
        return CellIterator(self.tiles, self.height, self.width)

    def valid_tile_coordinate(self, row, col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width

    def search_until_seat(self, row_start, col_start, row_offset, col_offset):
        row = row_start + row_offset
        col = col_start + col_offset

        while self.valid_tile_coordinate(row, col):
            if is_seat(self.tiles[row][col]):
                return (row, col)
            
            row += row_offset
            col += col_offset
        
        return None
    
    def calculate_considered_seats(self, occupancy_mode):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for cell in self:
            if not is_seat(cell.tile):
                    continue

            seats_to_consider = []

            if occupancy_mode == OccupancyMode.ADJACENCY:
                candidate_seats = [(cell.row + row_dir, cell.col + col_dir) for row_dir, col_dir in directions]
                for can_row,can_col in candidate_seats:
                    if self.valid_tile_coordinate(can_row, can_col) and is_seat(self.tiles[can_row][can_col]):
                        seats_to_consider.append((can_row, can_col))
            elif occupancy_mode == OccupancyMode.LINE_OF_SIGHT:
                for row_offset,col_offset in directions:
                    found_seat = self.search_until_seat(cell.row, cell.col, row_offset, col_offset)
                    if found_seat is not None:
                        seats_to_consider.append(found_seat)
                
            self.considered_seats[cell.row][cell.col] = seats_to_consider


    def count_occupied_considered_seats(self, tile):
        considered_seats_for_cell = self.considered_seats[tile.row][tile.col]
        considered_tiles = [self.tiles[row][col] for row,col in considered_seats_for_cell]
        return len([tile for tile in considered_tiles if tile == TILE_OCCUPIED_SEAT])

    def run_iteration(self):
        next_tiles =  deepcopy(self.tiles)
        self.unchanged_last_iteration = True
        seat_empty_threshold = 4 if self.occupancy_mode == OccupancyMode.ADJACENCY else 5

        for cell in self:
            if not is_seat(cell.tile):
                continue

            occupied_considered_seats = self.count_occupied_considered_seats(cell)

            if (cell.tile == TILE_EMPTY_SEAT):
                if (occupied_considered_seats == 0):
                    next_tiles[cell.row][cell.col] = TILE_OCCUPIED_SEAT
                    self.unchanged_last_iteration = False
            elif (cell.tile == TILE_OCCUPIED_SEAT):
                if (occupied_considered_seats >= seat_empty_threshold):
                    next_tiles[cell.row][cell.col] = TILE_EMPTY_SEAT
                    self.unchanged_last_iteration = False
        
        self.tiles = next_tiles
    
    def total_occupied_seats(self):
        return len([tile for tile in chain.from_iterable(self.tiles) if tile == TILE_OCCUPIED_SEAT])

def part_1(input):
    sim = SeatSim(input, OccupancyMode.ADJACENCY)

    while not sim.unchanged_last_iteration:
        sim.run_iteration()
    
    return sim.total_occupied_seats()

def part_2(input):
    sim = SeatSim(input, OccupancyMode.LINE_OF_SIGHT)

    while not sim.unchanged_last_iteration:
        sim.run_iteration()
    
    return sim.total_occupied_seats()
