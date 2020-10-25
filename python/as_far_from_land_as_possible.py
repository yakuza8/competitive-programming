import unittest
from typing import List


class Solution:

    @staticmethod
    def maxDistance(grid: List[List[int]]) -> int:
        """
        Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water
        cell such that its distance to the nearest land cell is maximized and return the distance. The distance used in
        this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1)
        is |x0 - x1| + |y0 - y1|. If no land or water exists in the grid, return -1.

        Example 1:
        Input: [[1,0,1],[0,0,0],[1,0,1]]
        Output: 2
        Explanation:
        The cell (1, 1) is as far as possible from all the land with distance 2.

        Example 2:
        Input: [[1,0,0],[0,0,0],[0,0,0]]
        Output: 4
        Explanation:
        The cell (2, 2) is as far as possible from all the land with distance 4.

        Note:
            1 <= grid.length == grid[0].length <= 100
            grid[i][j] is 0 or 1

        Runtime: 556 ms, faster than 87.70% of Python3 online submissions for As Far from Land as Possible.
        Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for As Far from Land as Possible.
        """
        from collections import deque

        grid_row_length = len(grid)
        grid_column_length = len(grid[0])
        queue = deque([(r, c) for c in range(grid_column_length) for r in range(grid_row_length) if grid[r][c] == 1])

        distance = -1

        if len(queue) != grid_column_length * grid_row_length:
            positions_to_move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                for node in range(len(queue)):
                    r, c = queue.popleft()
                    for dy, dx in positions_to_move:
                        cy, cx = r + dy, c + dx
                        if 0 <= cy < grid_row_length and 0 <= cx < grid_column_length and grid[cy][cx] == 0:
                            grid[cy][cx] = 1
                            queue.append((cy, cx))
                distance += 1
        return distance


class AsFarFromLandAsPossible(unittest.TestCase):

    def test_case_1(self):
        grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        expected_output = 2
        self.assertEqual(expected_output, Solution.maxDistance(grid))

    def test_case_2(self):
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_output = 4
        self.assertEqual(expected_output, Solution.maxDistance(grid))
