import unittest


class Pattern:
    def __init__(self, current_char: str, is_compulsory: bool, has_star_next: bool):
        self.current_char = current_char
        self.is_compulsory = is_compulsory
        self.has_star_next = has_star_next


class Solution:

    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        """
        Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).

        Note:
        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.

        Example 1:
        Input:
        s = "aa"
        p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".

        Example 2:
        Input:
        s = "aa"
        p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

        Example 3:
        Input:
        s = "ab"
        p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".

        Example 4:
        Input:
        s = "aab"
        p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

        Example 5:
        Input:
        s = "mississippi"
        p = "mis*is*p*."
        Output: false

        # Recursive
        Runtime: 1036 ms, faster than 29.63% of Python3 online submissions for Regular Expression Matching.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.

        Runtime: 48 ms, faster than 67.93% of Python3 online submissions for Regular Expression Matching.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
        """

        def pattern_can_be_ignored(pattern: str) -> bool:
            pattern_length = len(pattern)
            for i, char in enumerate(pattern):
                if char == '*':
                    continue
                else:
                    if i < pattern_length - 1:
                        if pattern[i + 1] == '*':
                            continue
                        else:
                            return False
                    return False
            return True

        '''
        def helper(string: str, pattern: str) -> bool:
            if pattern == "":
                return string == ""

            last_char = pattern[-1]
            current_char = last_char
            can_be_repeated = False
            if last_char == '*':
                current_char = pattern[-2]
                can_be_repeated = True

            if string == "":
                return pattern_can_be_ignored(pattern)

            if can_be_repeated:
                return ((string[-1] == current_char or current_char == '.') and (
                        helper(string[:-1], pattern[:-2]) or helper(string[:-1], pattern))) or helper(string, pattern[:-2])
            else:
                return (string[-1] == current_char or current_char == '.') and helper(string[:-1], pattern[:-1])

        return helper(s, p)
        '''
        string_length = len(s)
        pattern_length = len(p)
        tableau = [[False for _ in range(string_length + 1)] for _ in range(pattern_length + 1)]

        for i in range(1, string_length + 1):
            tableau[0][i] = False
        for i in range(1, pattern_length + 1):
            tableau[i][0] = pattern_can_be_ignored(p[:i])
        tableau[0][0] = True

        for i in range(1, pattern_length + 1):
            for j in range(1, string_length + 1):
                last_char = p[i - 1]
                can_be_repeated = True if last_char == '*' else False
                current_char = last_char if not can_be_repeated else p[i - 2]

                if can_be_repeated:
                    tableau[i][j] = ((s[j - 1] == current_char or current_char == '.') and (
                            tableau[i - 2][j - 1] or tableau[i][j - 1])) or tableau[i - 2][j]
                else:
                    tableau[i][j] = (s[j - 1] == current_char or current_char == '.') and tableau[i - 1][j - 1]

        return tableau[pattern_length][string_length]


class RegularExpressionMatching(unittest.TestCase):

    def test_case_1(self):
        s = "aa"
        p = "a"
        expected_output = False
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_2(self):
        s = "aa"
        p = "a*"
        expected_output = True
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_3(self):
        s = "ab"
        p = ".*"
        expected_output = True
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_4(self):
        s = "aab"
        p = "c*a*b"
        expected_output = True
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_5(self):
        s = "mississippi"
        p = "mis*is*p*."
        expected_output = False
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_6(self):
        s = "aaa"
        p = "aaaa"
        expected_output = False
        self.assertEqual(expected_output, Solution.isMatch(s, p))

    def test_case_7(self):
        s = "aaa"
        p = "ab*ac*a"
        expected_output = True
        self.assertEqual(expected_output, Solution.isMatch(s, p))
