#!/usr/bin/env python3
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        from math import log10

        if n <= 0:
            return False
        else:
            return (log10(n) / log10(3)) % 1 == 0
