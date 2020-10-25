import unittest
from typing import List


class Solution:

    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings, group anagrams together.

        Example:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output:
        [
          ["ate","eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]

        Note:
            All inputs will be in lowercase.
            The order of your output does not matter.
        """
        from collections import defaultdict
        # minimum_char = ord('a')
        # maximum_char = ord('z')
        anagram_dict = defaultdict(list)

        for anagram in strs:
            # bits = [0 for _ in range(maximum_char - minimum_char + 1)]
            # for ch in anagram:
            #     bits[ord(ch) - minimum_char] += 1
            anagram_dict[''.join(sorted(anagram))].append(anagram)
        return list(anagram_dict.values())


class GroupAnagrams(unittest.TestCase):

    def test_case_1(self):
        anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_result = [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
        self.assertListEqual(expected_result, Solution.groupAnagrams(anagrams))
