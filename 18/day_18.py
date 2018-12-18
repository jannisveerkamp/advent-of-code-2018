import copy

OPEN = "."
TREE = "|"
YARD = "#"


def day_18_task_1(yard, minutes):
    yard = parse_yard(yard)
    # print_yard(yard)

    for _ in range(minutes):
        y_copy = copy.deepcopy(yard)

        for row in range(len(y_copy)):
            for column in range(len(y_copy[row])):
                if y_copy[row][column] == OPEN:
                    if count_around(row, column, TREE, y_copy) >= 3:
                        yard[row][column] = TREE
                elif y_copy[row][column] == TREE:
                    if count_around(row, column, YARD, y_copy) >= 3:
                        yard[row][column] = YARD
                elif y_copy[row][column] == YARD:
                    if count_around(row, column, YARD, y_copy) == 0 or count_around(row, column, TREE, y_copy) == 0:
                        yard[row][column] = OPEN
        # print_yard(yard)

    wooded = sum(x.count(TREE) for x in yard)
    lumberyards = sum(x.count(YARD) for x in yard)
    return wooded * lumberyards


def count_around(row, column, cell_type, yard):
    counter = 0
    y_max = len(yard)
    x_max = len(yard[0])
    for y in range(row - 1, row + 2):
        for x in range(column - 1, column + 2):
            if not (y == row and x == column) and 0 <= y < y_max and 0 <= x < x_max and yard[y][x] == cell_type:
                counter += 1
    return counter


def print_yard(yard):
    for row in yard:
        print("".join(row))
    print()


def parse_yard(yard):
    return list(map(lambda row: [x for x in row], yard))
