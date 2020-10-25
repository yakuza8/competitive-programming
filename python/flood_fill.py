import unittest
from typing import List


class Solution:

    @staticmethod
    def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
            from collections import deque

            queue = deque()
            row_length, column_length = len(image), len(image[0])
            target_color = image[sr][sc]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            if target_color != newColor:
                queue.append((sr, sc))
            while queue:
                for pixel in range(len(queue)):
                    r, c = queue.popleft()
                    image[r][c] = newColor
                    for dy, dx in directions:
                        nr, nc = r + dy, c + dx
                        if 0 <= nr < row_length and 0 <= nc < column_length and image[nr][nc] == target_color:
                            queue.append((nr, nc))
            return image


class FloodFill(unittest.TestCase):

    def test_case_1(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        new_color = 2
        expected_output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertListEqual(expected_output, Solution.floodFill(image, sr, sc, new_color))

    def test_case_2(self):
        image = [[0, 0, 0], [0, 1, 1]]
        sr = 1
        sc = 1
        new_color = 1
        expected_output = [[0, 0, 0], [0, 1, 1]]
        self.assertListEqual(expected_output, Solution.floodFill(image, sr, sc, new_color))
