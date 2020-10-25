import unittest
from typing import List


class Solution:

    @staticmethod
    def findMaxLength(nums: List[int]) -> int:
        """
        Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

        Example 1:
        Input: [0,1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

        Example 2:
        Input: [0,1,0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

        Note: The length of the given binary array will not exceed 50,000.
        """

        countering_index = {0: -1}

        max_len = 0
        current_sum = 0
        for index, element in enumerate(nums):
            if element == 0:
                current_sum -= 1
            else:
                current_sum += 1
            # If we encounter the same sum previously
            if current_sum in countering_index:
                max_len = max(max_len, index - countering_index[current_sum])
            else:
                countering_index[current_sum] = index

        return max_len


class ContiguousArray(unittest.TestCase):

    def test_case_1(self):
        nums = [0, 1]
        expected_result = 2
        self.assertEqual(expected_result, Solution.findMaxLength(nums))

    def test_case_2(self):
        nums = [0, 1, 0]
        expected_result = 2
        self.assertEqual(expected_result, Solution.findMaxLength(nums))
