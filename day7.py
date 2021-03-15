import re

child_bag_re = r"([0-9]) ([a-z ]+) bags?"

class Bag:
    _child_bag_defs = ""
    name = ""
    contains = []

    def __init__(self, bag_def: str):
        split = bag_def.split(" bags contain ")
        self.name = split[0]
        self._child_bag_defs = re.findall(child_bag_re, split[1])
        self.contains = []

    def __repr__(self):
        return f"{self.name} {self.contains}"

    def set_contains(self, bagList):
        for child_bag_def in self._child_bag_defs:
            self.contains.append({
                "count": int(child_bag_def[0]), 
                "bag": next(bag for bag in bagList if bag.name == child_bag_def[1])
            })

    def can_contain_bag(self, bag):
        contained_bags = [childBag["bag"] for childBag in self.contains]
        if bag in contained_bags:
            return True
        else:
            for child in contained_bags:
                if child.can_contain_bag(bag):
                    return True

        return False
    
    def no_contained_bags(self):
        total = 0

        for child in self.contains:
            total += child["count"] + (child["count"] * child["bag"].no_contained_bags())
        
        return total
    
def parse_bags_input(input):
    bags = [Bag(bag_def) for bag_def in input]

    for bag in bags:
        bag.set_contains(bags)
    
    return bags
        
def part_1(input):
    bags = parse_bags_input(input)

    shiny_gold = next(bag for bag in bags if bag.name == "shiny gold")

    can_contain = [bag for bag in bags if bag.can_contain_bag(shiny_gold)]

    return len(can_contain)

def part_2(input):
    bags = parse_bags_input(input)

    shiny_gold = next(bag for bag in bags if bag.name == "shiny gold")

    return shiny_gold.no_contained_bags()
