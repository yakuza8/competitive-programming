import unittest


class Solution:

    @staticmethod
    def backspaceCompare(S: str, T: str) -> bool:
        """
        Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

        Example 1:
        Input: S = "ab#c", T = "ad#c"
        Output: true
        Explanation: Both S and T become "ac".

        Example 2:
        Input: S = "ab##", T = "c#d#"
        Output: true
        Explanation: Both S and T become "".

        Example 3:
        Input: S = "a##c", T = "#a#c"
        Output: true
        Explanation: Both S and T become "c".

        Example 4:
        Input: S = "a#c", T = "b"
        Output: false
        Explanation: S becomes "c" while T becomes "b".

        Note:
            1 <= S.length <= 200
            1 <= T.length <= 200
            S and T only contain lowercase letters and '#' characters.

        Follow up:
            Can you solve it in O(N) time and O(1) space?
        """

        def create_last_string(s: str) -> str:
            stack = []
            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)
        return create_last_string(S) == create_last_string(T)


class BackspaceStringCompare(unittest.TestCase):

    def test_case_1(self):
        S = "ab#c"
        T = "ad#c"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_2(self):
        S = "ab##"
        T = "c#d#"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_3(self):
        S = "a##c"
        T = "#a#c"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_4(self):
        S = "a#c"
        T = "b"
        expected_result = False
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_5(self):
        S = "xywrrmp"
        T = "xywrrmu#p"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_6(self):
        S = "bbbextm"
        T = "bbb#extm"
        expected_result = False
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_7(self):
        S = "nzp#o#g"
        T = "b#nzp#o#g"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    def test_case_8(self):
        S = "y#fo##f"
        T = "y#f#o##f"
        expected_result = True
        self.assertEqual(expected_result, Solution.backspaceCompare(S, T))

    "y#f#o##f"