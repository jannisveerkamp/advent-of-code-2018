import re

pattern = re.compile("#(?P<number>\d*) @ (?P<left>\d*),(?P<top>\d*): (?P<width>\d*)x(?P<height>\d*)")


def overlap(claims):
    matrix = fill_matrix(claims)
    return sum(sum(y > 1 for y in x) for x in matrix)


def no_overlap(claims):
    matrix = fill_matrix(claims)

    for claim in claims:
        match = pattern.match(claim)
        number = int(match.group("number"))
        left = int(match.group("left"))
        top = int(match.group("top"))
        width = int(match.group("width"))
        height = int(match.group("height"))

        has_overlap = False
        for x in range(left, left + width):
            for y in range(top, top + height):
                if matrix[x][y] != 1:
                    has_overlap = True

        if not has_overlap:
            return number

    return -1


def fill_matrix(claims):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for claim in claims:
        match = pattern.match(claim)
        left = int(match.group("left"))
        top = int(match.group("top"))
        width = int(match.group("width"))
        height = int(match.group("height"))

        for x in range(left, left + width):
            for y in range(top, top + height):
                matrix[x][y] += 1
    return matrix
