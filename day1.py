

f = open('input/Day1.txt', 'r')
input = f.read()

def getFloorChange(character):
    if character == '(':
        return 1
    elif character == ')':
        return -1
    return 0

def puzzle1():
    floor = 0
    for character in input:
        floor = floor + getFloorChange(character)
    return floor

def puzzle2():
    floor = 0
    position = 1
    for character in input:
        floor = floor + getFloorChange(character)
        if floor < 0:
            return position
        position = position + 1
    # assume we'll never get here
    return position
