import unittest
from typing import List


class Solution:

    @staticmethod
    def moveZeroes(nums: List[int]) -> None:
        """
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
        the non-zero elements.

        Example:
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Note:
            You must do this in-place without making a copy of the array.
            Minimize the total number of operations.

        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        zero_indexes = deque()

        for i in range(len(nums)):
            current_number = nums[i]

            if current_number == 0:
                zero_indexes.append(i)
            else:
                if len(zero_indexes) != 0:
                    zero_index = zero_indexes.popleft()
                    nums[zero_index] = current_number
                    nums[i] = 0
                    zero_indexes.append(i)


class MoveZeroes(unittest.TestCase):

    def test_case_1(self):
        nums = [0, 1, 0, 3, 12]
        expected_result = [1, 3, 12, 0, 0]
        Solution.moveZeroes(nums)
        self.assertListEqual(expected_result, nums)
