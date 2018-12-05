def reduce_polymer(polymer):
    temp_string = ""
    for char in polymer:
        next_char = "" if not temp_string else temp_string[-1]
        if should_remove_characters(char, next_char):
            temp_string = temp_string[:-1]
        else:
            temp_string += char

    return len(temp_string)


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
