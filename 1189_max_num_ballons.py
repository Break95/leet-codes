#!/usr/bin/env python3
# 1189. Max Number of Ballons.
# Memory efficient.
# https://leetcode.com/problems/maximum-number-of-balloons/
import math

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        result = 10**4 + 1

        counter = {'b': 0,
                   'a': 0,
                   'l': 0,
                   'o': 0,
                   'n': 0}

        for char in text:
            if char in counter:
                counter[char] += 1

        counter['l'] = int(math.floor(counter['l']/2))
        counter['o'] = int(math.floor(counter['o']/2))

        for key in counter.keys():
            if counter[key] < result:
                result = counter[key]

        return result
