#!/usr/bin/env python3
# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x', 'y', 'z']

        # Compute Actual Shift
        for elem in range(len(shifts) -1, 0, -1):
            tmp = (shifts[elem - 1] + shifts[elem]) % 26 # Modulo 26 to avoid unnecessary loops.

            if (tmp == 0):
                next

            if(tmp + alphabet.index(s[elem - 1]) > 25): # If out-of-bounds
                shifts[elem-1] = tmp
                s[elem-1] = alphabet[tmp + alphabet.index(s[elem - 1]) - 26]
            else:
                shifts[elem-1] = tmp
                s[elem-1] = alphabet[tmp + alphabet.index(s[elem - 1])]

        # Last case.
        i = len(s) - 1
        tmp = (shifts[i] + alphabet.index(s[i])) % 26
        if(tmp > 25):
            s[i] = alphabet[tmp - 26]
        else:
            s[i] = alphabet[tmp]

        return ''.join(s)
