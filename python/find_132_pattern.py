import unittest
from typing import List


class Solution:

    @staticmethod
    def find132pattern(nums: List[int]) -> bool:
        """
         Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k
         and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132
         pattern in the list.

        Note: n will be less than 15,000.

        Example 1:
        Input: [1, 2, 3, 4]
        Output: False
        Explanation: There is no 132 pattern in the sequence.

        Example 2:
        Input: [3, 1, 4, 2]
        Output: True
        Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

        Example 3:
        Input: [-1, 3, 2, 0]
        Output: True
        Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
        """
        collection_length = len(nums)

        if collection_length < 3:
            return False

        min_from_left = []
        left_min = nums[0]

        stack = []

        for i in range(collection_length):
            left_current = nums[i]
            if left_current < left_min:
                left_min = left_current
            min_from_left.append(left_min)

        for j in range(len(nums) - 1, 0, -1):
            while stack and stack[-1] < nums[j]:
                if stack[-1] > min_from_left[j - 1]:
                    return True
                stack.pop()
            stack.append(nums[j])

        return False


class Find132Pattern(unittest.TestCase):

    def test_case_1(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(Solution.find132pattern(nums))

    def test_case_2(self):
        nums = [3, 1, 4, 2]
        self.assertTrue(Solution.find132pattern(nums))

    def test_case_3(self):
        nums = [-1, 3, 2, 0]
        self.assertTrue(Solution.find132pattern(nums))

    def test_case_4(self):
        nums = [3, 5, 0, 3, 4]
        self.assertTrue(Solution.find132pattern(nums))

    def test_case_5(self):
        nums = [2, 4, 3, 1]
        self.assertTrue(Solution.find132pattern(nums))

    def test_case_6(self):
        nums = [-2, 1, 2, -2, 1, 2]
        self.assertTrue(Solution.find132pattern(nums))
