import unittest

from common.file import read_file_lines
from .polymer import reduce_polymer


class TestPolymerReduce(unittest.TestCase):

    def test_simple_reduce_polymer_1(self):
        test_input = ["aA"]
        self.assertEqual(reduce_polymer(test_input), 0)

    def test_simple_reduce_polymer_2(self):
        test_input = ["abBA"]
        self.assertEqual(reduce_polymer(test_input), 0)

    def test_simple_reduce_polymer_3(self):
        test_input = ["abAB"]
        self.assertEqual(reduce_polymer(test_input), 4)

    def test_simple_reduce_polymer_4(self):
        test_input = ["aabAAB"]
        self.assertEqual(reduce_polymer(test_input), 6)

    def test_simple_reduce_polymer_4(self):
        test_input = ["dabAcCaCBAcCcaDA"]
        self.assertEqual(reduce_polymer(test_input), 10)

    def test_reduce_polymer_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(reduce_polymer(test_input), 0)
