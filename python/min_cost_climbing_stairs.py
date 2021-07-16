import unittest
from typing import List


class Solution:

    @staticmethod
    def minCostClimbingStairs(cost: List[int]) -> int:
        """
        On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

        Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of
        the floor, and you can either start from the step with index 0, or the step with index 1.

        Example 1:
        Input: cost = [10, 15, 20]
        Output: 15
        Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

        Example 2:
        Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        Output: 6
        Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

        Note:
            Cost will have a length in the range [2, 1000].
            Every cost[i] will be an integer in the range [0, 999].
        """

        ''' Recursive
        def helper(_cost: List[int]) -> int:
            length = len(_cost)
            if length == 0:
                return 0
            if length == 1:
                return _cost[0]
            else:
                return _cost[0] + min(helper(_cost[1:]), helper(_cost[2:]))
        return min(helper(cost), helper(cost[1:]))
        '''

        length = len(cost)
        tableau = []
        for i in range(2):
            cost.insert(0, 0)
            tableau.append(0)

        for i in range(length + 1):
            tableau.append(min(cost[i] + tableau[i], cost[i + 1] + tableau[i + 1]))
        return tableau[-1]


class MinCostClimbingStairs(unittest.TestCase):

    def test_case_1(self):
        stairs = [10, 15, 20]
        expected_output = 15
        self.assertEqual(expected_output, Solution.minCostClimbingStairs(stairs))

    def test_case_2(self):
        stairs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected_output = 6
        self.assertEqual(expected_output, Solution.minCostClimbingStairs(stairs))
