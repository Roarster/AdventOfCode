f = open('input/Day7.txt', 'r')

class NoValueError(Exception):
    pass

def parse_or_look_up_value(token, values):
    try:
        return int(token)
    except ValueError:
        try:
            return values[token]
        except KeyError:
            raise NoValueError

def set_wire_value(values, new_value, wire_id):
    if wire_id not in values:
        values[wire_id] = new_value

def evaluate_line(values, unsolved_lines):
    line = unsolved_lines.pop(0)
    tokens = line.split()
    # 123 -> x, y -> x
    if tokens[1] == '->':
        try:
            value = parse_or_look_up_value(tokens[0], values)
            set_wire_value(values, value, tokens[2])
        except NoValueError:
            unsolved_lines.append(line)
    # x AND y -> z
    elif tokens[1] in ['OR', 'AND']:
        try:
            left_value = parse_or_look_up_value(tokens[0], values)
            right_value = parse_or_look_up_value(tokens[2], values)
            wire_value = left_value | right_value if tokens[1] == 'OR' else left_value & right_value
            set_wire_value(values, wire_value, tokens[4])
        except NoValueError:
            unsolved_lines.append(line)
    # p LSHIFT 2 -> q
    elif tokens[1] in ['LSHIFT', 'RSHIFT']:
        try:
            left_value = parse_or_look_up_value(tokens[0], values)
            right_value = parse_or_look_up_value(tokens[2], values)
            wire_value = left_value << right_value if tokens[1] == 'LSHIFT' else left_value >> right_value
            set_wire_value(values, wire_value, tokens[4])
        except NoValueError:
            unsolved_lines.append(line)
    # NOT e -> f
    elif tokens[0] == 'NOT':
        try:
            value = parse_or_look_up_value(tokens[1], values)
            set_wire_value(values, ~value, tokens[3])
        except NoValueError:
            unsolved_lines.append(line)

def puzzle13():
    f.seek(0)
    wire_values = dict()
    unsolved_lines = f.read().splitlines()
    while len(unsolved_lines) > 0:
        evaluate_line(wire_values, unsolved_lines)
    return wire_values['a']

def puzzle14():
    previous_result = puzzle13()
    f.seek(0)
    wire_values = {'b': previous_result}
    unsolved_lines = f.read().splitlines()
    while len(unsolved_lines) > 0:
        evaluate_line(wire_values, unsolved_lines)
    return wire_values['a']
