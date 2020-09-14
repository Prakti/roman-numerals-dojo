import unittest
import roman

class TestRomanNumerals(unittest.TestCase):

    def test_arabic_1_to_roman_I(self):
        self.assertEqual(roman.to_roman(1), "I")

    def test_arabic_3_to_roman_III(self):
        self.assertEqual(roman.to_roman(3), "III")

    def test_arabic_4_to_roman_IV(self):
        self.assertEqual(roman.to_roman(4), "IV")

    def test_arabic_8_to_roman_VIII(self):
        self.assertEqual(roman.to_roman(8), "VIII")


if __name__ == '__main__':
    unittest.main()