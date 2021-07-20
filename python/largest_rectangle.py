import unittest
from typing import List


class Solution:

    @staticmethod
    def largest_rectangle(h: List[int]) -> int:
        positions, heights = [], []
        max_height, hist_length = 0, len(h)
        for index, height in enumerate(h):
            if not heights or height > heights[-1]:
                positions.append(index)
                heights.append(height)
            else:
                new_position, new_height = None, None
                while heights and height < heights[-1]:
                    new_position, new_height = positions.pop(), heights.pop()
                    max_height = max(max_height, new_height * (index - new_position))
                if new_height:
                    positions.append(new_position)
                    heights.append(height)
        for rest in range(len(heights)):
            position, height = positions.pop(), heights.pop()
            max_height = max(max_height, height * (hist_length - position))
        return max_height


class LargestRectangle(unittest.TestCase):

    def test_case_1(self):
        h = [1, 2, 3, 4, 5]
        expected_output = 9
        self.assertEqual(expected_output, Solution.largest_rectangle(h))

    def test_case_2(self):
        h = [1, 3, 2, 1, 2]
        expected_output = 5
        self.assertEqual(expected_output, Solution.largest_rectangle(h))

    def test_case_3(self):
        h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
        expected_output = 26152
        self.assertEqual(expected_output, Solution.largest_rectangle(h))
