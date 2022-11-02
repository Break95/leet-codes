#!/usr/bin/env python3
#
# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import deque

        previous = {start}
        start = deque([[start, 0]])
        mutations = -1

        while start:
            tmp, mutations = start.popleft()

            if tmp == end:
                return mutations

            for gene in bank:
                # Check gene mutation count
                dist = 0
                for i in range(8):
                    if tmp[i] != gene[i]:
                        dist += 1

                if dist == 1 and gene not in previous:
                    previous.add(gene)
                    start.append([gene, mutations + 1])

        return -1
