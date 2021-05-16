import unittest


class Solution:

    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the
        order of characters. No two characters may map to the same character, but a character may
        map to itself.

        Example 1:
            Input: s = "egg", t = "add"
            Output: true

        Example 2:
            Input: s = "foo", t = "bar"
            Output: false

        Example 3:
            Input: s = "paper", t = "title"
            Output: true

        Constraints:
            1 <= s.length <= 5 * 104
            t.length == s.length
            s and t consist of any valid ascii character.
        """
        return Solution._is_iso(s, t) and Solution._is_iso(t, s)

    @staticmethod
    def _is_iso(s, t):
        char_mapping = {}
        for ch1, ch2 in zip(s, t):
            if ch1 in char_mapping:
                if char_mapping[ch1] != ch2:
                    return False
            else:
                char_mapping[ch1] = ch2
        return True


class IsomorphicStrings(unittest.TestCase):

    def test_case_1(self):
        s, t = 'egg', 'add'
        output = Solution.isIsomorphic(s, t)
        expected = True
        self.assertEqual(expected, output)

    def test_case_2(self):
        s, t = 'foo', 'bar'
        output = Solution.isIsomorphic(s, t)
        expected = False
        self.assertEqual(expected, output)

    def test_case_3(self):
        s, t = 'paper', 'title'
        output = Solution.isIsomorphic(s, t)
        expected = True
        self.assertEqual(expected, output)
