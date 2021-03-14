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
        containedBagName = list(map(lambda bagDef: bagDef[1], self._childBagDefs))
        self.contains = list(filter(lambda bag: bag.name in containedBagName, bagList))

    def canContainBag(self, bag):
        if bag in self.contains:
            return True
        else:
            for child in self.contains:
                if child.canContainBag(bag):
                    return True

        return False

bags = list(map(lambda bagDef: Bag(bagDef), input))

for bag in bags:
    bag.setContains(bags)

shinyGold = next(filter(lambda bag: bag.name == "shiny gold", bags))

canContain = filter(lambda bag: bag.canContainBag(shinyGold), bags)

print(len(list(canContain)))