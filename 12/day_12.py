MAX_GENERATIONS = 100  # Try & error for this value
EXTENSION_SIZE = MAX_GENERATIONS + 1


def day_12(instructions, generations):
    current_state, instructions = parse_instructions(instructions)
    current_state = expand(current_state)

    total_range = min(100, generations)

    for generation in range(total_range):
        new_state = current_state.copy()
        for pot_index in range(2, len(current_state) - 2):
            current_area = "".join(current_state[pot_index - 2: pot_index + 3])
            if current_area in instructions:
                new_state[pot_index] = instructions[current_area]
            else:
                new_state[pot_index] = "."
        current_state = new_state.copy()

    return pot_sum(current_state) + (generations - total_range) * 62  # 62 only relevant for part 2, depends on input


def expand(current_state):
    pre = ["."] * EXTENSION_SIZE
    post = ["."] * EXTENSION_SIZE
    pre.extend(current_state)
    pre.extend(post)
    return pre


def pot_sum(state):
    return sum(i - EXTENSION_SIZE if state[i] == "#" else 0 for i in range(len(state)))


def parse_instructions(instructions):
    initial_state = instructions[0].replace("initial state: ", "")

    parsed_instructions = dict()
    for i in range(2, len(instructions)):
        parsed_instructions[instructions[i][0:5]] = instructions[i][-1]

    return initial_state, parsed_instructions
