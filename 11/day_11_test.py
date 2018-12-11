import unittest

from .day_11 import day_11_task_1, power_level


class TestDay11Task1(unittest.TestCase):

    def test_day_11_task_1_simple_1(self):
        self.assertEqual(-5, power_level(122, 79, 57))

    def test_day_11_task_1_simple_2(self):
        self.assertEqual(0, power_level(217, 196, 39))

    def test_day_11_task_1_simple_3(self):
        self.assertEqual(4, power_level(101, 153, 71))

    def test_day_11_task_1__input(self):
        self.assertEqual(0, day_11_task_1(2568))
