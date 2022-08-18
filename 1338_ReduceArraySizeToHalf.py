#!/usr/bin/env python3
#
# 1338. Reduce Array Size to The Half
# You are given an integer array arr. You can choose a set of integers and remove
# all the occurrences of these integers in the array. Return the minimum size of
# the set so that at least half of the integers of the array are removed.

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        max_size = len(arr)
        target_size = max_size /2
        dict_count = {}
        max_word = (0,'')

        # Count the ocurrencies of each number.
        for elem in arr:
            if elem in dict_count:
                dict_count[elem] += 1
            else:
                dict_count[elem] = 1

        # Create a list with the sorted (descending) values of the
        # dictionary.
        sorted_list = [v for _,v in sorted(dict_count.items(),
                                             key=lambda item: item[1],
                                             reverse=True)]

        # Determine the smallest set size.
        out = 0
        while max_size > target_size:
            max_size -= sorted_list[out]
            out += 1

        return out
