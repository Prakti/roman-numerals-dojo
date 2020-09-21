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

roman_numerals_dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

legal_tuples_smaller = []
for num_a, val_a in roman_numerals_dict.items():
    legal_tuples_smaller += [num_a + num_b for num_b, val_b in
                            roman_numerals_dict.items() if val_a > val_b]   
legal_tuples = ["CM", "CD", "XC", "XL", "IX", "IV", "MM", "CC", "XX", "II"] \
    + legal_tuples_smaller \
    + list(roman_numerals_dict.keys())

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


def to_arabic(roman, last="", firstbutlast=""):
    if type(roman) != str:
        raise NotARomanNumber
    if not roman:
        if last:
            return 0
        else:
            raise NotARomanNumber
    num = roman[0]
    if num in roman_numerals_dict:
        arabic_numeral = roman_numerals_dict[num]
    else:
        raise NotARomanNumber
    if not last + num in legal_tuples:
        raise NotARomanNumber
    if len(firstbutlast)>0 \
            and roman_numerals_dict[firstbutlast] < arabic_numeral \
            and roman_numerals_dict[last] <= arabic_numeral:
        raise NotARomanNumber

    subtractor = 0
    if last + num in ["CM","CD", "XC", "XL", "IX", "IV"]:
        subtractor = 2 * roman_numerals_dict[last]

    return arabic_numeral - subtractor + to_arabic(roman[1:], num, last)


class NotARomanNumber(Exception):
    pass
