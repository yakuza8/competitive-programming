import unittest


class Solution:

    @staticmethod
    def numSplits(s: str) -> int:
        """
        You are given a string s, a split is called good if you can split s into 2 non-empty strings
        p and q where its concatenation is equal to s and the number of distinct letters in p and q
        are the same.

        Return the number of good splits you can make in s.

        Example 1:
            Input: s = "aacaba"
            Output: 2
            Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
            ("a", "acaba") Left string and right string contains 1 and 3 different letters
            respectively.
            ("aa", "caba") Left string and right string contains 1 and 3 different letters
            respectively.
            ("aac", "aba") Left string and right string contains 2 and 2 different letters
            respectively (good split).
            ("aaca", "ba") Left string and right string contains 2 and 2 different letters
            respectively (good split).
            ("aacab", "a") Left string and right string contains 3 and 1 different letters
            respectively.

        Example 2:
            Input: s = "abcd"
            Output: 1
            Explanation: Split the string as follows ("ab", "cd").

        Example 3:
            Input: s = "aaaaa"
            Output: 4
            Explanation: All possible splits are good.

        Example 4:
            Input: s = "acbadbaada"
            Output: 2

        Constraints:
            s contains only lowercase English letters.
            1 <= s.length <= 10^5
        """
        length = len(s)
        if length <= 1:
            return 0
        elif length == 2:
            return 1

        # Define window mappings
        count = 0
        left_map, right_map = {s[0]: 1}, {}
        for ch in s[1:]:
            if ch in right_map:
                right_map[ch] += 1
            else:
                right_map[ch] = 1

        # Slide the windows from now on
        for iteration in range(1, length):
            if len(left_map) == len(right_map):
                count += 1

            new_ch = s[iteration]
            # Going over left map
            if new_ch in left_map:
                left_map[new_ch] += 1
            else:
                left_map[new_ch] = 1

            # Going over right map
            if right_map[new_ch] == 1:
                del right_map[new_ch]
            else:
                right_map[new_ch] -= 1

        return count


class NumberOfGoodWaysToSplitAString(unittest.TestCase):

    def test_case_1(self):
        s = 'aacaba'
        expected_result = 2
        self.assertEqual(expected_result, Solution.numSplits(s))

    def test_case_2(self):
        s = 'abcd'
        expected_result = 1
        self.assertEqual(expected_result, Solution.numSplits(s))

    def test_case_3(self):
        s = 'aaaaa'
        expected_result = 4
        self.assertEqual(expected_result, Solution.numSplits(s))

    def test_case_4(self):
        s = 'acbadbaada'
        expected_result = 2
        self.assertEqual(expected_result, Solution.numSplits(s))
