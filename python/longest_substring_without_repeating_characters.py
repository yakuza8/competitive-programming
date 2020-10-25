import unittest


class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        Given a string, find the length of the longest substring without repeating characters.

        Example 1:
        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:
        Input: "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:
        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.

        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Runtime: 48 ms, faster than 93.20% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 13 MB, less than 99.49% of Python3 online submissions for Longest Substring Without Repeating Characters.
        """
        if s == "":
            return 0

        length_of_longest_substring = -1
        current_length = 0
        current_start = 0
        char_position_map = {}

        for i, ch in enumerate(s):
            if ch in char_position_map:
                previous_position = char_position_map[ch]
                if previous_position >= current_start:
                    current_start = previous_position + 1
                    current_length = i - current_start + 1
                else:
                    current_length += 1
            else:
                current_length += 1

            if current_length > length_of_longest_substring:
                length_of_longest_substring = current_length
            char_position_map[ch] = i

        return length_of_longest_substring


class LongestSubstringWithoutRepeatingCharacters(unittest.TestCase):

    def test_case_1(self):
        s = "abcabcbb"
        self.assertEqual(3, Solution.lengthOfLongestSubstring(s))

    def test_case_2(self):
        s = "bbbbb"
        self.assertEqual(1, Solution.lengthOfLongestSubstring(s))

    def test_case_3(self):
        s = "pwwkew"
        self.assertEqual(3, Solution.lengthOfLongestSubstring(s))

    def test_case_4(self):
        s = " "
        self.assertEqual(1, Solution.lengthOfLongestSubstring(s))

    def test_case_5(self):
        s = "abba"
        self.assertEqual(2, Solution.lengthOfLongestSubstring(s))

    def test_case_6(self):
        s = "tmmzuxt"
        self.assertEqual(5, Solution.lengthOfLongestSubstring(s))
