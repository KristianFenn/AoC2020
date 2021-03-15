input_file = open("Day 1\input.txt", "r")
input = [int(x) for x in input_file.readlines()]
input_file.close()

for num_1_index in range(0, len(input)):
    for num_2_index in range(num_1_index + 1, len(input)):
        for num_3_index in range(num_2_index + 1, len(input)):
            num_1 = input[num_1_index]
            num_2 = input[num_2_index]
            num_3 = input[num_3_index]
            if (num_1 + num_2 + num_3 == 2020):
                print(num_1 * num_2 * num_3)
                exit()