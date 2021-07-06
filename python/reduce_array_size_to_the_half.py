import unittest
from typing import List


class Solution:

    @staticmethod
    def minSetSize(arr: List[int]) -> int:
        """
        Given an array arr.  You can choose a set of integers and remove all the occurrences of
        these integers in the array.

        Return the minimum size of the set so that at least half of the integers of the array are
        removed.

        Example 1:
        Input: arr = [3,3,3,3,5,5,5,2,2,7]
        Output: 2
        Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal
        to half of the size of the old array).
        Possible sets of size 2 are {3,5},{3,2},{5,2}.
        Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has
        size greater than half of the size of the old array.

        Example 2:
        Input: arr = [7,7,7,7,7,7]
        Output: 1
        Explanation: The only possible set you can choose is {7}. This will make the new array
        empty.

        Example 3:
        Input: arr = [1,9]
        Output: 1

        Example 4:
        Input: arr = [1000,1000,3,7]
        Output: 1

        Example 5:
        Input: arr = [1,2,3,4,5,6,7,8,9,10]
        Output: 5

        Constraints:
            1 <= arr.length <= 10^5
            arr.length is even.
            1 <= arr[i] <= 10^5
        """
        from collections import Counter

        # Count all the items
        c, half_length = Counter(arr), len(arr) // 2

        # Set size
        min_set_size, removed_element_count = 0, 0

        for item, count in c.most_common():
            removed_element_count += count
            min_set_size += 1
            if removed_element_count >= half_length:
                break
        return min_set_size


class ContiguousArray(unittest.TestCase):

    def test_case_1(self):
        arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
        expected_result = 2
        self.assertEqual(expected_result, Solution.minSetSize(arr))

    def test_case_2(self):
        arr = [7, 7, 7, 7, 7, 7]
        expected_result = 1
        self.assertEqual(expected_result, Solution.minSetSize(arr))

    def test_case_3(self):
        arr = [1, 9]
        expected_result = 1
        self.assertEqual(expected_result, Solution.minSetSize(arr))

    def test_case_4(self):
        arr = [1000, 1000, 3, 7]
        expected_result = 1
        self.assertEqual(expected_result, Solution.minSetSize(arr))

    def test_case_5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = 5
        self.assertEqual(expected_result, Solution.minSetSize(arr))
