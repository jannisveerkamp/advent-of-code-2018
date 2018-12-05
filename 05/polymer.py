def reduce_polymer(polymer):
    temp_string = ""
    for char in polymer:
        next_char = "" if not temp_string else temp_string[-1]
        if should_remove_characters(char, next_char):
            temp_string = temp_string[:-1]
        else:
            temp_string += char

    return len(temp_string)


def remove_unit_from_polymer(polymer):
    chars = find_all_characters(polymer)
    return min(reduce_polymer(polymer.replace(c.lower(), "").replace(c.upper(), "")) for c in chars)


def should_remove_characters(a, b):
    return a.lower() == b.lower() and a.isupper() != b.isupper()


def find_all_characters(polymer):
    chars = set()
    for i in range(len(polymer)):
        if polymer[i].lower() not in chars:
            chars.add(polymer[i].lower())
    return chars
