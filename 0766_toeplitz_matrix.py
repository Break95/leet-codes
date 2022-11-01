#!/usr/bin/env python3
# Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        cols = len(matrix[0])
        rows = len(matrix)

        # Top row diags
        for j in range(cols):
            tmp = matrix[0][j]

            for i in range(1, rows):
                j += 1

                if j == cols:
                    break

                if matrix[i][j] != tmp:
                    return False

        # Col diags
        for i in range(1, rows):
            tmp = matrix[i][0]

            for j in range(1, cols):
                i += 1

                if i == rows:
                    break

                if matrix[i][j] != tmp:
                    return False

        return True
