"""Libray to convert between roman and arabic numbers"""

roman_numerals = [
    ("M", 1000), ("CM", 900),
    ("D", 500), ("CD", 400),
    ("C", 100), ("XC", 90),
    ("L", 50), ("XL", 40),
    ("X", 10), ("IX", 9),
    ("V", 5), ("IV", 4),
    ("I", 1)
]


def find_next_numeral(arabic):
    "Finds the next numeral and the corresponding arabic value"
    for numeral, value in roman_numerals:
        if arabic >= value:
            return numeral, value
    return "", 0


def to_roman(arabic):
    "Converts from arabic numbers to roman numbers. Casts floats to int."
    roman = ""
    arabic = int(arabic)

    while arabic > 0:
        next_numeral, subtractor = find_next_numeral(arabic)
        roman += next_numeral
        arabic -= subtractor

    return roman
