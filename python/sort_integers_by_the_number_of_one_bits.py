import unittest
from typing import List


class Solution:
    @staticmethod
    def sortByBits(arr: List[int]) -> List[int]:
        """
        You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in
        their binary representation and in case of two or more integers have the same number of 1's you have to sort
        them in ascending order.

        Return the array after sorting it.

        Example 1:
            Input: arr = [0,1,2,3,4,5,6,7,8]
            Output: [0,1,2,4,8,3,5,6,7]

        Explanation:
        [0] is the only integer with 0 bits.
        [1,2,4,8] all have 1 bit.
        [3,5,6] have 2 bits.
        [7] has 3 bits.
        The sorted array by bits is [0,1,2,4,8,3,5,6,7]

        Example 2:
            Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
            Output: [1,2,4,8,16,32,64,128,256,512,1024]

        Explanation: All integers have 1 bit in the binary representation, you should just sort them in ascending order.


        Constraints:
            1 <= arr.length <= 500
            0 <= arr[i] <= 104
        """
        nums = [(bin(i).count('1'), i)for i in arr]
        nums = sorted(nums)
        return [_[1] for _ in nums]


class SortIntegersByTheNumberOfOneBits(unittest.TestCase):

    def test_case_1(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_result = [0, 1, 2, 4, 8, 3, 5, 6, 7]
        self.assertListEqual(expected_result, Solution.sortByBits(arr))

    def test_case_2(self):
        arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
        expected_result = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.assertListEqual(expected_result, Solution.sortByBits(arr))
