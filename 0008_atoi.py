#!/usr/bin/env python3
# String to Integer
# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        index = 0
        negative = False
        numeric_strs = [str(x) for x in range(0,10)]
        signs = ['-', '+']

        # Move leading whitespaces.
        while index < len(s) and s[index] == ' ':
            index += 1

        # Now index is at a non whitespace position.
        # Check if it it '-', '+', or a number.
        if index >= len(s) or s[index] not in numeric_strs + signs:
            return number

        # Check if we are at a sign.
        if s[index] == '-':
            negative = True
            index +=1
        elif s[index] == '+':
            index += 1

        # Parse the numbers.
        while index < len(s) and s[index] in numeric_strs:
            number = number * 10 + int(s[index])
            index += 1

        # Edge case '-' followed by non numeric character or zero.
        if number == 0:
            return 0

        if negative:
            number *= -1

        # Edge cases out of bounds.
        if number > (2**31 - 1):
            return 2**31 - 1

        if number < (-2**31):
            return -2**31

        # Base case
        return number
