#!/usr/bin/env python3
# NOTE: We could improve the performace by advancing the
# balls at the same time instead of one ball at a time
# due to data locality when checking the matrix for boards.

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        exits = []
        rows = len(grid)
        cols = len(grid[0])

        for j in range(cols):
            exit = j

            for i in range(rows):
                board = grid[i][exit]

                # Check right board
                if board == 1:
                    # Out of bounds check.
                    if exit + 1 >= cols:
                        exit = -1
                        break

                    # Check if we can advance
                    if grid[i][exit+1] == -1:
                        exit = -1
                        break

                    # Update ball position.
                    exit += 1

                # Check left board
                else:

                    # Out of bounds check.
                    if exit - 1 < 0:
                        exit = -1
                        break

                    # Check if we can advance
                    if grid[i][exit-1] == 1:
                        exit = -1
                        break

                    # Update ball position.
                    exit -= 1

            exits.append(exit)

        return exits
