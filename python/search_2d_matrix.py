import unittest
from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following two properties:

        Each row is sorted in non-decreasing order. The first integer of each row is greater than the last integer of
        the previous row. Given an integer target, return true if target is in matrix or false otherwise.

        You must write a solution in O(log(m * n)) time complexity.

        Example 1:
            Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
            Output: true

        Example 2:
            Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
            Output: false

        Constraints:
            m == matrix.length
            n == matrix[i].length
            1 <= m, n <= 100
            -104 <= matrix[i][j], target <= 104
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left != right:
            middle = (left + right - 1) // 2
            m_r, m_c = middle // n, middle % n
            target_cell = matrix[m_r][m_c]

            if target_cell < target:
                left = middle + 1
            else:
                right = middle
        return matrix[right // n][right % n] == target


class Search2DMatrix(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        expected_result = True
        self.assertEqual(expected_result, Solution.searchMatrix(matrix, target))

    def test_case_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        expected_result = False
        self.assertEqual(expected_result, Solution.searchMatrix(matrix, target))

    def test_case_3(self):
        matrix = [[1]]
        target = 1
        expected_result = True
        self.assertEqual(expected_result, Solution.searchMatrix(matrix, target))

    def test_case_4(self):
        matrix = [[1]]
        target = 2
        expected_result = False
        self.assertEqual(expected_result, Solution.searchMatrix(matrix, target))

    def test_case_5(self):
        matrix = [[1, 1]]
        target = 2
        expected_result = False
        self.assertEqual(expected_result, Solution.searchMatrix(matrix, target))
