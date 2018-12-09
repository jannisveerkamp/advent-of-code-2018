import re
from collections import defaultdict, deque

pattern = re.compile("(?P<players>\d*) players; last marble is worth (?P<last_marble>\d*) points")


def parse_game_rule(game_rule):
    match = pattern.match(game_rule)
    return int(match.group("players")), int(match.group("last_marble"))


def day_09(game_rule, multiplier=1):
    players, last_marble = parse_game_rule(game_rule)
    last_marble *= multiplier

    player_scores = defaultdict(int)
    current_player = 0
    circle = deque([0])

    for current_marble in range(1, last_marble + 1):
        if current_marble % 23 == 0:
            circle.rotate(-7)
            player_scores[current_player] += current_marble + circle.popleft()
            circle.rotate(1)
        else:
            circle.rotate(1)
            circle.appendleft(current_marble)
        current_player = (current_player + 1) % players

    return max(player_scores.values())
