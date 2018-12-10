import re


def sort_instructions(instructions):
    instructions = parse_instructions(instructions)
    reverse_instructions = reverse(instructions)
    letters = sorted_letters(instructions)

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


def letter_offset(letter):
    return ord(letter) - 64


class Worker:
    def __init__(self):
        self.idle = True
        self.letter = None
        self.finish = -1

    def work_on(self, letter, begin, seconds_offset):
        self.idle = False
        self.letter = letter
        self.finish = begin + seconds_offset + letter_offset(letter)

    def finish_work(self):
        self.idle = True
        self.letter = None
        self.finish = -1


def work_time(instructions, num_workers, seconds_offset):
    instructions = parse_instructions(instructions)
    reverse_instructions = reverse(instructions)
    letters = sorted_letters(instructions)

    workers = [Worker() for _ in range(num_workers)]
    finished = []
    seconds = 0

    while len(finished) < len(letters):
        # Check if worker finished her/his work
        for worker in workers:
            if worker.finish == seconds:
                finished.append(worker.letter)
                worker.finish_work()

        # Get all letters which are ready to work on
        ready = list()
        for letter in letters:
            if letter in finished or letter in ready or any(worker.letter == letter for worker in workers):
                continue
            if letter not in reverse_instructions or all(dst in finished for dst in reverse_instructions[letter]):
                ready.append(letter)

        # Get all lazy workers to work
        for worker in workers:
            if worker.idle and len(ready) > 0:
                worker.work_on(ready.pop(0), seconds, seconds_offset)

        # Travel in time
        seconds += 1

    return seconds - 1


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
