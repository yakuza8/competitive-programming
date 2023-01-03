import unittest
from typing import List


class Solution:

    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
        sum and return its sum.

        Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.

        Follow up:
        If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
        which is more subtle.
        """
        ans = current_sum = nums[0]
        for num in nums[1::]:
            current_sum = max(num, current_sum + num)
            ans = max(ans, current_sum)
        return ans


class MaximumSubarray(unittest.TestCase):

    def test_case_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_result = 6
        self.assertEqual(expected_result, Solution.maxSubArray(nums))

    def test_case_2(self):
        nums = [-1]
        expected_result = -1
        self.assertEqual(expected_result, Solution.maxSubArray(nums))

    def test_case_3(self):
        nums = [-2, -1]
        expected_result = -1
        self.assertEqual(expected_result, Solution.maxSubArray(nums))
