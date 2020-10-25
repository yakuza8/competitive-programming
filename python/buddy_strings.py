import unittest


class Solution:

    @staticmethod
    def buddyStrings(A: str, B: str) -> bool:
        """
        Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

        Example 1:
        Input: A = "ab", B = "ba"
        Output: true

        Example 2:
        Input: A = "ab", B = "ab"
        Output: false

        Example 3:
        Input: A = "aa", B = "aa"
        Output: true

        Example 4:
        Input: A = "aaaaaaabc", B = "aaaaaaacb"
        Output: true

        Example 5:
        Input: A = "", B = "aa"
        Output: false

        Note:
            0 <= A.length <= 20000
            0 <= B.length <= 20000
            A and B consist only of lowercase letters.
        """
        from collections import defaultdict

        if len(A) != len(B):
            return False

        encountered_char_A = defaultdict(int)
        encountered_char_B = defaultdict(int)
        diff_count = 0

        for i in range(len(A)):
            char_A = A[i]
            char_B = B[i]
            encountered_char_A[char_A] += 1
            encountered_char_B[char_B] += 1
            if char_A != char_B:
                diff_count += 1

        if len(encountered_char_A.keys() ^ encountered_char_B.keys()) > 0:
            return False

        has_even = False
        for key in encountered_char_A.keys():
            if encountered_char_A[key] % 2 == 0:
                has_even = True
            if encountered_char_A[key] != encountered_char_B[key]:
                return False

        if diff_count == 0:
            return has_even
        elif diff_count == 2:
            return True
        else:
            return False


class BuddyStrings(unittest.TestCase):

    def test_case_1(self):
        A = "ab"
        B = "ba"
        self.assertTrue(Solution.buddyStrings(A, B))

    def test_case_2(self):
        A = "ab"
        B = "ab"
        self.assertFalse(Solution.buddyStrings(A, B))

    def test_case_3(self):
        A = "aa"
        B = "aa"
        self.assertTrue(Solution.buddyStrings(A, B))

    def test_case_4(self):
        A = "aaaaaaabc"
        B = "aaaaaaacb"
        self.assertTrue(Solution.buddyStrings(A, B))

    def test_case_5(self):
        A = ""
        B = "aa"
        self.assertFalse(Solution.buddyStrings(A, B))
