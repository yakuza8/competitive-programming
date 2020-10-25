import unittest


class Solution:

    @staticmethod
    def magicalString(n: int) -> int:
        """
        A magical string S consists of only '1' and '2' and obeys the following rules:
        The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.
        The first few elements of string S is the following: S = "1221121221221121122……"

        If we group the consecutive '1's and '2's in S, it will be:
        1 22 11 2 1 22 1 22 11 2 11 22 ......
        and the occurrences of '1's or '2's in each group are:
        1 2 2 1 1 2 1 2 2 1 2 2 ......

        You can see that the occurrence sequence above is the S itself.
        Given an integer N as input, return the number of '1's in the first N number in the magical string S.
        Note: N will not exceed 100,000.

        Example 1:
        Input: 6
        Output: 3
        Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.

        Runtime: 136 ms, faster than 38.38% of Python3 online submissions for Magical String.
        Memory Usage: 14.3 MB, less than 50.00% of Python3 online submissions for Magical String.

        Runtime: 140 ms, faster than 37.37% of Python3 online submissions for Magical String.
        Memory Usage: 13.7 MB, less than 75.00% of Python3 online submissions for Magical String.
        """
        '''
        if n == 0:
            return 0
        elif n <= 3:
            return 1
        else:
            string = [1, 2, 2]
            string_length = 3
            index = 2

            while string_length < n:
                element_to_extend = 1 if index % 2 == 0 else 2
                count_to_extend = string[index]
                string.extend(count_to_extend * [element_to_extend])
                index += 1
                string_length += count_to_extend

            return string[:n].count(1)
        '''

        if n == 0:
            return 0
        elif n <= 3:
            return 1
        else:
            string = [1, 2, 2]
            index = 2
            one_count = 1
            n = n - 3

            while n > 0:
                element_to_extend = 1 if index % 2 == 0 else 2
                count_to_extend = string[index]
                string.extend(count_to_extend * [element_to_extend])
                index += 1
                n -= count_to_extend
                one_count += 0 if element_to_extend == 2 else (count_to_extend if n >= 0 else n + count_to_extend)

            return one_count


class MagicalString(unittest.TestCase):

    def test_case_1(self):
        n = 6
        expected_output = 3
        self.assertEqual(expected_output, Solution.magicalString(n))
