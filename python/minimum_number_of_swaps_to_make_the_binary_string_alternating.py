import unittest
from typing import List


class Solution:

    @staticmethod
    def minSwaps(s: str) -> int:
        """
        Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is
        impossible.

        The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and
        "1010" are alternating, while the string "0100" is not.

        Any two characters may be swapped, even if they are not adjacent.

        Example 1:
            Input: s = "111000"
            Output: 1
            Explanation: Swap positions 1 and 4: "111000" -> "101010"
            The string is now alternating.

        Example 2:
            Input: s = "010"
            Output: 0
            Explanation: The string is already alternating, no swaps are needed.

        Example 3:
            Input: s = "1110"
            Output: -1

        Constraints:
            1 <= s.length <= 1000
            s[i] is either '0' or '1'.
        """
        alternation = [[0, 0], [0, 0]]
        for idx, num in enumerate(s):
            alternation[idx % 2][int(num)] += 1
        (f_zero, f_one), (s_zero, s_one) = alternation

        if abs(f_zero + s_zero - f_one - s_one) > 1:
            return -1

        num_zero, num_one = f_zero + s_zero, f_one + s_one
        if num_zero == num_one:
            return min(alternation[0])
        elif num_zero > num_one:
            return alternation[0][1]
        else:
            return alternation[0][0]


class SenderWithLargestWordCount(unittest.TestCase):

    def test_case_1(self):
        s = '111000'
        expected_output = 1
        self.assertEqual(expected_output, Solution.minSwaps(s))

    def test_case_2(self):
        s = '010'
        expected_output = 0
        self.assertEqual(expected_output, Solution.minSwaps(s))

    def test_case_3(self):
        s = '1110'
        expected_output = -1
        self.assertEqual(expected_output, Solution.minSwaps(s))

    def test_case_4(self):
        s = '00011110110110000000000110110101011101111011111101010010010000000000000001101101010010001011110000001101111111110000110101101101001011000011111011101101100110011111110001100110001110000000001100010111110100111001001111100001000110101111010011001'
        expected_output = 65
        self.assertEqual(expected_output, Solution.minSwaps(s))
