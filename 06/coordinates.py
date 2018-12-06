EMPTY = "."
MULTI = "x"


def size_safe_are(coordinates):
    return -1


def size_largest_area(coordinates):
    coordinates = parse_coordinates(coordinates)
    x_max, y_max = get_array_size(coordinates)

    area = [[EMPTY for _ in range(x_max)] for _ in range(y_max)]

    # put the coordinates into the area
    for i in range(len(coordinates)):
        area[coordinates[i][1]][coordinates[i][0]] = str(i)
    # print_area(area)
    # print("")

    infinite_areas = set()

    temp_area = [[{area[y][x]} for x in range(x_max)] for y in range(y_max)]

    # do some black magic
    while EMPTY in [x for y in area for x in y]:
        for y in range(y_max):
            for x in range(x_max):
                cell = area[y][x]
                if cell != EMPTY:
                    if y == 0 or y == y_max - 1 or x == 0 or x == x_max - 1:
                        infinite_areas.add(cell)
                    # fill around cell
                    fill_round_cell(temp_area, cell, x, y, x_max, y_max)
        update_area(area, temp_area, x_max, y_max)

    # print_area(area)

    max_area_size = 0
    for i in range(len(coordinates)):
        if str(i) not in infinite_areas:
            max_area_size = max(max_area_size, sum(x.count(str(i)) for x in area))

    return max_area_size


def fill_round_cell(temp_area, cell, x, y, x_max, y_max):
    if x != 0:
        fill(temp_area, cell, x - 1, y)
    if y != 0:
        fill(temp_area, cell, x, y - 1)
    if x != x_max - 1:
        fill(temp_area, cell, x + 1, y)
    if y != y_max - 1:
        fill(temp_area, cell, x, y + 1)


def fill(temp_area, cell, x, y):
    if EMPTY in temp_area[y][x]:
        temp_area[y][x].remove(EMPTY)
    temp_area[y][x].add(cell)


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
