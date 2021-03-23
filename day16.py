import re
from math import prod

validation_rule_re = r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"

def parse_validation_rule(line):
    re_groups = re.match(validation_rule_re, line).groups()
    name = re_groups[0]
    ranges_int = [int(x) for x in re_groups[1:]]
    ranges = [(ranges_int[0], ranges_int[1]), (ranges_int[2], ranges_int[3])]
    return (name, ranges)

def parse_input(input):
    input_iter = iter(input)
    line = next(input_iter)
    validation_rules = {}
    your_ticket = []
    tickets = []

    while line != "":
        name,ranges = parse_validation_rule(line)
        validation_rules[name] = ranges
        line = next(input_iter)
    
    next(input_iter)
    line = next(input_iter)

    your_ticket = [int(x) for x in line.split(",")]

    next(input_iter)
    next(input_iter)

    for line in input_iter:
        tickets.append([int(x) for x in line.split(",")])

    return (validation_rules, your_ticket, tickets)

def validate_number(validation_rule, num):
    for val_range in validation_rule:
        if num >= val_range[0] and num <= val_range[1]:
            return True
    
    return False

def validate_ticket(ticket, validation_rules):
    not_yet_valid = ticket.copy()
    for rule in validation_rules:
        passed_validation = [x for x in not_yet_valid if validate_number(validation_rules[rule], x)]
        not_yet_valid = [x for x in not_yet_valid if x not in passed_validation]
    return not_yet_valid

def part_1(input):
    validation_rules,your_ticket,tickets = parse_input(input)
    invalid_fields = []

    for ticket in tickets:
        ticket_invalid_fields = validate_ticket(ticket, validation_rules)
        invalid_fields.extend(ticket_invalid_fields)

    return sum(invalid_fields)

def part_2(input):
    validation_rules,your_ticket,tickets = parse_input(input)
    valid_tickets = tickets.copy()

    for ticket in tickets:
        if len(validate_ticket(ticket, validation_rules)) != 0:
            valid_tickets.remove(ticket)
    
    all_fields = list(validation_rules.keys())
    possible_columns = []
    for _ in range(0, len(your_ticket)):
        possible_columns.append(all_fields.copy())
    
    for ticket in valid_tickets:
        for idx,val in enumerate(ticket):
            fields_to_consider = possible_columns[idx]
            if len(fields_to_consider) == 1:
                continue

            for field in fields_to_consider:
                if not validate_number(validation_rules[field], val):
                    possible_columns[idx].remove(field)

    while max([len(fields) for fields in possible_columns]) > 1:
        single_field_columns = [col for col in possible_columns if len(col) == 1]
        fields_to_remove = [fields[0] for fields in single_field_columns]
        for idx,fields in enumerate(possible_columns):
            if len(fields) == 1:
                continue
            possible_columns[idx] = [field for field in possible_columns[idx] if field not in fields_to_remove]
    
    departure_field_idxes = [idx for idx, field in enumerate(possible_columns) if field[0].startswith("departure")]
    return prod([val for idx, val in enumerate(your_ticket) if idx in departure_field_idxes])
