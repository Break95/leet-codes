#!/usr/bin/env python3
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = 0
        missing = defaultdict(int)

        for word in words:
            if word[::-1] not in missing:
                missing[word] += 1
            else:
                if missing[word[::-1]] > 0:
                    missing[word[::-1]] -= 1
                    pairs += 1
                else:
                    missing[word] += 1

        # Check for self mirror 'word'
        same = 0
        for word in missing.keys():
            if missing[word] > 0 and word[0] == word[1]:
                same = 1
                break

        return (2 * pairs  + same) * 2
