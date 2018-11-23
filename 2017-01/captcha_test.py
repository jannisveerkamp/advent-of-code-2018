import unittest

from .captcha import calculate_captcha_sum, calculate_advanced_captcha_sum
from common.file import read_file


class TestCaptcha(unittest.TestCase):

    def test_calculate_captcha_sum_1122(self):
        self.assertEqual(calculate_captcha_sum("1122"), 3)

    def test_calculate_captcha_sum_1111(self):
        self.assertEqual(calculate_captcha_sum("1111"), 4)

    def test_calculate_captcha_sum_1234(self):
        self.assertEqual(calculate_captcha_sum("1234"), 0)

    def test_calculate_captcha_sum_91212129(self):
        self.assertEqual(calculate_captcha_sum("91212129"), 9)

    def test_calculate_captcha_sum_test_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(calculate_captcha_sum(test_input), 1341)


class TestCaptchaAdvanced(unittest.TestCase):

    def test_calculate_advanced_captcha_sum_1122(self):
        self.assertEqual(calculate_advanced_captcha_sum("1212"), 6)

    def test_calculate_advanced_captcha_sum_1111(self):
        self.assertEqual(calculate_advanced_captcha_sum("1221"), 0)

    def test_calculate_advanced_captcha_sum_123425(self):
        self.assertEqual(calculate_advanced_captcha_sum("123425"), 4)

    def test_calculate_advanced_captcha_sum_91212129(self):
        self.assertEqual(calculate_advanced_captcha_sum("123123"), 12)

    def test_calculate_advanced_captcha_sum_1341(self):
        self.assertEqual(calculate_advanced_captcha_sum("12131415"), 4)

    def test_calculate_captcha_sum_test_input(self):
        test_input = read_file(__file__, "input.txt")
        self.assertEqual(calculate_advanced_captcha_sum(test_input), 1348)
