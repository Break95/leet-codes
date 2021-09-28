#!/usr/bin/env python3
# 922. Sort array by parity II. https://leetcode.com/problems/sort-array-by-parity-ii/
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1

        for index in range(0, len(nums), 2):
            if nums[index] % 2 == 0:
                continue

            for odd_i in range(odd, len(nums), 2):
                # Swap
                if nums[odd_i] % 2 == 0:
                    tmp = nums[index]
                    nums[index] = nums[odd_i]
                    nums[odd_i] = tmp

                    odd = odd_i
                    if odd == len(nums):
                        return nums
                    break

        return nums
