import re

pattern = re.compile("(?P<players>\d*) players; last marble is worth (?P<last_marble>\d*) points")


def parse_game_rule(game_rule):
    match = pattern.match(game_rule)
    return int(match.group("players")), int(match.group("last_marble"))


def day_09_task_1(game_rule):
    players, last_marble = parse_game_rule(game_rule)
    return -1
