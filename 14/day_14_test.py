import unittest

from .day_14 import day_14_task_1


class TestDay14Task1(unittest.TestCase):

    def test_day_14_task_1_simple_1(self):
        self.assertEqual("0124515891", day_14_task_1(5))

    def test_day_14_task_1_simple_2(self):
        self.assertEqual("5158916779", day_14_task_1(9))

    def test_day_14_task_1_simple_3(self):
        self.assertEqual("9251071085", day_14_task_1(18))

    def test_day_14_task_1_simple_4(self):
        self.assertEqual("5941429882", day_14_task_1(2018))

    def test_day_14_task_1_input(self):
        self.assertEqual("6289129761", day_14_task_1(825401))
