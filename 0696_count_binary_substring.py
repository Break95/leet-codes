#!/usr/bin/env python3
# Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        groups = []
        counter = 1
        current_char = s[0]
        total = 0

        for i in range(1, len(s)):
            if current_char != s[i]:
                groups.append(counter)
                current_char = s[i]
                counter = 0
            counter += 1

        groups.append(counter)

        for i in range(len(groups)-1):
            total += min(groups[i], groups[i+1])

        return total
