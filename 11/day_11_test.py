import unittest

from .day_11 import power_level, square_power, build_grid, day_11_task_1, day_11_task_2


class TestDay11Task1(unittest.TestCase):

    def test_day_11_power_level_1(self):
        self.assertEqual(-5, power_level(122, 79, 57))

    def test_day_11_power_level_2(self):
        self.assertEqual(0, power_level(217, 196, 39))

    def test_day_11_power_level_3(self):
        self.assertEqual(4, power_level(101, 153, 71))

    def test_day_11_square_power_1(self):
        self.assertEqual(29, square_power(33, 45, build_grid(18)))

    def test_day_11_square_power_2(self):
        self.assertEqual(30, square_power(21, 61, build_grid(42)))

    def test_day_11_task_1_simple_input_1(self):
        self.assertEqual((33, 45), day_11_task_1(18))

    def test_day_11_task_1_simple_input_2(self):
        self.assertEqual((21, 61), day_11_task_1(42))

    def test_day_11_task_1_input(self):
        self.assertEqual((21, 68), day_11_task_1(2568))


class TestDay11Task2(unittest.TestCase):

    def test_day_11_task_2_simple_input_1(self):
        self.assertEqual((90, 269, 16), day_11_task_2(18))

    def test_day_11_task_2_simple_input_2(self):
        self.assertEqual((232, 251, 12), day_11_task_2(42))

    def test_day_11_task_2_input(self):
        self.assertEqual((90, 201, 15), day_11_task_2(2568))
