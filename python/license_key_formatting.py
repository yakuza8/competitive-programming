import unittest


class Solution:
    @staticmethod
    def licenseKeyFormatting(S: str, K: int) -> str:
        """
        You are given a license key represented as a string S which consists only alphanumeric character and dashes.
        The string is separated into N+1 groups by N dashes. Given a number K, we would want to reformat the strings
        such that each group contains exactly K characters, except for the first group which could be shorter than K,
        but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and
         all lowercase letters should be converted to uppercase.

        Given a non-empty string S and a number K, format the string according to the rules described above.

        Example 1:
        Input: S = "5F3Z-2e-9-w", K = 4
        Output: "5F3Z-2E9W"

        Explanation: The string S has been split into two parts, each part has 4 characters.
        Note that the two extra dashes are not needed and can be removed.

        Example 2:
        Input: S = "2-5g-3-J", K = 2
        Output: "2-5G-3J"
        Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

        Note:
            The length of string S will not exceed 12,000, and K is a positive integer.
            String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
            String S is non-empty.

        Runtime: 36 ms, faster than 87.01% of Python3 online submissions for License Key Formatting.
        Memory Usage: 13.7 MB, less than 38.46% of Python3 online submissions for License Key Formatting.
        """
        S = "".join(S.split("-"))
        length = len(S)
        remaining = length % K
        if remaining == length:
            return S

        return (("" if remaining == 0 else S[:remaining] + "-") + "-".join(
            S[remaining:][K * i: K * (i + 1)] for i in range(length // K))).upper()


class LicenseKeyFormattingUnittest(unittest.TestCase):

    def test_case_1(self):
        key = "5F3Z-2e-9-w"
        K = 4
        expected_result = "5F3Z-2E9W"
        self.assertEqual(expected_result, Solution.licenseKeyFormatting(key, K))

    def test_case_2(self):
        key = "2-5g-3-J"
        K = 2
        expected_result = "2-5G-3J"
        self.assertEqual(expected_result, Solution.licenseKeyFormatting(key, K))

    def test_case_3(self):
        key = "2"
        K = 2
        expected_result = "2"
        self.assertEqual(expected_result, Solution.licenseKeyFormatting(key, K))