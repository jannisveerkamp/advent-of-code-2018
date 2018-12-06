EMPTY = "."
MULTI = "x"
UNSAFE = "o"


def size_safe_are(coordinates, max_sum_distance):
    coordinates = parse_coordinates(coordinates)
    x_max, y_max = get_array_size(coordinates)

    area = [[EMPTY for _ in range(x_max)] for _ in range(y_max)]

    for y in range(y_max):
        for x in range(x_max):
            distance_sum = 0
            for coordinate in coordinates:
                distance = manhattan_distance(x, y, coordinate[0], coordinate[1])
                distance_sum += distance
                if distance_sum >= max_sum_distance:
                    area[y][x] = UNSAFE
                    continue

    safe_area_size = sum(x.count(EMPTY) for x in area)
    return safe_area_size


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def size_largest_area(coordinates):
    coordinates = parse_coordinates(coordinates)
    x_max, y_max = get_array_size(coordinates)

    area = [[EMPTY for _ in range(x_max)] for _ in range(y_max)]

    # put the coordinates into the area
    for i in range(len(coordinates)):
        area[coordinates[i][1]][coordinates[i][0]] = str(i)

    infinite_areas = set()

    temp_area = [[{area[y][x]} if area[y][x] != EMPTY else set() for x in range(x_max)] for y in range(y_max)]

    # do some black magic
    while EMPTY in [x for y in area for x in y]:
        for y in range(y_max):
            for x in range(x_max):
                cell = area[y][x]
                if cell != EMPTY:
                    if y == 0 or y == y_max - 1 or x == 0 or x == x_max - 1:
                        infinite_areas.add(cell)
                    fill_around_cell(temp_area, cell, x, y, x_max, y_max)
        update_area(area, temp_area, x_max, y_max)

    max_area_size = 0
    for i in range(len(coordinates)):
        if str(i) not in infinite_areas:
            max_area_size = max(max_area_size, sum(x.count(str(i)) for x in area))

    return max_area_size


def fill_around_cell(temp_area, cell, x, y, x_max, y_max):
    if x != 0:
        temp_area[y][x - 1].add(cell)
    if y != 0:
        temp_area[y - 1][x].add(cell)
    if x != x_max - 1:
        temp_area[y][x + 1].add(cell)
    if y != y_max - 1:
        temp_area[y + 1][x].add(cell)


def update_area(area, temp_area, x_max, y_max):
    for y in range(y_max):
        for x in range(x_max):
            if area[y][x] == EMPTY:
                size = len(temp_area[y][x])
                if size == 1:
                    area[y][x] = temp_area[y][x].pop()
                elif size > 1:
                    area[y][x] = MULTI


def get_array_size(coordinates):
    max_x = max(coordinates, key=lambda c: c[0])[0] + 1
    max_y = max(coordinates, key=lambda c: c[1])[1] + 1
    return max_x, max_y


def parse_coordinates(coordinates):
    parsed_coordinates = []
    for coordinate in coordinates:
        x, y = coordinate.split(", ")
        parsed_coordinates.append([int(x), int(y)])
    return parsed_coordinates


# Helper method for debugging
def print_area(area):
    for x in area:
        print("".join(x))
