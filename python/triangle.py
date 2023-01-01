import unittest
from typing import List


class Solution:

    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        """
        Given a triangle array, return the minimum path sum from top to bottom.

        For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the
        current row, you may move to either index i or index i + 1 on the next row.

        Example 1:
            Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
            Output: 11
            Explanation: The triangle looks like:
               2
              3 4
             6 5 7
            4 1 8 3
            The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

        Example 2:
            Input: triangle = [[-10]]
            Output: -10

        Constraints:
            1 <= triangle.length <= 200
            triangle[0].length == 1
            triangle[i].length == triangle[i - 1].length + 1
            -104 <= triangle[i][j] <= 104

        Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
        """

        def collapse(layer):
            return [min(_, __) for _, __ in zip(layer[:-1:], layer[1::])]

        def sum_layers(layer1, layer2):
            return [sum(_) for _ in zip(layer1, layer2)]

        current_layer = len(triangle) - 1
        current_bottom = triangle[current_layer]

        while current_layer > 0:
            current_bottom = sum_layers(triangle[current_layer - 1], collapse(current_bottom))
            current_layer -= 1
        return current_bottom[0]


class Triangle(unittest.TestCase):

    def test_case_1(self):
        triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
        expected_result = 11
        self.assertEqual(expected_result, Solution.minimumTotal(triangle))

    def test_case_2(self):
        triangle = [[-10]]
        expected_result = -10
        self.assertEqual(expected_result, Solution.minimumTotal(triangle))
