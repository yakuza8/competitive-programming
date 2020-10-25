import unittest
from typing import List


class Solution:

    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        """
        Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
        the sum of all numbers along its path.

        Note: You can only move either down or right at any point in time.

        Example:
        Input:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
        Output: 7
        Explanation: Because the path 1→3→1→1→1 minimizes the sum.
        """
        tableau = [[float('inf') for i in range(len(grid[0]) + 1)] for y in range(len(grid) + 1)]
        tableau[0][0] = tableau[0][1] = tableau[1][0] = 0

        for row_index, row in enumerate(grid):
            for column_index, column in enumerate(row):
                tableau[row_index + 1][column_index + 1] = min(tableau[row_index][column_index + 1], tableau[row_index + 1][column_index]) + column

        return int(tableau[-1][-1])


class MinimumPathSum(unittest.TestCase):

    def test_case_1(self):
        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        expected_result = 7
        self.assertEqual(expected_result, Solution.minPathSum(grid))
