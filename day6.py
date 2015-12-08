from point import Point

f = open('input/Day6.txt', 'r')

def get_point_from_text(text):
    parts = text.split(',')
    return Point(int(parts[0]), int(parts[1]))

def puzzle11():
    lights_on = set()
    f.seek(0)
    for line in f:
        parts = line.split()
        if parts[0] == 'toggle':
            start = get_point_from_text(parts[1])
            end = get_point_from_text(parts[3])
            lights_on = lights_on.symmetric_difference(Point.create_rectangle_of_points(start, end))
        elif parts[0] + parts[1] == 'turnon':
            start = get_point_from_text(parts[2])
            end = get_point_from_text(parts[4])
            lights_on = lights_on.union(Point.create_rectangle_of_points(start, end))
        elif parts[0] + parts[1] == 'turnoff':
            start = get_point_from_text(parts[2])
            end = get_point_from_text(parts[4])
            lights_on = lights_on.difference(Point.create_rectangle_of_points(start, end))
    return len(lights_on)

def puzzle12():
    lights_on = dict()
    f.seek(0)
    for line in f:
        parts = line.split()
        if parts[0] == 'toggle':
            start = get_point_from_text(parts[1])
            end = get_point_from_text(parts[3])
            points = Point.create_rectangle_of_points(start, end)
            difference = 2
        elif parts[0] + parts[1] == 'turnon':
            start = get_point_from_text(parts[2])
            end = get_point_from_text(parts[4])
            points = Point.create_rectangle_of_points(start, end)
            difference = 1
        elif parts[0] + parts[1] == 'turnoff':
            start = get_point_from_text(parts[2])
            end = get_point_from_text(parts[4])
            points = Point.create_rectangle_of_points(start, end)
            difference = -1
        for point in points:
            try:
                lights_on[point] += difference
            except KeyError:
                lights_on[point] = difference
            if lights_on[point] < 0:
                lights_on[point] = 0
    return sum(lights_on.values())
