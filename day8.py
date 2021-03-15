import re

instruction_re = r"([a-z]+) \+?([\-0-9]+)"

def run_program(instructions):
    accumulator = 0
    program_counter = 0

    was_executed = [False for instruction in instructions]
    looped = False

    while True:
        if program_counter >= len(instructions):
            break
        elif was_executed[program_counter]:
            looped = True
            break

        opcode,val = instructions[program_counter]

        if opcode == "acc":
            accumulator += val 
        elif opcode == "jmp":
            program_counter += val
            continue
        
        was_executed[program_counter] = True
        program_counter += 1

    return { "looped": looped, "accumulator": accumulator }

def parse_instructions(input):
    instructions_raw = [re.search(instruction_re, inst).groups() for inst in input]
    instructions = [(inst[0], int(inst[1])) for inst in instructions_raw]
    return instructions

def part_1(input):
    instructions = parse_instructions(input)

    result = run_program(instructions)

    return result["accumulator"]

def part_2(input):
    instructions = parse_instructions(input)

    nop_and_jmp_idxes = (idx for idx, inst in enumerate(instructions) if inst[0] == "nop" or inst[0] == "jmp")

    while True:
        idx = next(nop_and_jmp_idxes)

        original_inst = instructions[idx]

        if instructions[idx][0] == "nop":
            # we don't want to produce a jmp +/- 0, as this will cause an infinite loop
            if (instructions[idx][1] == 0):
                continue

            instructions[idx] = ("jmp", instructions[idx][1])
        else:
            instructions[idx] = ("nop", instructions[idx][1])
        
        result = run_program(instructions)

        if not result["looped"]:
            return result["accumulator"]

        instructions[idx] = original_inst
        
