from typing import List
import unittest


class Solution(object):
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, num in enumerate(nums):
            if target - num in indexes:
                return [indexes[target - num], i]
            indexes[num] = i

    @staticmethod
    def two_sum_sorted_array(nums: List[int], target: int) -> List[int]:
        """
        With above implementation
        Runtime: 68 ms, faster than 77.90% of Python3 online submissions for Two Sum II - Input array is sorted.
        Memory Usage: 13.7 MB, less than 18.84% of Python3 online submissions for Two Sum II - Input array is sorted.

        With commented implementation
        Runtime: 1676 ms, faster than 5.00% of Python3 online submissions for Two Sum II - Input array is sorted.
        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.

        With submitted implementation
        Runtime: 60 ms, faster than 96.03% of Python3 online submissions for Two Sum II - Input array is sorted.
        Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
        """
        mapping = {_key: _index for (_index, _key) in enumerate(nums)}
        for (_index, _key) in enumerate(nums):
            target_num = target - _key
            if target_num in mapping:
                target_index = mapping[target_num]
                if _index != target_index:
                    return [_index, target_index]


class TwoSumUnittest(unittest.TestCase):

    def test_case_1(self):
        _nums = [2, 7, 11, 15]
        _target = 9
        _result = Solution.two_sum(_nums, _target)
        self.assertListEqual([0, 1], _result)

    def test_case_2(self):
        _nums = [2, 7, 11, 15]
        _target = 22
        _result = Solution.two_sum(_nums, _target)
        self.assertListEqual([1, 3], _result)

    def test_case_3(self):
        _nums = [2, 7, 11, 15]
        _target = 26
        _result = Solution.two_sum(_nums, _target)
        self.assertListEqual([2, 3], _result)

    def test_case_4(self):
        """
        Check there is no answer returned by the function
        """
        _nums = [2, 7, 11, 15]
        _target = 4
        _result = Solution.two_sum(_nums, _target)
        self.assertIsNone(_result)

    def test_case_5(self):
        """
        Multiple index for the same number
        """
        _nums = [2, 7, 2, 15]
        _target = 4
        _result = Solution.two_sum(_nums, _target)
        self.assertListEqual([0, 2], _result)

    def test_case_6(self):
        """
        Target number can be reached by multiple solutions
        but get it with the first encountered one
        """
        _nums = [21, 7, 6, 15, 3, 2]
        _target = 9
        _result = Solution.two_sum(_nums, _target)
        self.assertListEqual([2, 4], _result)


class TwoSumSortedUnittest(unittest.TestCase):

    def test_case_1(self):
        _nums = [2, 7, 11, 15]
        _target = 9
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertListEqual([0, 1], _result)

    def test_case_2(self):
        _nums = [2, 7, 11, 15]
        _target = 22
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertListEqual([1, 3], _result)

    def test_case_3(self):
        _nums = [2, 7, 11, 15]
        _target = 26
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertListEqual([2, 3], _result)

    def test_case_4(self):
        """
        Check there is no answer returned by the function
        """
        _nums = [2, 7, 11, 15]
        _target = 4
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertIsNone(_result)

    def test_case_5(self):
        """
        Multiple index for the same number
        """
        _nums = [2, 7, 2, 15]
        _target = 4
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertListEqual([0, 2], _result)

    def test_case_6(self):
        """
        Target number can be reached by multiple solutions
        but get it with the first encountered one
        """
        _nums = [2, 3, 6, 7, 15]
        _target = 9
        _result = Solution.two_sum_sorted_array(_nums, _target)
        self.assertListEqual([0, 3], _result)


if __name__ == '__main__':
    unittest.main()
