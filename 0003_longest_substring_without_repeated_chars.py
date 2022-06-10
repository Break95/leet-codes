#!/usr/bin/env python3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        longest_s = 0
        start = 0

        for char in s:
            # Found a repeteated char
            if char in substring:
                # Check if we are bigger than previous.
                longest_s = max(longest_s, len(substring))

                # Remove elements preceding repeated char
                limit = s.index(char, start)
                while start <= limit:
                    substring.discard(s[start])
                    start += 1

            substring.add(char)

        return max(longest_s, len(substring))
