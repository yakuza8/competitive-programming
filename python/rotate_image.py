import unittest
from typing import List


class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
        (clockwise).

        You have to rotate the image in-place, which means you have to modify the input 2D matrix
        directly. DO NOT allocate another 2D matrix and do the rotation.

        Example 1:
            Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
            Output: [[7,4,1],[8,5,2],[9,6,3]]

        Example 2:
            Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
            Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

        Example 3:
            Input: matrix = [[1]]
            Output: [[1]]

        Example 4:
            Input: matrix = [[1,2],[3,4]]
            Output: [[3,1],[4,2]]

        Constraints:
            matrix.length == n
            matrix[i].length == n
            1 <= n <= 20
            -1000 <= matrix[i][j] <= 1000
        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[i][j]
                matrix[i][j] = temp


class RotateImage(unittest.TestCase):

    def test_case_1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        Solution.rotate(matrix=matrix)
        self.assertEqual(expected_result, matrix)

    def test_case_2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected_result = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        Solution.rotate(matrix=matrix)
        self.assertEqual(expected_result, matrix)

    def test_case_3(self):
        matrix = [[1]]
        expected_result = [[1]]
        Solution.rotate(matrix=matrix)
        self.assertEqual(expected_result, matrix)

    def test_case_4(self):
        matrix = [[1, 2], [3, 4]]
        expected_result = [[3, 1], [4, 2]]
        Solution.rotate(matrix=matrix)
        self.assertEqual(expected_result, matrix)
