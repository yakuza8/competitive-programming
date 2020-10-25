import unittest


class Solution:
    @staticmethod
    def num_jewels_in_stones(J: str, S: str) -> int:
        """
        You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
        Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
        The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

        Example 1:
        Input: J = "aA", S = "aAAbbbb"
        Output: 3

        Example 2:
        Input: J = "z", S = "ZZ"
        Output: 0

        Note:
        S and J will consist of letters and have length at most 50.
        The characters in J are distinct.

        :param J: String where each character representing jewel types
        :param S: Stones that you have
        :return: Count of jewels among stones

        Runtime: 20 ms, faster than 99.22% of Python3 online submissions for Jewels and Stones.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
        """
        return sum([S.count(ch) for ch in J])


class JewelsInStonesUnittest(unittest.TestCase):

    def test_case_1(self):
        J = "aA"
        S = "aAAbbbb"
        expected_result = 3
        self.assertEquals(expected_result, Solution.num_jewels_in_stones(J, S))

    def test_case_2(self):
        J = "z"
        S = "ZZ"
        expected_result = 0
        self.assertEquals(expected_result, Solution.num_jewels_in_stones(J, S))
