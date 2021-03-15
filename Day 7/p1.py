import re

input_file = open("Day 7\\input.txt", "r")
input = input_file.read().splitlines()
input_file.close()

child_bag_re = r"([0-9]) ([a-z ]+) bags?"

class Bag:
    _child_bag_defs = ""
    name = ""
    contains = []

    def __init__(self, bag_def: str):
        split = bag_def.split(" bags contain ")
        self.name = split[0]
        self._child_bag_defs = re.findall(child_bag_re, split[1])

    def __repr__(self):
        return f"{self.name} {self.contains}"

    def set_contains(self, bag_list):
        containedBagNames = [bagDef[1] for bagDef in self._child_bag_defs]
        self.contains = [bag for bag in bag_list if bag.name in containedBagNames]

    def can_contain_bag(self, bag):
        if bag in self.contains:
            return True
        else:
            for child in self.contains:
                if child.can_contain_bag(bag):
                    return True

        return False

bags = [Bag(bag_def) for bag_def in input]

for bag in bags:
    bag.set_contains(bags)

shiny_gold =  next(bag for bag in bags if bag.name == "shiny gold")
can_contain = [bag for bag in bags if bag.can_contain_bag(shiny_gold)]

print(len(can_contain))
