import re
from datetime import datetime


class Record:
    pattern = re.compile("\[(?P<date>.*)\] (Guard #)*(?P<guard_id>\d+)*( begins shift)*(?P<action>.*)")

    def __init__(self, claim):
        match = self.pattern.match(claim)
        self.date = datetime.strptime(match.group("date"), "%Y-%m-%d %H:%M")
        guard_id = match.group("guard_id")
        self.guard_id = 0 if guard_id is None else int(guard_id)  # optional
        self.action = match.group("action")  # optional


def find_sleepiest_guard(records):
    guard_sleeptimes, guard_total_sleeptimes = __get_guard_sleeptimes(records)

    # find most sleepy guard first
    sleepiest_guard = max(guard_total_sleeptimes, key=lambda key: guard_total_sleeptimes[key])

    # only pass the most sleepy guard
    return __max_minutes_times_sleepiest_guard_id({sleepiest_guard: guard_sleeptimes[sleepiest_guard]})


def find_sleepiest_guard_2(records):
    guard_sleeptimes, guard_total_sleeptimes = __get_guard_sleeptimes(records)
    # get the max value of all guards
    return __max_minutes_times_sleepiest_guard_id(guard_sleeptimes)


def __max_minutes_times_sleepiest_guard_id(guard_sleeptimes):
    sleepiest_guard = 0
    max_minutes = 0
    max_index = 0
    # find max minutes a guard is asleep
    for guard, minutes in guard_sleeptimes.items():
        for idx, value in enumerate(minutes):
            if value > max_minutes:
                max_index = idx
                max_minutes = value
                sleepiest_guard = guard

    return max_index * sleepiest_guard


def __get_guard_sleeptimes(records):
    # parse input records
    parsed_records = []
    for record in records:
        parsed_records.append(Record(record))
    parsed_records.sort(key=lambda current_record: current_record.date)  # Records might have a wrong order

    # get guard sleeptimes
    guard_sleeptimes = dict()
    guard_total_sleeptimes = dict()
    current_guard = 0
    sleep_time = datetime.now()

    for record in parsed_records:
        if record.guard_id != 0:
            current_guard = record.guard_id
        else:
            if record.action == "falls asleep":
                sleep_time = record.date
            else:
                time_diff = record.date - sleep_time
                if current_guard not in guard_total_sleeptimes:
                    guard_total_sleeptimes[current_guard] = 0
                    guard_sleeptimes[current_guard] = [0 for _ in range(60)]
                guard_total_sleeptimes[current_guard] += int(time_diff.total_seconds() / 60)
                minute_start = sleep_time.minute
                minute_end = record.date.minute
                for x in range(minute_start, minute_end):
                    guard_sleeptimes[current_guard][x] += 1
    return guard_sleeptimes, guard_total_sleeptimes
