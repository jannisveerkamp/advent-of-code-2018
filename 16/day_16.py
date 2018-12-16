ADDR = "addr"
ADDI = "addi"
MULR = "mulr"
MULI = "muli"
BANR = "banr"
BANI = "bani"
BORR = "borr"
BORI = "bori"
SETR = "setr"
SETI = "seti"
GTIR = "gtir"
GTRI = "gtri"
GTRR = "gtrr"
EQRI = "eqri"
EQIR = "eqir"
EQRR = "eqrr"
OPCODES = {ADDR, ADDI, MULR, MULI, BANR, BANI, BORR, BORI, SETR, SETI, GTIR, GTRR, EQRI, EQIR, EQRR}


def op(register, opcode, input1, input2, output):
    if opcode == ADDR:
        register[output] = register[input1] + register[input2]
    elif opcode == ADDI:
        register[output] = register[input1] + input2
    elif opcode == MULR:
        register[output] = register[input1] * register[input2]
    elif opcode == MULI:
        register[output] = register[input1] * input2
    elif opcode == BANR:
        register[output] = register[input1] & register[input2]
    elif opcode == BANI:
        register[output] = register[input1] & input2
    elif opcode == BORR:
        register[output] = register[input1] | register[input2]
    elif opcode == BORI:
        register[output] = register[input1] | input2
    elif opcode == SETR:
        register[output] = register[input1]
    elif opcode == SETI:
        register[output] = input1
    elif opcode == GTIR:
        register[output] = 1 if input1 > register[input2] else 0
    elif opcode == GTRI:
        register[output] = 1 if register[input1] > input2 else 0
    elif opcode == GTRR:
        register[output] = 1 if register[input1] > register[input2] else 0
    elif opcode == EQRI:
        register[output] = 1 if input1 == register[input2] else 0
    elif opcode == EQIR:
        register[output] = 1 if register[input1] == input2 else 0
    elif opcode == EQRR:
        register[output] = 1 if register[input1] == register[input2] else 0


def day_16_task_1(instructions):
    instructions = parse_instructions(instructions)
    three_or_more = 0

    for instruction in instructions:
        counter = 0
        for opcode in OPCODES:
            register = instruction[0].copy()
            _, a, b, c = instruction[1]
            op(register, opcode, a, b, c)
            if register == instruction[2]:
                counter += 1
        if counter > 2:
            three_or_more += 1

    return three_or_more


def day_16_task_2(instructions, programm):
    return -1


def parse_instructions(instructions):
    chunks = [instructions[i:i + 3] for i in range(0, len(instructions), 4)]

    result = []
    for chunk in chunks:
        before = list(map(int, chunk[0][chunk[0].index("[") + 1: chunk[0].index("]")].split(",")))
        instruction = list(map(int, chunk[1].split()))
        after = list(map(int, chunk[2][chunk[2].index("[") + 1: chunk[2].index("]")].split(",")))
        result.append((before, instruction, after))
    return result
