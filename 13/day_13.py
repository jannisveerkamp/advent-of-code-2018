CART_LEFT = "<"
CART_UP = "^"
CART_RIGHT = ">"
CART_DOWN = "v"
CARTS = {CART_LEFT, CART_RIGHT, CART_UP, CART_DOWN}

HORI = "-"
VERT = "|"
CURVE_1 = "/"
CURVE_2 = "\\"
CROSS = "+"


class Cart:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.next_intersection_turn = CART_LEFT

    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        if self.x != other.x:
            return self.x < other.x
        return self.dir < other.dir

    def move(self):
        if self.dir == CART_LEFT:
            self.x -= 1
        elif self.dir == CART_RIGHT:
            self.x += 1
        elif self.dir == CART_UP:
            self.y -= 1
        elif self.dir == CART_DOWN:
            self.y += 1

    def turn(self):
        if self.dir == CART_LEFT and self.next_intersection_turn == CART_LEFT:
            self.dir = CART_DOWN
        elif self.dir == CART_LEFT and self.next_intersection_turn == CART_UP:
            self.dir = CART_LEFT  # nothing
        elif self.dir == CART_LEFT and self.next_intersection_turn == CART_RIGHT:
            self.dir = CART_UP

        elif self.dir == CART_UP and self.next_intersection_turn == CART_LEFT:
            self.dir = CART_LEFT
        elif self.dir == CART_UP and self.next_intersection_turn == CART_UP:
            self.dir = CART_UP  # nothing
        elif self.dir == CART_UP and self.next_intersection_turn == CART_RIGHT:
            self.dir = CART_RIGHT

        elif self.dir == CART_RIGHT and self.next_intersection_turn == CART_LEFT:
            self.dir = CART_UP
        elif self.dir == CART_RIGHT and self.next_intersection_turn == CART_UP:
            self.dir = CART_RIGHT  # nothing
        elif self.dir == CART_RIGHT and self.next_intersection_turn == CART_RIGHT:
            self.dir = CART_DOWN

        elif self.dir == CART_DOWN and self.next_intersection_turn == CART_LEFT:
            self.dir = CART_RIGHT
        elif self.dir == CART_DOWN and self.next_intersection_turn == CART_UP:
            self.dir = CART_DOWN  # nothing
        elif self.dir == CART_DOWN and self.next_intersection_turn == CART_RIGHT:
            self.dir = CART_LEFT

        if self.next_intersection_turn == CART_LEFT:
            self.next_intersection_turn = CART_UP
        elif self.next_intersection_turn == CART_UP:
            self.next_intersection_turn = CART_RIGHT
        elif self.next_intersection_turn == CART_RIGHT:
            self.next_intersection_turn = CART_LEFT


def day_13_task_1(grid):
    carts = get_initial_cart_positions(grid)

    while True:
        carts.sort()
        # print_grid_carts(grid, carts)

        for i in range(len(carts)):
            cart = carts[i]
            cart.move()

            if grid[cart.y][cart.x] == CURVE_1:
                if cart.dir == CART_UP:
                    cart.dir = CART_RIGHT
                elif cart.dir == CART_LEFT:
                    cart.dir = CART_DOWN
                elif cart.dir == CART_DOWN:
                    cart.dir = CART_LEFT
                elif cart.dir == CART_RIGHT:
                    cart.dir = CART_UP

            if grid[cart.y][cart.x] == CURVE_2:
                if cart.dir == CART_UP:
                    cart.dir = CART_LEFT
                elif cart.dir == CART_LEFT:
                    cart.dir = CART_UP
                elif cart.dir == CART_DOWN:
                    cart.dir = CART_RIGHT
                elif cart.dir == CART_RIGHT:
                    cart.dir = CART_DOWN

            if grid[cart.y][cart.x] == CROSS:
                cart.turn()

            for j in range(len(carts)):
                if i != j:
                    other_cart = carts[j]
                    if cart.y == other_cart.y and cart.x == other_cart.x:
                        # BOOM Crash!
                        return cart.x, cart.y


def day_13_task_2(grid):
    return -1, -1


def print_grid_carts(grid, carts):
    temp_grid = grid.copy()

    for cart in carts:
        temp_grid[cart.y] = grid[cart.y][:cart.x] + cart.dir + grid[cart.y][cart.x + 1:]

    for row in temp_grid:
        print("".join(row))
    print("")


def get_initial_cart_positions(grid):
    carts = []
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] in CARTS:
                carts.append(Cart(column, row, grid[row][column]))
                if grid[row][column] == CART_LEFT or grid[row][column] == CART_RIGHT:
                    grid[row] = grid[row][:column] + "-" + grid[row][column + 1:]
                elif grid[row][column] == CART_UP or grid[row][column] == CART_DOWN:
                    grid[row] = grid[row][:column] + "|" + grid[row][column + 1:]
    return carts
