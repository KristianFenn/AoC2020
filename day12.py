import re

instruction_re = r"([A-Z])([0-9]+)"

heading_directions = {
    0: (0, 1),
    90: (1, 0),
    180: (0, -1),
    270: (-1, 0)
}

def part_1(input):
    heading = 90

    east = 0
    north = 0

    instructions = [re.match(instruction_re, inst).groups() for inst in input]
    instructions = [(inst[0], int(inst[1])) for inst in instructions]

    for instruction,value in instructions:
        if instruction == "N":
            north += value
        elif instruction == "S":
            north -= value
        elif instruction == "E":
            east += value
        elif instruction == "W":
            east -= value
        elif instruction == "L":
            heading = (heading - value) % 360
        elif instruction == "R":
            heading = (heading + value) % 360
        elif instruction == "F":
            direction = heading_directions[heading]
            east += direction[0] * value
            north += direction[1] * value
    
    return abs(east) + abs(north)

heading_transform = {

}

def transform_coordinate(angle_to_right, east, north):
    new_east = east
    new_north = north

    if angle_to_right == 90:
        new_east = north
        new_north = east * -1
    elif angle_to_right == 180:
        new_east = east * -1 
        new_north = north * -1
    if angle_to_right == 270:
        new_east = north * -1
        new_north = east

    return new_east,new_north


def part_2(input):
    ship_east = 0
    ship_north = 0

    waypoint_east = 10
    waypoint_north = 1

    instructions = [re.match(instruction_re, inst).groups() for inst in input]
    instructions = [(inst[0], int(inst[1])) for inst in instructions]

    for instruction,value in instructions:
        if instruction == "N":
            waypoint_north += value
        elif instruction == "S":
            waypoint_north -= value
        elif instruction == "E":
            waypoint_east += value
        elif instruction == "W":
            waypoint_east -= value
        elif instruction == "L":
            angle_to_right = -value % 360
            waypoint_east,waypoint_north = transform_coordinate(angle_to_right, waypoint_east, waypoint_north)
        elif instruction == "R":
            angle_to_right = value % 360
            waypoint_east,waypoint_north = transform_coordinate(angle_to_right, waypoint_east, waypoint_north)
        elif instruction == "F":
            ship_east += waypoint_east * value
            ship_north += waypoint_north * value
    
    return abs(ship_east) + abs(ship_north)
    