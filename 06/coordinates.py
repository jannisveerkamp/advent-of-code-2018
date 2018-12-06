def size_largest_area(coordinates):
    coordinates = parse_coordinates(coordinates)
    x_max, y_max = get_array_size(coordinates)

    area = [["." for _ in range(x_max)] for _ in range(y_max)]
    print_area(area)

    return -1


def get_array_size(coordinates):
    max_x = max(coordinates, key=lambda c: c[0])[0]
    max_y = max(coordinates, key=lambda c: c[1])[1]
    return max_x, max_y


def parse_coordinates(coordinates):
    parsed_coordinates = []
    for coordinate in coordinates:
        x, y = coordinate.split(", ")
        parsed_coordinates.append([int(x), int(y)])
    return parsed_coordinates


def print_area(area):
    for x in area:
        print("".join(x))
