import unittest
from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        """
        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

        Example 1:
        Input: [2,2,1]
        Output: 1

        Example 2:
        Input: [4,1,2,1,2]
        Output: 4
        """
        '''
        seen_nums = {}
        for num in nums:
            if num not in seen_nums:
                seen_nums[num] = True
            else:
                del seen_nums[num]
        return list(seen_nums.keys())[0]
        '''
        num = 0
        for i in nums:
            num ^= i
        return num


class SingleNumber(unittest.TestCase):

    def test_case_1(self):
        nums = [2, 2, 1]
        expected_result = 1
        self.assertEqual(expected_result, Solution.singleNumber(nums))

    def test_case_2(self):
        nums = [4, 1, 2, 1, 2]
        expected_result = 4
        self.assertEqual(expected_result, Solution.singleNumber(nums))
