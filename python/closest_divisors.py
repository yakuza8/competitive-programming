import unittest
from typing import List, Tuple


class Solution:

    @staticmethod
    def closest_divisors(num: int) -> List[int]:
        """
        Input: num = 8
        Output: [3,3]
        Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

        Example 2:

        Input: num = 123
        Output: [5,25]

        Example 3:

        Input: num = 999
        Output: [40,25]

        Runtime: 192 ms, faster than 72.44% of Python3 online submissions for Closest Divisors.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Closest Divisors.
        """
        def find_divisors(number: int) -> Tuple[int, int]:
            for i in range(int(number ** 0.5) + 1, 0, -1):
                if number % i == 0:
                    return i, number // i

        def find_most_closest_tuple(tuples: List[Tuple[int, int]]) -> List[int]:
            index = -1
            diff = 10e10

            for i, t in enumerate(tuples):
                tmp_diff = abs(t[0] - t[1])
                if tmp_diff < diff:
                    index = i
                    diff = tmp_diff

            return list(tuples[index])

        num_inc_one_divisors = find_divisors(num + 1)
        num_inc_two_divisors = find_divisors(num + 2)
        return find_most_closest_tuple([num_inc_one_divisors, num_inc_two_divisors])


class ClosestDivisorsUnittest(unittest.TestCase):

    def test_case_1(self):
        num = 8
        expected_result = [3, 3]
        self.assertListEqual(expected_result, Solution.closest_divisors(num))

    def test_case_2(self):
        num = 123
        expected_result = [5, 25]
        self.assertListEqual(expected_result, Solution.closest_divisors(num))

    def test_case_3(self):
        num = 999
        expected_result = [40, 25]
        self.assertListEqual(expected_result, Solution.closest_divisors(num))
