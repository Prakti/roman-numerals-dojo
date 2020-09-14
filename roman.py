"""Libray to convert between roman and arabic numbers"""

roman_numbers = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1, "":0}
next_subtractable_roman = {"M":"C","D":"C","C":"X","L":"X","X":"I","V":"I","I":""}


def get_next_part(arabic):
    roman = ""
    sum = 0

    for roman_part,arabic_part in roman_numbers.items():
        next_subtractable = next_subtractable_roman[roman_part]            
        next_subtractable_arabic = roman_numbers[next_subtractable]
        if arabic >= arabic_part - next_subtractable_arabic:
            if arabic < arabic_part:
                sum -= next_subtractable_arabic
                roman += next_subtractable   
            sum += arabic_part    
            roman += roman_part
            return roman, sum


def to_roman(arabic):
    roman = ""
    while arabic > 0:
        roman_part, arabic_part = get_next_part(arabic)
        arabic -= arabic_part
        roman += roman_part
    return roman


if __name__ == "__main__":
    print(to_roman(1))
