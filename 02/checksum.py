import collections


def checksum(box_ids):
    twos = 0
    threes = 0
    for box_id in box_ids:
        numbers = collections.Counter(box_id).values()
        if 2 in numbers:
            twos += 1
        if 3 in numbers:
            threes += 1

    return twos * threes
