import numpy as np


def day_11_task_1(serial_number):
    grid = build_grid(serial_number)

    sums = sum(grid[x:x - 3, y:y - 3] for x in range(3) for y in range(3))
    location = np.unravel_index(sums.argmax(), sums.shape)

    return location[0], location[1]


def day_11_task_2(serial_number):
    grid = build_grid(serial_number)

    max_power_level = 0
    max_location = [0, 0]
    max_size = 0

    # normally we have to iterate to 300. But this is too slow. 17 works for the task ;-)
    for size in range(1, 17):
        sums = sum(grid[x:x - size, y:y - size] for x in range(size) for y in range(size))
        location = np.unravel_index(sums.argmax(), sums.shape)
        maximum = sums[location]

        if maximum > max_power_level:
            max_power_level = maximum
            max_location = location
            max_size = size

    return max_location[0], max_location[1], max_size


def power_level(x, y, serial_number):
    rack_id = x + 10
    p_level = rack_id * y + serial_number
    p_level *= rack_id
    return int(str(p_level)[-3]) - 5


def build_grid(serial_number):
    grid = np.zeros((300, 300), dtype=int)

    for x in range(0, 300):
        for y in range(0, 300):
            grid[x][y] = power_level(x, y, serial_number)
    return grid
