import unittest
from typing import List


class Solution:

    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        """
        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the
        product of all the elements of nums except nums[i].

        Example:
        Input:  [1,2,3,4]
        Output: [24,12,8,6]

        Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the
         whole array) fits in a 32 bit integer.
        Note: Please solve it without division and in O(n).

        Follow up:
        Could you solve it with constant space complexity? (The output array does not count as extra space for the
        purpose of space complexity analysis.)
        """
        output_array = [1 for _ in nums]

        for index in range(1, len(nums)):
            output_array[index] = nums[index - 1] * output_array[index - 1]

        acc = 1
        for index in range(len(nums) - 1, -1, -1):
            output_array[index] = acc * output_array[index]
            acc *= nums[index]
        return output_array


class ProductOfArrayExceptSelf(unittest.TestCase):

    def test_case_1(self):
        nums = [1, 2, 3, 4]
        expected_result = [24, 12, 8, 6]
        self.assertListEqual(expected_result, Solution.productExceptSelf(nums))
