import unittest
from typing import List


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:
            Input: strs = ["flower","flow","flight"]
            Output: "fl"

        Example 2:
            Input: strs = ["dog","racecar","car"]
            Output: ""
            Explanation: There is no common prefix among the input strings.

        Constraints:
            1 <= strs.length <= 200
            0 <= strs[i].length <= 200
            strs[i] consists of only lowercase English letters.
        """

        def get_common_prefix(s1: str, s2: str) -> str:
            prefix = ''
            for ch1, ch2 in zip(s1, s2):
                if ch1 == ch2:
                    prefix += ch1
                else:
                    break
            return prefix

        prefix = strs[0]
        for string in strs[1:]:
            prefix = get_common_prefix(prefix, string)
            if len(prefix) == 0:
                break
        return prefix


class LongestCommonPrefix(unittest.TestCase):

    def test_case_1(self):
        strs = ["flower", "flow", "flight"]
        expected_result = "fl"
        self.assertEqual(expected_result, Solution.longestCommonPrefix(strs))

    def test_case_2(self):
        strs = ["dog", "racecar", "car"]
        expected_result = ""
        self.assertEqual(expected_result, Solution.longestCommonPrefix(strs))
