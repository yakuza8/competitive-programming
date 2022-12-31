import unittest
from typing import List


class Solution:

    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

        You may return the answer in any order.

        Example 1:
            Input: n = 4, k = 2
            Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
            Explanation: There are 4 choose 2 = 6 total combinations.
            Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

        Example 2:
            Input: n = 1, k = 1
            Output: [[1]]
            Explanation: There is 1 choose 1 = 1 total combination.

        Constraints:
            1 <= n <= 20
            1 <= k <= n
        """
        result = []

        def helper(accumulator, n, k, i):
            if len(accumulator) == k:
                result.append(accumulator)
                return

            for _ in range(i, n + 1):
                print()
                accumulator.append(_)
                helper(accumulator[:], n, k, _ + 1)
                accumulator.pop()
                print()

        helper([], n, k, 1)
        return result


class Combination(unittest.TestCase):

    def test_case_1(self):
        n, k = 4, 2
        expected_result = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertListEqual(expected_result, Solution.combine(n, k))

    def test_case_2(self):
        n, k = 1, 1
        expected_result = [[1]]
        self.assertEqual(expected_result, Solution.combine(n, k))
