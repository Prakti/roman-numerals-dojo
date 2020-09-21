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

legal_tuples = ["CM", "CD", "XC", "XL", "IX", "IV"]
for num_a, val_a in roman_numerals_dict.items():
    legal_tuples += [num_a + num_b for num_b, val_b in
                     roman_numerals_dict.items() if val_a >= val_b]

illegal_triples = ["IIX", "IXI", "IIV"]
illegal_tuples = []

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
    if len(roman)==0:
        return 0
    num = roman[0]
    if num in roman_numerals_dict:
        arabic_numeral = roman_numerals_dict[num]
    else:
        raise NotARomanNumber

    if firstbutlast + last + num in illegal_triples or last + num in illegal_tuples:
        raise NotARomanNumber

    subtractor = 0
    if last + num in ["CM","CD", "XC", "XL", "IX", "IV"]:
        subtractor = 2 * roman_numerals_dict[last]

    return arabic_numeral - subtractor + to_arabic(roman[1:], num, last)


class NotARomanNumber(Exception):
    pass
