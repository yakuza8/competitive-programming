import unittest


class Solution:

    @staticmethod
    def rangeBitwiseAnd(m: int, n: int) -> int:
        """
        Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range,
        inclusive.

        Example 1:
        Input: [5,7]
        Output: 4

        Example 2:
        Input: [0,1]
        Output: 0
        """
        difference = n - m
        small_number_bin_repr = bin(m)[2:]
        reversed_repr = small_number_bin_repr[::-1]
        up_to_now_needed_sum = 0

        result = 0

        for index, value in enumerate(reversed_repr):
            current_digit = int(value)

            if current_digit == 1:
                # To make this digit 0, the amount we needed
                change_amount = up_to_now_needed_sum + 1
                if difference < change_amount:
                    result += 1 << index
            else:
                up_to_now_needed_sum += 1 << index

        return result


class BitwiseAndOfNumberRange(unittest.TestCase):

    def test_case_1(self):
        m, n = [5, 7]
        expected_result = 4
        self.assertEqual(expected_result, Solution.rangeBitwiseAnd(m, n))

    def test_case_2(self):
        m, n = [0, 1]
        expected_result = 0
        self.assertEqual(expected_result, Solution.rangeBitwiseAnd(m, n))
