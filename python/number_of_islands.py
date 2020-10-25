import unittest
from typing import List


class Solution:

    @staticmethod
    def numIslands(grid: List[List[str]]) -> int:
        """
        Given a 2d grid map of ','1','s (land) and ','0','s (water), count the number of islands. An island is surrounded by
        water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of
        the grid are all surrounded by water.

        Example '1':
        Input:
        [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        Output: '1'

        Example 2:
        Input:
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        Output: 3
        """
        from collections import deque

        islands = 0

        if not grid:
            return islands

        queue = deque([])
        steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row_length, column_length = len(grid), len(grid[0])

        for row_index, row in enumerate(grid):
            while '1' in row:
                # Increment islands
                islands += 1
                queue.append((row.index('1'), row_index))

                while queue:
                    for i in range(len(queue)):
                        x, y = queue.popleft()
                        grid[y][x] = '0'
                        for dx, dy in steps:
                            cx, cy = x + dx, y + dy
                            if 0 <= cx < column_length and 0 <= cy < row_length and grid[cy][cx] == '1':
                                grid[cy][cx] = '0'
                                queue.append((cx, cy))
        return islands


class NumberOfIslands(unittest.TestCase):

    def test_case_1(self):
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        expected_result = 1
        self.assertEqual(expected_result, Solution.numIslands(grid))

    def test_case_2(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        expected_result = 3
        self.assertEqual(expected_result, Solution.numIslands(grid))

    def test_case_3(self):
        grid = []
        expected_result = 0
        self.assertEqual(expected_result, Solution.numIslands(grid))

    def test_case_4(self):
        grid = [[]]
        expected_result = 0
        self.assertEqual(expected_result, Solution.numIslands(grid))
