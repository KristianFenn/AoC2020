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
        self.contains = list()

    def __repr__(self):
        return f"{self.name} {self.contains}"

    def setContains(self, bagList):
        for childBag in self._childBagDefs:
            containedBag = next(filter(lambda bag: bag.name == childBag[1], bagList))
            self.contains.append({
                "count": int(childBag[0]), 
                "bag": containedBag
            })

    def canContainBag(self, bag):
        containedBags = list(map(lambda childBag: childBag["bag"], self.contains))
        if bag in containedBags:
            return True
        else:
            for child in containedBags:
                if child.canContainBag(bag):
                    return True

        return False
    
    def noContainedBags(self):
        total = 0

        for child in self.contains:
            total += child["count"] + (child["count"] * child["bag"].noContainedBags())
        
        return total
        

bags = list(map(lambda bagDef: Bag(bagDef), input))

for bag in bags:
    bag.setContains(bags)

shinyGold = next(filter(lambda bag: bag.name == "shiny gold", bags))

print(shinyGold.noContainedBags())