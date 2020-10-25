import unittest
from typing import List


class Solution:

    @staticmethod
    def countElements(arr: List[int]) -> int:
        """
        Given an integer array arr, count element x such that x + 1 is also in arr.
        If there're duplicates in arr, count them seperately.

        Example 1:
        Input: arr = [1,2,3]
        Output: 2
        Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

        Example 2:
        Input: arr = [1,1,3,3,5,5,7,7]
        Output: 0
        Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.

        Example 3:
        Input: arr = [1,3,2,3,5,0]
        Output: 3
        Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.

        Example 4:
        Input: arr = [1,1,2,2]
        Output: 2
        Explanation: Two 1s are counted cause 2 is in arr.


        Constraints:
            1 <= arr.length <= 1000
            0 <= arr[i] <= 1000
        """
        from collections import defaultdict
        counts = 0

        element_counts = defaultdict(int)

        for num in arr:
            element_counts[num] += 1

        for num, count in element_counts.items():
            if num + 1 in element_counts:
                counts += count

        return counts


class CountingElements(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 3]
        expected_result = 2
        self.assertEqual(expected_result, Solution.countElements(arr))

    def test_case_2(self):
        arr = [1, 1, 3, 3, 5, 5, 7, 7]
        expected_result = 0
        self.assertEqual(expected_result, Solution.countElements(arr))

    def test_case_3(self):
        arr = [1, 3, 2, 3, 5, 0]
        expected_result = 3
        self.assertEqual(expected_result, Solution.countElements(arr))

    def test_case_4(self):
        arr = [1, 1, 2, 2]
        expected_result = 2
        self.assertEqual(expected_result, Solution.countElements(arr))
