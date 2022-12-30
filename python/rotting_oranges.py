import unittest
from typing import List


class Solution:
    @staticmethod
    def orangesRotting(grid: List[List[int]]) -> int:
        """
        You are given an m x n grid where each cell can have one of three values:

        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
        return -1.

        Example 1:
            Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
            Output: 4

        Example 2:
            Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
            Output: -1
            Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only
            happens 4-directionally.

        Example 3:
            Input: grid = [[0,2]]
            Output: 0
            Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

        Constraints:
            m == grid.length
            n == grid[i].length
            1 <= m, n <= 10
            grid[i][j] is 0, 1, or 2.
        """
        m, n = len(grid), len(grid[0])
        differences = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        TEST_BORDER = lambda _, __: m > _ >= 0 and n > __ >= 0 and grid[_][__] == 1
        fresh_oranges = 0

        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        result = 0
        while queue:
            for _ in range(len(queue)):
                y, x = queue.pop(0)
                for dy, dx in differences:
                    ny, nx = y + dy, x + dx
                    if TEST_BORDER(ny, nx):
                        queue.append((ny, nx))
                        grid[ny][nx] = 2
                        fresh_oranges -= 1
            if queue:
                result += 1

        return -1 if fresh_oranges else result


class RottingOranges(unittest.TestCase):
    def test_case_1(self):
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected_result = 4
        self.assertEqual(expected_result, Solution.orangesRotting(grid))

    def test_case_2(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected_result = -1
        self.assertEqual(expected_result, Solution.orangesRotting(grid))

    def test_case_3(self):
        grid = [[0, 2]]
        expected_result = 0
        self.assertEqual(expected_result, Solution.orangesRotting(grid))
