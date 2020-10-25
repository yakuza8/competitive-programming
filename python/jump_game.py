import unittest
from typing import List


class Solution:

    @staticmethod
    def canJump(nums: List[int]) -> bool:
        """
        Given an array of non-negative integers, you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Determine if you are able to reach the last index.

        Example 1:
        Input: [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

        Example 2:
        Input: [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum
                     jump length is 0, which makes it impossible to reach the last index.

        """
        length = len(nums)
        last_position_to_jump = length - 1

        for index in range(length - 2, -1, -1):
            jump_to_take = nums[index]
            if index + jump_to_take >= last_position_to_jump:
                last_position_to_jump = index
        return last_position_to_jump == 0


class JumpGame(unittest.TestCase):

    def test_case_1(self):
        jumps = [2, 3, 1, 1, 4]
        expected_result = True
        self.assertEqual(expected_result, Solution.canJump(jumps))

    def test_case_2(self):
        jumps = [3, 2, 1, 0, 4]
        expected_result = False
        self.assertEqual(expected_result, Solution.canJump(jumps))
