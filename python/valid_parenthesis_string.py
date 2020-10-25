import unittest


class Solution:

    @staticmethod
    def checkValidString(s: str) -> bool:
        """
        Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether
        this string is valid. We define the validity of a string by these rules:

        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
        An empty string is also valid.

        Example 1:
        Input: "()"
        Output: True

        Example 2:
        Input: "(*)"
        Output: True

        Example 3:
        Input: "(*))"
        Output: True

        Note:
        The string size will be in the range [1, 100].
        """
        parenthesis_stack = []
        star_stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                parenthesis_stack.append(i)
            elif ch == '*':
                star_stack.append(i)
            else:
                if parenthesis_stack:
                    parenthesis_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while parenthesis_stack and star_stack:
            if parenthesis_stack[-1] < star_stack[-1]:
                parenthesis_stack.pop()
                star_stack.pop()
            else:
                return False
        return not bool(parenthesis_stack)


class ValidParenthesisString(unittest.TestCase):

    def test_case_1(self):
        s = "()"
        expected_result = True
        self.assertEqual(expected_result, Solution.checkValidString(s))

    def test_case_2(self):
        s = "(*)"
        expected_result = True
        self.assertEqual(expected_result, Solution.checkValidString(s))

    def test_case_3(self):
        s = "(*))"
        expected_result = True
        self.assertEqual(expected_result, Solution.checkValidString(s))

    def test_case_4(self):
        s = "(*()"
        expected_result = True
        self.assertEqual(expected_result, Solution.checkValidString(s))

    def test_case_5(self):
        s = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
        expected_result = False
        self.assertEqual(expected_result, Solution.checkValidString(s))