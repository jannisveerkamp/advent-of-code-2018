def day_15_task_1(grid):
    grid = split_grid(grid)
    print_grid(grid)
    return -1


def split_grid(grid):
    return list(map(lambda row: list(row), grid))


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
