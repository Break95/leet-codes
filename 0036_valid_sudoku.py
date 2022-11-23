#!/usr/bin/env python3
# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for i in range(9)]

        for i in range(9):
            # As we read the board by rows we only need one row
            # and 3 'sub-boxes' in memory at any point in time.

            if i%3 == 0:
                squares = [[] for i in range(3)]

            row = []

            for j in range(9):
                if board[i][j] == '.':
                    continue

                # Rows
                if board[i][j] not in row:
                    row.append(board[i][j])
                else:
                    return False

                # Cols
                if board[i][j] not in cols[j]:
                    cols[j].append(board[i][j])
                else:
                    return False

                # Sub-boxes
                if j < 3:
                    if board[i][j] not in squares[0]:
                        squares[0].append(board[i][j])
                    else:
                        return False
                elif j < 6:
                    if board[i][j] not in squares[1]:
                        squares[1].append(board[i][j])
                    else:
                        return False
                else:
                    if board[i][j] not in squares[2]:
                        squares[2].append(board[i][j])
                    else:
                        return False

        return True
