import unittest


class Solution:

    @staticmethod
    def findNthDigit(n: int) -> int:
        """
        Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

        Note:
        n is positive and will fit within the range of a 32-bit signed integer (n < 231).

        Example 1:
        Input:
        3
        Output:
        3

        Example 2:
        Input:
        11
        Output:
        0

        Explanation:
        The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

        Runtime: 24 ms, faster than 87.55% of Python3 online submissions for Nth Digit.
        Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Nth Digit.
        """
        current_decimal_size = 0
        while True:
            current_decimal_size += 1
            min_value = int("1" + (current_decimal_size - 1) * "0")
            max_value = int("9" * current_decimal_size)
            digit_count = (max_value - min_value + 1) * current_decimal_size

            if n <= digit_count:
                break
            n -= digit_count

        # Proper decimal and min value is found
        n -= 1
        skip_count = n // current_decimal_size
        position = n % current_decimal_size
        min_value += skip_count
        return int(str(min_value)[position])


class FindNthDigit(unittest.TestCase):

    def test_case_1(self):
        n = 3
        expected_output = 3
        self.assertEqual(expected_output, Solution.findNthDigit(n))

    def test_case_2(self):
        n = 11
        expected_output = 0
        self.assertEqual(expected_output, Solution.findNthDigit(n))

    def test_case_3(self):
        n = 200
        expected_output = 0
        self.assertEqual(expected_output, Solution.findNthDigit(n))

    def test_case_4(self):
        n = 9
        expected_output = 9
        self.assertEqual(expected_output, Solution.findNthDigit(n))
