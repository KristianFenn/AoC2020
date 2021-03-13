inputFile = open("Day 1\input.txt", "r")
input = list(map(lambda x: int(x), inputFile.readlines()))
inputFile.close()

for num1Index in range(0, len(input)):
    for num2Index in range(num1Index + 1, len(input)):
        num1 = input[num1Index]
        num2 = input[num2Index]
        if (num1 + num2 == 2020):
            print(num1 * num2)
            exit()