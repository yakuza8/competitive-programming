import unittest


class Solution:

    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        """
        Given two strings text1 and text2, return the length of their longest common subsequence.
        A subsequence of a string is a new string generated from the original string with some characters(can be none)
        deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
        while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
        If there is no common subsequence, return 0.

        Example 1:
        Input: text1 = "abcde", text2 = "ace"
        Output: 3
        Explanation: The longest common subsequence is "ace" and its length is 3.

        Example 2:
        Input: text1 = "abc", text2 = "abc"
        Output: 3
        Explanation: The longest common subsequence is "abc" and its length is 3.

        Example 3:
        Input: text1 = "abc", text2 = "def"
        Output: 0
        Explanation: There is no such common subsequence, so the result is 0.

        Constraints:
            1 <= text1.length <= 1000
            1 <= text2.length <= 1000
            The input strings consist of lowercase English characters only.
        """
        '''
        def helper(t1: str, t2: str) -> int:
            if len(t1) == 0 or len(t2) == 0:
                return 0
            else:
                still_t1 = helper(t1, t2[:-1])
                still_t2 = helper(t1[:-1], t2)
                common_postfix = helper(t1[:-1], t2[:-1]) + (1 if t1[-1] == t2[-1] else 0)
                return max(still_t1, still_t2, common_postfix)
        return helper(text1, text2)
        '''
        tableau = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
        for index2 in range(1, len(text2) + 1):
            for index1 in range(1, len(text1) + 1):
                tableau[index2][index1] = max(tableau[index2 - 1][index1], tableau[index2][index1 - 1],
                                              tableau[index2 - 1][index1 - 1] + (
                                                  1 if text1[index1 - 1] == text2[index2 - 1] else 0))
        return tableau[-1][-1]


class LongestCommonSubsequence(unittest.TestCase):

    def test_case_1(self):
        text1, text2 = "abcde", "ace"
        expected_result = 3
        self.assertEqual(expected_result, Solution.longestCommonSubsequence(text1, text2))

    def test_case_2(self):
        text1, text2 = "abc", "abc"
        expected_result = 3
        self.assertEqual(expected_result, Solution.longestCommonSubsequence(text1, text2))

    def test_case_3(self):
        text1, text2 = "abc", "def"
        expected_result = 0
        self.assertEqual(expected_result, Solution.longestCommonSubsequence(text1, text2))
