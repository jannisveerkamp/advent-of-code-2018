import re
from datetime import datetime


class Record:
    # pattern = re.compile("#(?P<number>\d*) @ (?P<left>\d*),(?P<top>\d*): (?P<width>\d*)x(?P<height>\d*)")
    pattern = re.compile("\[(?P<date>.*)\] (Guard #)*(?P<guard>\d+)*( begins shift)*(?P<action>.*)")

    def __init__(self, claim):
        match = self.pattern.match(claim)
        self.date = datetime.strptime(match.group("date"), "%Y-%m-%d %H:%M")
        guard = match.group("guard")
        self.guard_number = 0 if guard is None else int(guard)  # optional
        self.action = match.group("action")  # optional


def find_sleepiest_guard(records):
    # parse input records
    parsed_records = []
    for record in records:
        parsed_records.append(Record(record))
    parsed_records.sort(key=lambda x: x.date)

    # get guard sleeptimes
    guard_sleeptimes = dict()
    guard_total_sleeptimes = dict()
    current_guard = 0
    sleep_time = datetime.now()

    for record in parsed_records:
        if record.guard_number != 0:
            current_guard = record.guard_number
        else:
            if record.action == "falls asleep":
                sleep_time = record.date
            else:
                time_diff = record.date - sleep_time
                if current_guard not in guard_total_sleeptimes:
                    guard_total_sleeptimes[current_guard] = 0
                    guard_sleeptimes[current_guard] = [0 for x in range(60)]
                guard_total_sleeptimes[current_guard] += int(time_diff.total_seconds() / 60)
                minute_start = sleep_time.minute
                minute_end = record.date.minute
                for x in range(minute_start, minute_end):
                    guard_sleeptimes[current_guard][x] += 1

    # find most sleepy guard
    max_sleep = 0
    sleepiest_guard = 0
    for key, value in guard_total_sleeptimes.items():
        if value > max_sleep:
            sleepiest_guard = key
            max_sleep = value

    # find most sleepy minute for given guard
    minutes = guard_sleeptimes[sleepiest_guard]
    max_minutes = 0
    max_index = 0
    # for key, value in minutes:
    for idx, value in enumerate(minutes):
        if value > max_minutes:
            max_index = idx
            max_minutes = value

    return sleepiest_guard * max_index


def find_sleepiest_guard_2(records):
    return 0
