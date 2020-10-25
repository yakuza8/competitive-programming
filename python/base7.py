import unittest


class Solution:

    @staticmethod
    def convertToBase7(num: int) -> str:
        """
        Given an integer, return its base 7 string representation.

        Example 1:
        Input: 100
        Output: "202"

        Example 2:
        Input: -7
        Output: "-10"

        Note: The input will be in range of [-1e7, 1e7].
        """
        def helper(_num):
            i = 1
            base = []
            while _num >= i * 7:
                i *= 7

            remaining = _num
            while i > 0:
                base.append(str(remaining // i))
                remaining = remaining % i
                i //= 7

            return "".join(base)

        is_negative = num < 0
        return "-" + helper(-num) if is_negative else helper(num)


class Base7(unittest.TestCase):

    def test_case_1(self):
        num = 100
        self.assertEqual("202", Solution.convertToBase7(num))

    def test_case_2(self):
        num = -7
        self.assertEqual("-10", Solution.convertToBase7(num))

    def test_case_3(self):
        num = 0
        self.assertEqual("0", Solution.convertToBase7(num))
