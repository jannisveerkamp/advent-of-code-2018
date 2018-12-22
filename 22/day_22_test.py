import unittest

from .day_22 import day_22_task_1


class TestDay22Task1(unittest.TestCase):

    def test_day_22_task_1_simple(self):
        self.assertEqual(114, day_22_task_1(depth=510, target=(10, 10)))

    def test_day_2_task_1_input(self):
        self.assertEqual(0, day_22_task_1(depth=4845, target=(6, 770)))
