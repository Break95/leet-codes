#!/usr/bin/env python3
# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        possible = deque([start + arr[start], start-arr[start]])
        arr_size = len(arr)

        while possible:
            start = possible.popleft()

            # If we can jump within the limits of the array
            # and have not visited the element.
            if 0 <= start and start < arr_size and arr[start] >= 0:

                # Check if values is 0
                if arr[start] == 0:
                    return True

                # Jump and add new possible positions.
                possible.appendleft(start + arr[start])
                possible.append(start - arr[start])

                 # Mark element as visited.
                arr[start]= -arr[start]

        return False
