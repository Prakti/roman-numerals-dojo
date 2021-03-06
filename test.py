import unittest
import roman
import math

from roman import NotARomanNumber

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


class TestArabicNumerals(unittest.TestCase):
    def test_I_to_1(self):
        self.assertEqual(roman.to_arabic("I"), 1)

    def test_IV_to_4(self):
        self.assertEqual(roman.to_arabic("IV"), 4)

    def test_XV_to_15(self):
        self.assertEqual(roman.to_arabic("XV"), 15)

    def test_MCMLXXXXVII_to_1987(self):
        self.assertEqual(roman.to_arabic("MCMLXXXVII"), 1987)

    def test_MMMMMMMCMXLIX_to_7949(self):
        self.assertEqual(roman.to_arabic("MMMMMMMCMXLIX"), 7949)

    def test_Z_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("Z")

    def test_IZ_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("IZ")

    def test_IIX_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("IIX")

    def test_IXX_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("IXX")

    def test_MCMM_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("MCMM")

    def test_MDD_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("MDD")

    def test_MLVX_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("MLVX")

    def test_empty_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic("")

    def test_1_is_NotARomanNumber(self):
        with self.assertRaises(NotARomanNumber):
            roman.to_arabic(1)



if __name__ == '__main__':
    unittest.main()
