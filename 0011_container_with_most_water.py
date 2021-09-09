#!/usr/bin/env python3
# Container with most water.
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        j = len(height) - 1
        i = 0

        while i < j:
            current_area = (j-i) * min(height[i], height[j])
            if (current_area > max_area):
                max_area = current_area
            if(height[i] > height[j]):
                j -= 1
            else:
                i +=1

        return max_area
