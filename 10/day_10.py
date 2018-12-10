import re

pattern = re.compile("position=< ?(?P<x>-?\d*),  ?(?P<y>-?\d*)> velocity=< ?(?P<dx>-?\d*).  ?(?P<dy>-?\d*)>")
DOT = "#"
EMPTY = "."


class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move_on(self, multiplier=1):
        self.x += self.dx * multiplier
        self.y += self.dy * multiplier


def parse_instructions(instructions):
    result = []
    for instruction in instructions:
        m = pattern.match(instruction)
        result.append(Point(int(m.group("x")), int(m.group("y")), int(m.group("dx")), int(m.group("dy"))))
    return result


def day_10(instructions, iterations, skip_iterations, return_on_max_y):
    points = parse_instructions(instructions)

    # Skip iterations to speed up everything
    for point in points:
        point.move_on(skip_iterations)

    # The correct solution should have no big gap in the y direction. Ideally it SHOULD search for a minimum ;-)
    for i in range(0, iterations):
        if max(points, key=lambda p: p.y).y - min(points, key=lambda p: p.y).y <= return_on_max_y:
            print_points(points)
            return skip_iterations + i
        for point in points:
            point.move_on()
    return -1


def print_points(points):
    min_x = min(points, key=lambda p: p.x).x
    max_x = max(points, key=lambda p: p.x).x
    min_y = min(points, key=lambda p: p.y).y
    max_y = max(points, key=lambda p: p.y).y

    output = [[EMPTY for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for point in points:
        output[point.y - min_y][point.x - min_x] = DOT

    for y in output:
        print("".join("".join(y)))
    print()
