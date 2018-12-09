import re
from collections import defaultdict

pattern = re.compile("(?P<players>\d*) players; last marble is worth (?P<last_marble>\d*) points")


def parse_game_rule(game_rule):
    match = pattern.match(game_rule)
    return int(match.group("players")), int(match.group("last_marble"))


def day_09_task_1(game_rule):
    players, last_marble = parse_game_rule(game_rule)

    player_scores = defaultdict(int)
    current_player = 0
    position = 0
    circle = [0]

    for current_marble in range(1, last_marble + 1):
        if current_marble % 23 == 0:
            position = position - 7
            if position < 0:
                position = len(circle) + position
            player_scores[current_player] += current_marble + circle.pop(position)
        else:
            position = ((position + 1) % len(circle)) + 1
            circle.insert(position, current_marble)
        current_player = (current_player + 1) % players

    return max(player_scores.values())
