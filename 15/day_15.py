GOBLIN = "G"
ELF = "E"
FLOOR = "."
WALL = "#"


class Unit:
    def __init__(self, row, column, is_elf):
        self.row = row
        self.column = column
        self.is_elf = is_elf
        self.hp = 200
        self.attack_power = 3

    def __lt__(self, other):
        if self.row == other.row:
            return self.column < other.column
        return self.row < other.row


def day_15_task_1(grid):
    grid = split_grid(grid)
    units = find_units(grid)

    print_grid(grid)

    return -1


def find_units(grid):
    units = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == GOBLIN:
                units.append(Unit(row, column, False))
            elif grid[row][column] == ELF:
                units.append(Unit(row, column, True))
    return units


def split_grid(grid):
    return list(map(lambda row: list(row), grid))


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
