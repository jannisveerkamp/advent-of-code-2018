def reduce_polymer(polymer):
    should_remove = True
    while should_remove:
        should_remove = False
        for i in range(len(polymer) - 1):
            if should_remove_characters(polymer[i], polymer[i + 1]):
                polymer = polymer[:i] + polymer[i + 2:]
                should_remove = True
                break

    return len(polymer)


def should_remove_characters(a, b):
    return a.lower() == b.lower() and a.isupper() != b.isupper()


def remove_unit_from_polymer(polymer):
    return -1
