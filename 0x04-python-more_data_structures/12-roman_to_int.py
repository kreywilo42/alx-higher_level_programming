#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    for a in range(len(roman_string)):
        if a > 0 and romans[roman_string[a]] > romans[roman_string[a - 1]]:
            roman_number += romans[roman_string[a]] - 2 * \
                    romans[roman_string[a - 1]]
        else:
            roman_number += romans[roman_string[a]]
    return roman_number
