import unittest
import roman

class TestRomanNumerals(unittest.TestCase):

    def test_arabic_1_to_roman_I(self):
        self.assertEqual(roman.to_roman(1), "I")

if __name__ == '__main__':
    unittest.main()