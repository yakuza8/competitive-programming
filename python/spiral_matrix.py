import unittest
from typing import List


class Solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.

        Example 1:
            Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [1,2,3,6,9,8,7,4,5]

        Example 2:
            Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
            Output: [1,2,3,4,8,12,11,10,9,5,6,7]

        Constraints:
            m == matrix.length
            n == matrix[i].length
            1 <= m, n <= 10
            -100 <= matrix[i][j] <= 100
        """
        ans = []
        while matrix:
            ans.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return ans


class SpiralMatrix(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertListEqual(expected_result, Solution.spiralOrder(matrix))

    def test_case_2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected_result = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertListEqual(expected_result, Solution.spiralOrder(matrix))
