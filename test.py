import unittest
import roman
import math

class TestRomanNumerals(unittest.TestCase):

    def test_arabic_1_to_roman_I(self):
        self.assertEqual(roman.to_roman(1), "I")

    def test_arabic_3_to_roman_III(self):
        self.assertEqual(roman.to_roman(3), "III")

    def test_arabic_4_to_roman_IV(self):
        self.assertEqual(roman.to_roman(4), "IV")

    def test_arabic_8_to_roman_VIII(self):
        self.assertEqual(roman.to_roman(8), "VIII")

    def test_arabic_9_to_roman_IX(self):
        self.assertEqual(roman.to_roman(9), "IX")

    def test_arabic_13_to_roman_XIII(self):
        self.assertEqual(roman.to_roman(13), "XIII")

    def test_arabic_47_to_roman_XLVII(self):
        self.assertEqual(roman.to_roman(47), "XLVII")

    def test_arabic_777_to_roman_DCCLXXVII(self):
        self.assertEqual(roman.to_roman(777), "DCCLXXVII")

    def test_arabic_1987_to_roman_MCMLXXXVII(self):
        self.assertEqual(roman.to_roman(1987), "MCMLXXXVII")

    def test_arabic_7949_to_roman_MMMMMMMCMXLIX(self):
        self.assertEqual(roman.to_roman(7949), "MMMMMMMCMXLIX")

    def test_arabic_minus_to_roman_ERROR(self):
        self.assertEqual(roman.to_roman(-10), "")

    def test_arabic_zero_to_roman_empty(self):
        self.assertEqual(roman.to_roman(0), "")

    def test_pi_to_roman_empty(self):
        self.assertEqual(roman.to_roman(math.pi), "III")


class TestGetNextPart(unittest.TestCase):
    def test_get_next_part_2000_M(self):
        self.assertEqual(roman.get_next_part(2000), ("M", 1000))


    def test_get_next_part_1_I(self):
        self.assertEqual(roman.get_next_part(1), ("I",1))


if __name__ == '__main__':
    unittest.main()