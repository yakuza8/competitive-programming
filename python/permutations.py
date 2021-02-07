import unittest
from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. You can
        return the answer in any order.

        Example 1:

        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        Example 2:

        Input: nums = [0,1]
        Output: [[0,1],[1,0]]
        Example 3:

        Input: nums = [1]
        Output: [[1]]


        Constraints:

        1 <= nums.length <= 6
        -10 <= nums[i] <= 10
        All the integers of nums are unique.
        """
        result = []
        length = len(nums)

        def helper(l, recurse_list):
            if len(recurse_list) == length:
                result.append(recurse_list)
            for num in l:
                temp_recurse = recurse_list[:]
                temp_recurse += [num]
                temp_l = l[:]
                temp_l.remove(num)
                helper(temp_l, temp_recurse)

        helper(nums, recurse_list=[])
        return result


class Permutations(unittest.TestCase):
    def test_case_1(self):
        result = Solution.permute([1, 2, 3])
        self.assertListEqual(result,
                             [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
