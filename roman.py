"""Libray to convert between roman and arabic numbers"""

roman_numbers = {"I":1, "V":5, "X":10, }

def to_roman(arabic):
    if arabic <= 3:
        return arabic * "I"
    else:
        return "IV"