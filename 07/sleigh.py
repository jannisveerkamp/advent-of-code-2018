import re


def sort_instructions(instructions):
    instructions = parse_instructions(instructions)
    letters = sorted_letters(instructions)
    reverse_instructions = reverse(instructions)

    result = []
    while len(result) < len(letters):
        for letter in letters:
            # We already sorted those
            if letter in result:
                continue

            # Append root node
            if letter not in reverse_instructions:
                result.append(letter)
                break

            # Append if all "sources" reached
            if all(dst in result for dst in reverse_instructions[letter]):
                result.append(letter)
    return "".join(result)


pattern = re.compile("Step (?P<step>\w) must be finished before step (?P<before>\w) can begin.")


def parse_instructions(instructions):
    parsed_instructions = []
    for instruction in instructions:
        match = pattern.match(instruction)
        parsed_instructions.append((match.group("step"), match.group("before")))
    return parsed_instructions


def sorted_letters(instructions):
    letters = set()
    for instruction in instructions:
        letters.add(instruction[0])
        letters.add(instruction[1])
    letters = list(letters)
    letters.sort()
    return letters


def reverse(instructions):
    reverse_instructions = dict()
    for instruction in instructions:
        if instruction[1] not in reverse_instructions:
            reverse_instructions[instruction[1]] = set()
        reverse_instructions[instruction[1]].add(instruction[0])
    return reverse_instructions
