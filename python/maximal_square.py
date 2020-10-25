import unittest
from typing import List


class Solution:

    @staticmethod
    def maximalSquare(matrix: List[List[str]]) -> int:
        """
        Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

        Example:

        Input:
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0
        Output: 4
        """
        max_size = 0
        row_length = len(matrix)
        if row_length == 0:
            return max_size
        column_length = len(matrix[0])

        tableau = [[0 for _ in range(column_length + 1)] for _ in range(row_length + 1)]

        for row_index in range(row_length):
            for column_index in range(column_length):
                if matrix[row_index][column_index] == '1':
                    tableau[row_index + 1][column_index + 1] = min(
                        tableau[row_index][column_index + 1], tableau[row_index + 1][column_index],
                        tableau[row_index][column_index]
                    ) + 1
                    max_size = max(max_size, tableau[row_index + 1][column_index + 1])
        return max_size * max_size


class MaximalSquare(unittest.TestCase):

    def test_case_1(self):
        matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']
        ]
        expected_result = 4
        self.assertEqual(expected_result, Solution.maximalSquare(matrix))

    def test_case_2(self):
        matrix = [
            ["1", "0", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1", "1"]
        ]
        expected_result = 9
        self.assertEqual(expected_result, Solution.maximalSquare(matrix))
