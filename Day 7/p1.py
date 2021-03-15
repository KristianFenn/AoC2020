import re

inputFile = open("Day 7\\input.txt", "r")
input = inputFile.read().splitlines()
inputFile.close()

childBagRe = r"([0-9]) ([a-z ]+) bags?"

class Bag:
    _childBagDefs = ""
    name = ""
    contains = list()

    def __init__(self, bagDef: str):
        split = bagDef.split(" bags contain ")
        self.name = split[0]
        self._childBagDefs = re.findall(childBagRe, split[1])

    def __repr__(self):
        return f"{self.name} {self.contains}"

    def setContains(self, bagList):
        containedBagNames = [bagDef[1] for bagDef in self._childBagDefs]
        self.contains = [bag for bag in bagList if bag.name in containedBagNames]

    def canContainBag(self, bag):
        if bag in self.contains:
            return True
        else:
            for child in self.contains:
                if child.canContainBag(bag):
                    return True

        return False

bags = [Bag(bagDef) for bagDef in input]

for bag in bags:
    bag.setContains(bags)

shinyGold =  next(bag for bag in bags if bag.name == "shiny gold")
canContain = [bag for bag in bags if bag.canContainBag(shinyGold)]

print(len(canContain))