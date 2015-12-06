f = open('input/Day2.txt', 'r')

def puzzle3():
    f.seek(0)
    area = 0
    for line in f:
        tokens = line.split('x')
        length = int(tokens[0])
        width = int(tokens[1])
        height = int(tokens[2])
        longest = max(length, width, height)
        area =  area + 2*length*width + 2*width*height + 2*height*length + (length*width*height)/longest
    return area

def puzzle4():
    f.seek(0)
    totalLength = 0
    for line in f:
        tokens = line.split('x')
        length = int(tokens[0])
        width = int(tokens[1])
        height = int(tokens[2])
        longest = max(length, width, height)
        totalLength = totalLength + length + length + width + width + height + height - longest - longest + (length*width*height)
    return totalLength
