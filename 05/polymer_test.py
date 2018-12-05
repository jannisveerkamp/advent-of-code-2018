import unittest

from common.file import read_file
from .polymer import reduce_polymer, should_remove_characters


class TestPolymerReduce(unittest.TestCase):

    def test_should_remove_characters(self):
        self.assertEqual(should_remove_characters('a', 'A'), True)
        self.assertEqual(should_remove_characters('b', 'B'), True)
        self.assertEqual(should_remove_characters('a', 'a'), False)
        self.assertEqual(should_remove_characters('A', 'A'), False)
        self.assertEqual(should_remove_characters('A', 'a'), True)
        self.assertEqual(should_remove_characters('a', 'b'), False)
        self.assertEqual(should_remove_characters('a', 'B'), False)
        self.assertEqual(should_remove_characters('A', 'b'), False)
        self.assertEqual(should_remove_characters('A', 'B'), False)

    def test_simple_reduce_polymer_1(self):
        test_input = "aA"
        self.assertEqual(reduce_polymer(test_input), 0)

    def test_simple_reduce_polymer_2(self):
        test_input = "abBA"
        self.assertEqual(reduce_polymer(test_input), 0)

    def test_simple_reduce_polymer_3(self):
        test_input = "abAB"
        self.assertEqual(reduce_polymer(test_input), 4)

    def test_simple_reduce_polymer_4(self):
        test_input = "aabAAB"
        self.assertEqual(reduce_polymer(test_input), 6)

    def test_simple_reduce_polymer_4(self):
        test_input = "dabAcCaCBAcCcaDA"
        self.assertEqual(reduce_polymer(test_input), 10)

    def test_reduce_polymer_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(reduce_polymer(test_input), 11754)
