#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    total = 0
    prev = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = [roman[x] for x in roman_string]
    for x in integer:
        if x > prev:
            total -= prev * 2
        prev = x
        total += x
    return total
