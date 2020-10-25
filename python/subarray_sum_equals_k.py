import unittest
from typing import List


class Solution:

    @staticmethod
    def subarraySum(nums: List[int], k: int) -> int:
        """
        Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
        equals to k.

        Example 1:
        Input:nums = [1,1,1], k = 2
        Output: 2

        Note:
            The length of the array is in range [1, 20,000].
            The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
        """
        from collections import defaultdict

        # To keep track of successive sum
        sum_lookup = defaultdict(list)

        count = 0
        current_sum = 0
        for index, value in enumerate(nums):
            current_sum += value

            # Add current sum if it is looked for
            if k == current_sum:
                count += 1

            # Check difference from the current sum
            increase_amount = current_sum - k
            if increase_amount in sum_lookup:
                count += len(sum_lookup[increase_amount])

            # Update current sum list
            sum_lookup[current_sum].append(index)

        return count


class SubarraySumEqualsK(unittest.TestCase):

    def test_case_1(self):
        nums = [1, 1, 1]
        k = 2
        expected_result = 2
        self.assertEqual(expected_result, Solution.subarraySum(nums, k))

    def test_case_2(self):
        nums = [5, 1, 4, 6, 1]
        k = 5
        expected_result = 2
        self.assertEqual(expected_result, Solution.subarraySum(nums, k))

    def test_case_3(self):
        nums = [1]
        k = 0
        expected_result = 0
        self.assertEqual(expected_result, Solution.subarraySum(nums, k))
