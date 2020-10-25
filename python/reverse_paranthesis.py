import unittest
from typing import Tuple, List


class Solution:

    @staticmethod
    def reverseParentheses(s: str) -> str:
        """
        You are given a string s that consists of lower case English letters and brackets.
        Reverse the strings in each pair of matching parentheses, starting from the innermost one.
        Your result should not contain any brackets.

        Example 1:
        Input: s = "(abcd)"
        Output: "dcba"

        Example 2:
        Input: s = "(u(love)i)"
        Output: "iloveu"
        Explanation: The substring "love" is reversed first, then the whole string is reversed.

        Example 3:
        Input: s = "(ed(et(oc))el)"
        Output: "leetcode"
        Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

        Example 4:
        Input: s = "a(bcdefghijkl(mno)p)q"
        Output: "apmnolkjihgfedcbq"

        Runtime: 20 ms, faster than 98.60% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.
        """

        def find_matching_parentheses(_s: str) -> List[Tuple[int, int]]:
            _matches = []
            stack = []

            for index, char in enumerate(_s):
                if char == '(':
                    stack.append(index)
                elif char == ')':
                    _matches.append((stack.pop(), index))

            return _matches

        matches = find_matching_parentheses(s)
        matches = sorted(matches, key=lambda v: v[1] - v[0])

        for start, end in matches:
            s = s[:start] + s[start:end + 1][::-1] + s[end + 1:]

        return ''.join(i for i in s if i not in ['(', ')'])


class ReverseSubstringsBetweenEachPairOfParentheses(unittest.TestCase):

    def test_case_1(self):
        s = "(abcd)"
        expected_output = "dcba"
        self.assertEqual(expected_output, Solution.reverseParentheses(s))

    def test_case_2(self):
        s = "(u(love)i)"
        expected_output = "iloveu"
        self.assertEqual(expected_output, Solution.reverseParentheses(s))

    def test_case_3(self):
        s = "(ed(et(oc))el)"
        expected_output = "leetcode"
        self.assertEqual(expected_output, Solution.reverseParentheses(s))

    def test_case_4(self):
        s = "a(bcdefghijkl(mno)p)q"
        expected_output = "apmnolkjihgfedcbq"
        self.assertEqual(expected_output, Solution.reverseParentheses(s))
