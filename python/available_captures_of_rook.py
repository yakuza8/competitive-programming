import unittest
from typing import List


class Solution:

    @staticmethod
    def numRookCaptures(board: List[List[str]]) -> int:
        def check(position: int, static_position: int, is_row: bool, forward: bool, board: List[List[str]]):
            for i in (range(static_position + 1, 8) if forward else range(static_position - 1, -1, -1)):
                cell = board[i][position] if is_row else board[position][i]
                if cell == 'B':
                    return 0
                elif cell == 'p':
                    return 1
            return 0

        row, column = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row, column = i, j

        return check(row, column, False, False, board) + check(row, column, False, True, board) + \
               check(column, row, True, False, board) + check(column, row, True, True, board)


class NumberRookCaptures(unittest.TestCase):

    def test_case_1(self):
        board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
        expected_output = 3
        self.assertEqual(expected_output, Solution.numRookCaptures(board))

    def test_case_2(self):
        board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                 [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                 [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
        expected_output = 0
        self.assertEqual(expected_output, Solution.numRookCaptures(board))

    def test_case_3(self):
        board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                 [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                 [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
        expected_output = 3
        self.assertEqual(expected_output, Solution.numRookCaptures(board))

    def test_case_4(self):
        board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", "B", "B", "B", "B", "B", "."],
                 [".", "p", "B", "p", "p", "p", "B", "p"], [".", "p", "B", "p", "R", "p", "B", "p"],
                 [".", "p", "B", "p", "p", "p", "B", "p"], [".", ".", "B", "B", "B", "B", "B", "."],
                 [".", ".", ".", "p", "p", "p", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
        expected_output = 4
        self.assertEqual(expected_output, Solution.numRookCaptures(board))
