def frequency(changes):
    return sum(map_list_to_int(changes))


def frequency_twice(changes):
    changes = map_list_to_int(changes)
    seen_frequencies = {0}
    index = 0
    current_frequency = 0

    while True:
        current_frequency += changes[index]
        index = (index + 1) % len(changes)
        if current_frequency in seen_frequencies:
            return current_frequency
        else:
            seen_frequencies.add(current_frequency)


def map_list_to_int(changes):
    return list(map(int, changes))
