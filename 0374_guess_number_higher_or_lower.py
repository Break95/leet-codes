#!/usr/bin/env python3
# https://leetcode.com/problems/guess-number-higher-or-lower/


class Solution:
    def guessNumber(self, n: int) -> int:
        max_val = n
        min_val = 1

        mid = (max_val - min_val)//2

        while True:
            pick = guess(mid)

            if pick == 0:
                break
            if pick == 1:
                min_val = mid + 1
            else:
                max_val = mid - 1

            mid = (max_val+min_val)//2

        return mid
