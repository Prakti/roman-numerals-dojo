"""Libray to convert between roman and arabic numbers"""

roman_numbers = {"I":1, "V":5, "X":10, }

def to_roman(arabic):
    roman = ""

    while arabic > 0:
        if arabic == 9:
            roman += "IX"
            arabic -= 9
        elif arabic >= 5:
            roman += "V"
            arabic -= 5
        elif arabic == 4:
            roman += "IV"
            arabic -= 4
        elif arabic < 4:
            roman += arabic * "I"
            arabic = 0

    return roman