import re

parse_mem_re = r"mem\[([0-9]+)] = ([0-9]+)"
bit_len = 36

def to_bit_array(num):
    bit_string = bin(num)[2:]
    bin_string_len = len(bit_string)

    if bin_string_len < bit_len:
        bit_string = ("0" * (bit_len - bin_string_len)) + bit_string
    elif bin_string_len > bit_len:
        bit_string = bit_string[-bit_len:]
        
    return [x for x in bit_string]

def from_bit_array(bit_array):
    as_string = "".join(bit_array)
    return int(as_string, 2)

def apply_simple_mask(num, mask):
    num_bit_array = to_bit_array(num)
    for idx,bit in enumerate(mask):
        if bit == "0":
            num_bit_array[idx] = "0"
        elif bit == "1":
            num_bit_array[idx] = "1"
    return from_bit_array(num_bit_array)

def apply_floating_mask(num, mask):
    num_bit_array = to_bit_array(num)
    for idx,bit in enumerate(mask):
        if bit == "1":
            num_bit_array[idx] = "1"
        elif bit == "X":
            num_bit_array[idx] = "X"
    permutations = generate_floating_permutations(num_bit_array)
    return [from_bit_array(x) for x in permutations]

def generate_floating_permutations(bit_array):
    result = []
    for idx,bit in enumerate(bit_array):
        if bit == "X":
            with_zero = bit_array.copy()
            with_zero[idx] = "0"
            with_one = bit_array.copy()
            with_one[idx] = "1"
            result += generate_floating_permutations(with_zero)
            result += generate_floating_permutations(with_one)
            return result
    
    return ["".join(bit_array)]

def part_1(input):
    mask = []
    memory = {}

    for line in input:
        if line.startswith("mask"):
            mask = [x for x in line[7:]]
        elif line.startswith("mem"):
            address,val = [int(x) for x in re.match(parse_mem_re, line).groups()]
            result = apply_simple_mask(val,mask)
            memory[address] = result
    
    return sum(value for value in memory.values())

def part_2(input):
    mask = []
    memory = {}

    for line in input:
        if line.startswith("mask"):
            mask = [x for x in line[7:]]
        elif line.startswith("mem"):
            address,val = [int(x) for x in re.match(parse_mem_re, line).groups()]
            addresses = apply_floating_mask(address, mask)
            for address in addresses:
                memory[address] = val
    
    return sum(value for value in memory.values())