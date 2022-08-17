#!/usr/bin/env python3
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_indexes = {}
        str_len = len(s)

        # Store in dictionary the positions of the characters.
        # If it is repeated sum the length of the string to
        # make the it "out of bounds".
        for cursor in range(len(s)):
            if s[cursor] not in unique_indexes:
                unique_indexes[s[cursor]] = cursor
            elif unique_indexes[s[cursor]] < str_len:
                unique_indexes[s[cursor]] += str_len

        min_idx = str_len

        # Check the dictionary for the smallest index
        # smaller than the length of the word.

        # Keys are read in the same order of the word
        # as they are stored in order so the first
        # value smaller than the length of the word
        # is the first non repeated character.
        for key in unique_indexes:
            if unique_indexes[key] < min_idx:
                return unique_indexes[key]

        return -1
