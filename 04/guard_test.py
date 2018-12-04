import unittest

from common.file import read_file_lines
from .guard import find_sleepiest_guard, find_sleepiest_guard_2


class TestSleepiestGuard(unittest.TestCase):

    def test_simple_find_sleepiest_guard(self):
        test_input = ["[1518-11-01 00:00] Guard #10 begins shift",
                      "[1518-11-01 00:05] falls asleep",
                      "[1518-11-01 00:25] wakes up",
                      "[1518-11-01 00:30] falls asleep",
                      "[1518-11-01 00:55] wakes up",
                      "[1518-11-01 23:58] Guard #99 begins shift",
                      "[1518-11-02 00:40] falls asleep",
                      "[1518-11-02 00:50] wakes up",
                      "[1518-11-03 00:05] Guard #10 begins shift",
                      "[1518-11-03 00:24] falls asleep",
                      "[1518-11-03 00:29] wakes up",
                      "[1518-11-04 00:02] Guard #99 begins shift",
                      "[1518-11-04 00:36] falls asleep",
                      "[1518-11-04 00:46] wakes up",
                      "[1518-11-05 00:03] Guard #99 begins shift",
                      "[1518-11-05 00:45] falls asleep",
                      "[1518-11-05 00:55] wakes up"]
        self.assertEqual(find_sleepiest_guard(test_input), 240)

    def test_simple_find_sleepiest_guard_unsorted(self):
        test_input = ["[1518-11-01 00:55] wakes up",
                      "[1518-11-01 00:25] wakes up",
                      "[1518-11-01 00:30] falls asleep",
                      "[1518-11-01 23:58] Guard #99 begins shift",
                      "[1518-11-02 00:40] falls asleep",
                      "[1518-11-03 00:05] Guard #10 begins shift",
                      "[1518-11-02 00:50] wakes up",
                      "[1518-11-03 00:29] wakes up",
                      "[1518-11-03 00:24] falls asleep",
                      "[1518-11-05 00:55] wakes up",
                      "[1518-11-01 00:05] falls asleep",
                      "[1518-11-05 00:03] Guard #99 begins shift",
                      "[1518-11-04 00:02] Guard #99 begins shift",
                      "[1518-11-04 00:36] falls asleep",
                      "[1518-11-04 00:46] wakes up",
                      "[1518-11-01 00:00] Guard #10 begins shift",
                      "[1518-11-05 00:45] falls asleep"]
        self.assertEqual(find_sleepiest_guard(test_input), 240)

    def test_find_sleepiest_guard_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(find_sleepiest_guard(test_input), 72925)


class TestSleepiestGuard2(unittest.TestCase):

    def test_simple_find_sleepiest_guard_2(self):
        test_input = ["[1518-11-01 00:00] Guard #10 begins shift",
                      "[1518-11-01 00:05] falls asleep",
                      "[1518-11-01 00:25] wakes up",
                      "[1518-11-01 00:30] falls asleep",
                      "[1518-11-01 00:55] wakes up",
                      "[1518-11-01 23:58] Guard #99 begins shift",
                      "[1518-11-02 00:40] falls asleep",
                      "[1518-11-02 00:50] wakes up",
                      "[1518-11-03 00:05] Guard #10 begins shift",
                      "[1518-11-03 00:24] falls asleep",
                      "[1518-11-03 00:29] wakes up",
                      "[1518-11-04 00:02] Guard #99 begins shift",
                      "[1518-11-04 00:36] falls asleep",
                      "[1518-11-04 00:46] wakes up",
                      "[1518-11-05 00:03] Guard #99 begins shift",
                      "[1518-11-05 00:45] falls asleep",
                      "[1518-11-05 00:55] wakes up"]
        self.assertEqual(find_sleepiest_guard_2(test_input), 4455)

    def test_simple_find_sleepiest_guard_2_unsorted(self):
        test_input = ["[1518-11-01 00:55] wakes up",
                      "[1518-11-01 00:25] wakes up",
                      "[1518-11-01 00:30] falls asleep",
                      "[1518-11-01 23:58] Guard #99 begins shift",
                      "[1518-11-02 00:40] falls asleep",
                      "[1518-11-03 00:05] Guard #10 begins shift",
                      "[1518-11-02 00:50] wakes up",
                      "[1518-11-03 00:29] wakes up",
                      "[1518-11-03 00:24] falls asleep",
                      "[1518-11-05 00:55] wakes up",
                      "[1518-11-01 00:05] falls asleep",
                      "[1518-11-05 00:03] Guard #99 begins shift",
                      "[1518-11-04 00:02] Guard #99 begins shift",
                      "[1518-11-04 00:36] falls asleep",
                      "[1518-11-04 00:46] wakes up",
                      "[1518-11-01 00:00] Guard #10 begins shift",
                      "[1518-11-05 00:45] falls asleep"]
        self.assertEqual(find_sleepiest_guard_2(test_input), 4455)

    def test_find_sleepiest_guard_2_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(find_sleepiest_guard_2(test_input), -1)
