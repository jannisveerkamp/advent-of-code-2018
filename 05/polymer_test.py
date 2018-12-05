import unittest

from common.file import read_file
from .polymer import reduce_polymer, should_remove_characters, find_all_characters, remove_unit_from_polymer


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


class TestPolymerRemoveUnit(unittest.TestCase):

    def test_find_all_characters(self):
        self.assertEqual(find_all_characters("aA"), {'a'})
        self.assertEqual(find_all_characters("aB"), {'a', 'b'})
        self.assertEqual(find_all_characters("bBaAbBcCdddcB"), {'a', 'b', 'c', 'd'})

    def test_remove_unit_from_polymer_1(self):
        test_input = "aA"
        self.assertEqual(remove_unit_from_polymer(test_input), 0)

    def test_remove_unit_from_polymer_2(self):
        test_input = "abBA"
        self.assertEqual(remove_unit_from_polymer(test_input), 0)

    def test_remove_unit_from_polymer_3(self):
        test_input = "abAB"
        self.assertEqual(remove_unit_from_polymer(test_input), 0)

    def test_remove_unit_from_polymer_4(self):
        test_input = "aabAAB"
        self.assertEqual(remove_unit_from_polymer(test_input), 0)

    def test_remove_unit_from_polymer_5(self):
        test_input = "dabAcCaCBAcCcaDA"
        self.assertEqual(remove_unit_from_polymer(test_input), 4)

    def test_remove_unit_from_polymer_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(remove_unit_from_polymer(test_input), 4098)
