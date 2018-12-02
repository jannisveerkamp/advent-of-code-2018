import unittest

from .checksum import checksum
from common.file import read_file_lines


class TestChecksum(unittest.TestCase):

    def test_simple_checksum(self):
        test_input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
        self.assertEqual(checksum(test_input), 12)

    def test_checksum_input(self):
        test_input = read_file_lines(__file__, "input.txt")
        self.assertEqual(checksum(test_input), 6944)
