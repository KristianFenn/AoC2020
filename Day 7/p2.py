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
        self._childBagDefs = [
            { "count": int(bagDef[0]), "bagName": bagDef[1] } for bagDef in re.findall(childBagRe, split[1])
        ]
        self.contains = list()

    def __repr__(self):
        return f"{self.name} {self.contains}"

    def setContains(self, bagList):
        for childBagDef in self._childBagDefs:
            self.contains.append({
                "count": childBagDef["count"], 
                "bag": next(bag for bag in bagList if bag.name == childBagDef["bagName"])
            })

    def canContainBag(self, bag):
        containedBags = [childBag["bag"] for childBag in self.contains]
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
        

bags = [Bag(bagDef) for bagDef in input]

for bag in bags:
    bag.setContains(bags)

shinyGold = next(bag for bag in bags if bag.name == "shiny gold")

print(shinyGold.noContainedBags())