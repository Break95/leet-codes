#!/usr/bin/env python3
# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters from magazine
# and false otherwise.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        # Check if we have enoough letters for the ransom note.
        len_ran = len(ransomNote)
        len_mag = len(magazine)

        if len_ran > len_mag:
            return False

        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)

        for k in ransomNote:
            if k not in magazine:
                return False
            else:
                if ransomNote[k] > magazine[k]:
                    return False
        return True
