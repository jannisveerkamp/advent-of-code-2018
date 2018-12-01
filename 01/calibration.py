def frequency(input):
    sum = 0
    for number in input:
        sum += int(number)
    return sum


def frequency_twice(input):
    seen_frequencies = [0]
    index = 0
    current_frequency = 0

    while True:
        current_frequency += int(input[index])
        index = (index + 1) % len(input)
        if current_frequency in seen_frequencies:
            return current_frequency
        else:
            seen_frequencies.append(current_frequency)
    