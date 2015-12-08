class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def create_rectangle_of_points(start, end):
        points = set()
        for x_position in range(start.x, end.x + 1):
            for y_position in range(start.y, end.y + 1):
                points.add(Point(x_position, y_position))
        return points
