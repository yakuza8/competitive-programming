import unittest
from typing import List


class Solution:
    @staticmethod
    def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell. The distance between two
        adjacent cells is 1.

        Example 1:
            Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
            Output: [[0,0,0],[0,1,0],[0,0,0]]

        Example 2:
            Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
            Output: [[0,0,0],[0,1,0],[1,2,1]]

        Constraints:
            m == mat.length
            n == mat[i].length
            1 <= m, n <= 104
            1 <= m * n <= 104
            mat[i][j] is either 0 or 1.
            There is at least one 0 in mat.
        """
        MAX = 10 ** 10
        differences = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m, n = len(mat), len(mat[0])
        result = [[MAX for j in range(n)] for i in range(m)]
        TEST_BORDER = lambda _, __: m > _ >= 0 and n > __ >= 0

        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))

        distance = 1
        while queue:
            for _ in range(len(queue)):
                y, x = queue.pop(0)
                for dy, dx in differences:
                    ny, nx = y + dy, x + dx
                    if TEST_BORDER(ny, nx) and result[ny][nx] > distance:
                        queue.append((ny, nx))
                        result[ny][nx] = distance
            distance += 1

        return result


class ZeroOneMatrix(unittest.TestCase):
    def test_case_1(self):
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected_result = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertListEqual(expected_result, Solution.updateMatrix(mat))

    def test_case_2(self):
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected_result = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        self.assertListEqual(expected_result, Solution.updateMatrix(mat))
