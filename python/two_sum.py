from typing import List
import unittest


class Solution(object):
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        # Get index list for each number
        number_with_indexes = defaultdict(list)
        for index, number in enumerate(nums):
            number_with_indexes[number].append(index)

        # Then iterate over them to find target number
        # which results into target value by summing
        # with current number
        for index, number in enumerate(nums):
            target_minus_number = target - number
            if target_minus_number in number_with_indexes:
                target_number_index_list = number_with_indexes[target_minus_number]
                for target_number_index in target_number_index_list:
                    # The index should not be the same with current number
                    if target_number_index != index:
                        return [index, target_number_index]

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

        '''
        def find_item_in_the_list(_key, _list, _prev_start):
            if len(_list) == 0:
                return None
            elif len(_list) == 1:
                return None if _list[0] != _key else _prev_start

            _middle_index = int(len(_list) / 2)
            _middle = _list[_middle_index]
            if _middle == _key:
                return _prev_start + _middle_index
            elif _middle < _key:
                return find_item_in_the_list(_key, _list[_middle_index + 1:], _prev_start + _middle_index + 1)
            else:
                return find_item_in_the_list(_key, _list[:_middle_index], _prev_start)

        for index, number in enumerate(nums):
            target_minus_number = target - number
            result = find_item_in_the_list(target_minus_number, nums, 0)
            if result is not None and index != result:
                return [index, result]
        '''

        mapping = {_key: _index for (_index, _key) in enumerate(nums)}
        for (_index, _key) in enumerate(nums):
            target_num = target - _key
            if target_num in mapping:
                target_index = mapping[target_num]
                return [_index + 1, target_index + 1]


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
        self.assertListEqual([1, 5], _result)


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
