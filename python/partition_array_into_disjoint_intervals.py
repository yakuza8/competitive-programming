import unittest
from typing import List


class Solution:
    @staticmethod
    def partitionDisjoint(A: List[int]) -> int:
        """
        Given an array A, partition it into two (contiguous) subarrays left and right so that:
        * Every element in left is less than or equal to every element in right.
        * left and right are non-empty.
        * left has the smallest possible size.

        Return the length of left after such a partitioning.  It is guaranteed that such a
        partitioning exists.

        Example 1:
            Input: [5,0,3,8,6]
            Output: 3
            Explanation: left = [5,0,3], right = [8,6]

        Example 2:
            Input: [1,1,1,0,6,12]
            Output: 4
            Explanation: left = [1,1,1,0], right = [6,12]

        Note:
            2 <= A.length <= 30000
            0 <= A[i] <= 10^6
            It is guaranteed there is at least one way to partition A as described.
        """
        if len(A) == 2:
            return 1
        maxs_from_left = []
        m = A[0]
        for num in A:
            m = max(m, num)
            maxs_from_left.append(m)

        mins_from_right = []
        m = A[-1]
        for num in A[::-1]:
            m = min(m, num)
            mins_from_right.insert(0, m)

        for i in range(len(A) - 1):
            if maxs_from_left[i] <= mins_from_right[i + 1]:
                return i + 1


class PartitionArrayIntoDisjointIntervalsUnittest(unittest.TestCase):

    def test_case_1(self):
        A = [5, 0, 3, 8, 6]
        self.assertEqual(3, Solution.partitionDisjoint(A))

    def test_case_2(self):
        A = [1, 1, 1, 0, 6, 12]
        self.assertEqual(4, Solution.partitionDisjoint(A))

    def test_case_3(self):
        A = [6, 0, 8, 30, 37, 6, 75, 98, 39, 90, 63, 74, 52, 92, 64]
        self.assertEqual(2, Solution.partitionDisjoint(A))
