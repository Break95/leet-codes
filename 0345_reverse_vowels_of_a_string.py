#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        st = 0
        end = len(s) - 1
        s = list(s) # Convert to list for faster swapping.

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        w_len = len(s) -1


        while st < end:
            # Search for vowels
            while s[st] not in vowels:
                st += 1
                if st >= w_len:
                    break

            while s[end] not in vowels:
                end -= 1
                if end <= 0:
                    break

            if st >= end:
                break

            s[st], s[end] = s[end], s[st]

            end -= 1
            st += 1

        return ''.join(s)
