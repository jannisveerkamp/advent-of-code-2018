import re


class Claim:
    pattern = re.compile("#(?P<number>\d*) @ (?P<left>\d*),(?P<top>\d*): (?P<width>\d*)x(?P<height>\d*)")

    def __init__(self, claim):
        match = self.pattern.match(claim)
        self.number = int(match.group("number"))
        self.left = int(match.group("left"))
        self.top = int(match.group("top"))
        self.width = int(match.group("width"))
        self.height = int(match.group("height"))


def overlap(claims):
    claim_list = [Claim(claim) for claim in claims]
    matrix = __fill_matrix(claim_list)
    return sum(sum(y > 1 for y in x) for x in matrix)


def no_overlap(claims):
    claim_list = [Claim(claim) for claim in claims]
    matrix = __fill_matrix(claim_list)

    for claim in claim_list:
        if not find_overlap(claim, matrix):
            return claim.number
    return -1


def find_overlap(claim, matrix):
    for x in range(claim.left, claim.left + claim.width):
        for y in range(claim.top, claim.top + claim.height):
            if matrix[x][y] != 1:
                return True
    return False


def __fill_matrix(claims):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                matrix[x][y] += 1
    return matrix
