import unittest
from typing import List, Union


class Solution:

    @staticmethod
    def calculate(s: str) -> int:
        """
        Implement a basic calculator to evaluate a simple expression string.
        The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
        The integer division should truncate toward zero.

        Example 1:
        Input: "3+2*2"
        Output: 7

        Example 2:
        Input: " 3/2 "
        Output: 1

        Example 3:
        Input: " 3+5 / 2 "
        Output: 5

        Note:
            You may assume that the given expression is always valid. Do not use the eval built-in library function.
        """
        import re
        operators = ['+', '-', '*', '/']

        def get_priority(op: str) -> int:
            if op in ['+', '-']:
                return 1
            return 2

        def convert_postfix(expression: List[Union[int, str]]) -> List:
            postfix = []
            operator_stack = []
            top_operator_priority = -1
            for element in expression:
                if element in operators:
                    priority = get_priority(element)
                    while priority <= top_operator_priority:
                        top_element = operator_stack.pop()
                        postfix.append(top_element)
                        if len(operator_stack) > 0:
                            top_operator_priority = get_priority(operator_stack[-1])
                        else:
                            break

                    operator_stack.append(element)
                    top_operator_priority = priority
                else:
                    postfix.append(int(element))
            for op in operator_stack[::-1]:
                postfix.append(op)
            return postfix

        def apply_operation(first: int, second: int, operator: str) -> int:
            if operator == '+':
                return first + second
            elif operator == '-':
                return first - second
            elif operator == '*':
                return first * second
            elif operator == '/':
                return first // second
            else:
                raise NotImplemented

        def evaluate_postfix(postfix: List[Union[int, str]]) -> int:
            stack = []
            for element in postfix:
                if element in operators:
                    second_operator = stack.pop()
                    first_operator = stack.pop()
                    stack.append(apply_operation(first_operator, second_operator, element))
                else:
                    stack.append(element)
            return stack.pop()

        expression_parsed = re.split(r'(\+|-|\*|/)', s)
        postfix_expression = convert_postfix(expression_parsed)
        return evaluate_postfix(postfix_expression)


class BasicCalculatorII(unittest.TestCase):

    def test_case_1(self):
        exp = "3+2*2"
        expected_output = 7
        self.assertEqual(expected_output, Solution.calculate(exp))

    def test_case_2(self):
        exp = " 3/2 "
        expected_output = 1
        self.assertEqual(expected_output, Solution.calculate(exp))

    def test_case_3(self):
        exp = "3+5 / 2"
        expected_output = 5
        self.assertEqual(expected_output, Solution.calculate(exp))

    def test_case_4(self):
        exp = "1-1+1"
        expected_output = 1
        self.assertEqual(expected_output, Solution.calculate(exp))

    def test_case_5(self):
        exp = "1*2-3/4+5*6-7*8+9/10"
        expected_output = -24
        self.assertEqual(expected_output, Solution.calculate(exp))
