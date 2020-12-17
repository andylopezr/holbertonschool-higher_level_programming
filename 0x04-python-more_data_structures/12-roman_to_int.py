#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        total = 0
        prev = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        numbers = [roman[x] for x in roman_string]
        for x in numbers:
            if x > prev:
                total -= prev * 2
            prev = x
            total += x
        return total
