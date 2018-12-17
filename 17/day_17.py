import re

import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np

pattern_x = re.compile(".*(?P<x>x=\d*(..)?\d+).*")
pattern_y = re.compile(".*(?P<y>y=\d*(..)?\d+).*")

EMPTY = 0
CLAY = 1
WATER = 2
REST = 3


def day_17_task_1(clay_veins):
    grid = parse_grid(clay_veins)
    water = {(0, 500)}
    grid[0][500] = WATER

    y_max = len(grid) - 1
    y_min = 0
    for row in grid:
        if CLAY in row:
            break
        y_min += 1

    cmap = matplotlib.colors.ListedColormap(['white', 'black', 'cyan', 'blue'])
    bounds = [0, 1, 2, 3, 4]
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    # im = plt.imshow(grid, cmap=cmap, vmin=0, vmax=1000, norm=norm)

    new_water = set()
    has_next = True
    while has_next:
        has_next = False
        # plot_grid(grid, im)

        for water_cell in water:
            y = water_cell[0]
            x = water_cell[1]
            if y < y_max:
                # Fill water exactly below
                if grid[y + 1][x] == EMPTY:
                    grid[y + 1][x] = WATER
                    new_water.add((y + 1, x))
                    continue

                # Fill horizontally
                if grid[y][x - 1] == EMPTY and (grid[y + 1][x] == CLAY or grid[y + 1][x] == REST):
                    grid[y][x - 1] = WATER
                    new_water.add((y, x - 1))
                if grid[y][x + 1] == EMPTY and (grid[y + 1][x] == CLAY or grid[y + 1][x] == REST):
                    grid[y][x + 1] = WATER
                    new_water.add((y, x + 1))

                # Fill below left/right
                if grid[y + 1][x + 1] == EMPTY and (grid[y + 1][x] == CLAY or grid[y + 1][x] == REST) and \
                        (grid[y + 1][x - 1] == CLAY or grid[y + 1][x - 1] == REST):
                    grid[y + 1][x + 1] = WATER
                    new_water.add((y + 1, x + 1))
                if grid[y + 1][x - 1] == EMPTY and (grid[y + 1][x] == CLAY or grid[y + 1][x] == REST) and \
                        (grid[y + 1][x + 1] == CLAY or grid[y + 1][x + 1] == REST):
                    grid[y + 1][x - 1] = WATER
                    new_water.add((y + 1, x - 1))
        if len(new_water) > 0:
            has_next = True
        water |= new_water
        new_water.clear()

        # Check whether the water has rested
        remove_list = set()
        for water_cell in water:
            y = water_cell[0]
            x = water_cell[1]

            if y < y_max:
                # Just check from the left direction is enough
                if grid[y][x - 1] == CLAY:
                    x_iter = x
                    while True:
                        if grid[y][x_iter] == EMPTY or grid[y + 1][x_iter] == EMPTY:
                            break
                        if grid[y][x_iter] == CLAY:
                            for i in range(x, x_iter):
                                grid[y][i] = REST
                                remove_list.add((y, i))
                                has_next = True
                            break
                        if grid[y][x_iter] == WATER:
                            x_iter += 1

        if len(new_water) > 0:
            has_next = True
        water |= new_water
        new_water.clear()
        water = water - remove_list
        remove_list.clear()

    # plot_grid(grid, im)

    water_sum = 0
    rest_sum = 0
    for row in grid:
        for cell in row:
            if cell == WATER or cell == REST:
                if cell == REST:
                    rest_sum += 1
                water_sum += 1
    return water_sum - y_min, rest_sum


def plot_grid(grid, im):
    im.set_data(grid)
    plt.draw()
    plt.pause(0.0000001)


def parse_grid(clay_veins):
    coordinates = set()

    # Parse input
    max_y = 0
    for cell in clay_veins:
        match_x = pattern_x.match(cell)
        match_y = pattern_y.match(cell)
        x = match_x.group("x").replace(", ", "").replace("x=", "").split("..")
        y = match_y.group("y").replace(", ", "").replace("y=", "").split("..")
        x = list(map(int, x))
        y = list(map(int, y))

        for row in range(y[0], y[-1] + 1):
            for column in range(x[0], x[-1] + 1):
                max_y = max(row, max_y)
                coordinates.add((row, column))

    # Generate grid
    grid = [[EMPTY for _ in range(1000)] for _ in range(max_y + 1)]

    for coordinate in coordinates:
        grid[coordinate[0]][coordinate[1]] = CLAY

    return np.array(grid)
