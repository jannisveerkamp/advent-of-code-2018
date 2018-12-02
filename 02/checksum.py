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


def common_for_correct_box_ids(box_ids):
    for id_1 in box_ids:
        for id_2 in box_ids:
            diff = difference(id_1, id_2)
            if len(id_1) == len(diff) + 1:
                return diff
    return ""


def difference(id_1, id_2):
    result = ""
    for i in range(len(id_1)):
        if id_1[i] == id_2[i]:
            result += id_1[i]
    return result
