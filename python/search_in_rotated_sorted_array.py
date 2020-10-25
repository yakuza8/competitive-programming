import unittest
from typing import List


class Solution:

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
        You are given a target value to search. If found in the array return its index, otherwise return -1.
        You may assume no duplicate exists in the array.
        Your algorithm's runtime complexity must be in the order of O(log n).

        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4

        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
        """

        def is_in_this_part(min_value, max_value, target_value):
            return (min_value < target_value < max_value) or (
                    max_value < min_value and (target_value < max_value or min_value < target_value))

        return_index = -1
        if not nums:
            return -1

        min_index, max_index = 0, len(nums) - 1
        middle_index = (min_index + max_index) // 2
        while min_index <= max_index:
            min_val, mid_val, max_val = nums[min_index], nums[middle_index], nums[max_index]
            if min_val == target:
                return min_index
            elif mid_val == target:
                return middle_index
            elif max_val == target:
                return max_index
            else:
                if is_in_this_part(min_val, mid_val, target):
                    max_index = middle_index - 1
                elif is_in_this_part(mid_val, max_val, target):
                    min_index = middle_index + 1
                else:
                    break
                middle_index = (min_index + max_index) // 2
        return return_index


class MinimumPathSum(unittest.TestCase):

    def test_case_1(self):
        nums, target = [4, 5, 6, 7, 0, 1, 2], 0
        expected_result = 4
        self.assertEqual(expected_result, Solution.search(nums, target))

    def test_case_2(self):
        nums, target = [4, 5, 6, 7, 0, 1, 2], 3
        expected_result = -1
        self.assertEqual(expected_result, Solution.search(nums, target))

    def test_case_3(self):
        nums, target = [], 5
        expected_result = -1
        self.assertEqual(expected_result, Solution.search(nums, target))

    def test_case_4(self):
        nums, target = [1, 3], 2
        expected_result = -1
        self.assertEqual(expected_result, Solution.search(nums, target))

    def test_case_5(self):
        nums, target = [1], 1
        expected_result = 0
        self.assertEqual(expected_result, Solution.search(nums, target))
