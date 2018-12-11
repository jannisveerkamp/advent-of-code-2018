def day_11_task_1(serial_number):
    grid = build_grid(serial_number)

    max_x = 0
    max_y = 0
    max_square_power = 0

    for x in range(0, 298):
        for y in range(0, 298):
            current_power = square_power(x, y, grid)
            if current_power > max_square_power:
                max_square_power = current_power
                max_x = x
                max_y = y

    return max_x, max_y


def day_11_task_2(serial_number):
    grid = build_grid(serial_number)

    max_x = 0
    max_y = 0
    max_size = 0
    max_square_power = 0
    for size in range(1, 301):
        for x in range(0, 301 - size):
            for y in range(0, 301 - size):
                current_power = square_power(x, y, grid, size)
                if current_power > max_square_power:
                    max_square_power = current_power
                    max_x = x
                    max_y = y
                    max_size = size

    return max_x, max_y, max_size


def square_power(x, y, grid, size=3):
    square_sum = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            square_sum += grid[i][j]
    return square_sum


def power_level(x, y, serial_number):
    rack_id = x + 10
    p_level = rack_id * y + serial_number
    p_level *= rack_id
    return int(str(p_level)[-3]) - 5


def build_grid(serial_number):
    grid = [[0 for _ in range(300)] for _ in range(300)]

    for x in range(0, 300):
        for y in range(0, 300):
            grid[x][y] = power_level(x, y, serial_number)
    return grid
