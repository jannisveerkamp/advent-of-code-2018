def reduce_polymer(polymer):
    should_remove = True
    while should_remove:
        should_remove = False

        i = 0
        while i < len(polymer) - 1:
            if should_remove_characters(polymer[i], polymer[i + 1]):
                polymer = polymer[:i] + polymer[i + 2:]
                should_remove = True
            i += 1

    return len(polymer)


def should_remove_characters(a, b):
    return a.lower() == b.lower() and a.isupper() != b.isupper()


def remove_unit_from_polymer(polymer):
    chars = find_all_characters(polymer)

    min_length = 100000
    for char in chars:
        removed = polymer.replace(char.lower(), "").replace(char.upper(), "")
        length = reduce_polymer(removed)
        min_length = min(length, min_length)

    return min_length


def find_all_characters(polymer):
    chars = set()
    for i in range(len(polymer)):
        if polymer[i].lower() not in chars:
            chars.add(polymer[i].lower())
    return chars
