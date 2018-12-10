import unittest

from common.file import read_file_lines
from .day_10 import day_10


class TestDay10(unittest.TestCase):

    def test_day_10_simple(self):
        test_input = ["position=< 9,  1> velocity=< 0,  2>",
                      "position=< 7,  0> velocity=<-1,  0>",
                      "position=< 3, -2> velocity=<-1,  1>",
                      "position=< 6, 10> velocity=<-2, -1>",
                      "position=< 2, -4> velocity=< 2,  2>",
                      "position=<-6, 10> velocity=< 2, -2>",
                      "position=< 1,  8> velocity=< 1, -1>",
                      "position=< 1,  7> velocity=< 1,  0>",
                      "position=<-3, 11> velocity=< 1, -2>",
                      "position=< 7,  6> velocity=<-1, -1>",
                      "position=<-2,  3> velocity=< 1,  0>",
                      "position=<-4,  3> velocity=< 2,  0>",
                      "position=<10, -3> velocity=<-1,  1>",
                      "position=< 5, 11> velocity=< 1, -2>",
                      "position=< 4,  7> velocity=< 0, -1>",
                      "position=< 8, -2> velocity=< 0,  1>",
                      "position=<15,  0> velocity=<-2,  0>",
                      "position=< 1,  6> velocity=< 1,  0>",
                      "position=< 8,  9> velocity=< 0, -1>",
                      "position=< 3,  3> velocity=<-1,  1>",
                      "position=< 0,  5> velocity=< 0, -1>",
                      "position=<-2,  2> velocity=< 2,  0>",
                      "position=< 5, -2> velocity=< 1,  2>",
                      "position=< 1,  4> velocity=< 2,  1>",
                      "position=<-2,  7> velocity=< 2, -2>",
                      "position=< 3,  6> velocity=<-1, -1>",
                      "position=< 5,  0> velocity=< 1,  0>",
                      "position=<-6,  0> velocity=< 2,  0>",
                      "position=< 5,  9> velocity=< 1, -2>",
                      "position=<14,  7> velocity=<-2,  0>",
                      "position=<-3,  6> velocity=< 2, -1>"]
        # Prints HI
        self.assertEqual(3, day_10(test_input, 5, 0, 7))

    def test_day_10__input(self):
        # Prints GJNKBZEE
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(10727, day_10(test_input, 50, 10700, 9))
