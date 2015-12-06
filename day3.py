from point import Point

f = open('input/Day3.txt', 'r')
input = f.read()

def getNewPosition(character, currentPosition):
    if character == '>':
        return currentPosition + Point(1, 0)
    elif character == '<':
        return currentPosition + Point(-1, 0)
    elif character == 'v':
        return currentPosition + Point(0, -1)
    elif character == '^':
        return currentPosition + Point(0, 1)
    return currentPosition

def puzzle5():
    currentPosition = Point()
    positions = set([currentPosition])
    for character in input:
        currentPosition = getNewPosition(character, currentPosition)
        positions.add(currentPosition)
    return len(positions)

def puzzle6():
    santaPosition = Point()
    roboSantaPosition = Point()
    positions = set([santaPosition])
    santasTurn = True
    for character in input:
        if santasTurn:
            santaPosition = getNewPosition(character, santaPosition)
            positions.add(santaPosition)
        else:
            roboSantaPosition = getNewPosition(character, roboSantaPosition)
            positions.add(roboSantaPosition)
        santasTurn = not santasTurn

    return len(positions)
