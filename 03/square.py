import re

pattern = re.compile(".* @ (?P<left>\d*),(?P<top>\d*): (?P<width>\d*)x(?P<height>\d*)")


def overlap(claims):
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

    return sum(sum(y > 1 for y in x) for x in matrix)
