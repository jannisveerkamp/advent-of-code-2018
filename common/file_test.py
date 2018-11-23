import unittest

from .file import read_file, read_file_lines, write_file, write_file_lines, delete_file


class TestFileOperations(unittest.TestCase):

    def test_read_file(self):
        text = read_file(__file__, "input.txt")
        self.assertEqual(text, "line1 1\nline2 2")

    def test_read_file_lines(self):
        text = read_file_lines(__file__, "input.txt")
        self.assertEqual(text, ["line1 1", "line2 2"])

    def test_write_file(self):
        text = "line1 a\nline2 b"
        filename = "output.txt"

        write_file(__file__, filename, text)
        parsed = read_file(__file__, filename)
        delete_file(__file__, filename)

        self.assertEqual(parsed, text)

    def test_write_file_lines(self):
        text = ["line1 a", "line2 b"]
        filename = "output.txt"

        write_file_lines(__file__, filename, text)
        parsed = read_file_lines(__file__, filename)
        delete_file(__file__, filename)

        self.assertEqual(parsed, text)
