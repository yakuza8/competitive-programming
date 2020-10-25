import unittest
from typing import List


class Solution:

    @staticmethod
    def calPoints(ops: List[str]) -> int:
        """
         You're now a baseball game point recorder.

        Given a list of strings, each string can be one of the 4 following types:
            Integer (one round's score): Directly represents the number of points you get in this round.
            "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
            "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
            "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.

        Each round's operation is permanent and could have an impact on the round before and the round after.
        You need to return the sum of the points you could get in all the rounds.

        Example 1:
        Input: ["5","2","C","D","+"]
        Output: 30
        Explanation:
        Round 1: You could get 5 points. The sum is: 5.
        Round 2: You could get 2 points. The sum is: 7.
        Operation 1: The round 2's data was invalid. The sum is: 5.
        Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
        Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

        Example 2:
        Input: ["5","-2","4","C","D","9","+","+"]
        Output: 27
        Explanation:
        Round 1: You could get 5 points. The sum is: 5.
        Round 2: You could get -2 points. The sum is: 3.
        Round 3: You could get 4 points. The sum is: 7.
        Operation 1: The round 3's data is invalid. The sum is: 3.
        Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
        Round 5: You could get 9 points. The sum is: 8.
        Round 6: You could get -4 + 9 = 5 points. The sum is 13.
        Round 7: You could get 9 + 5 = 14 points. The sum is 27.
        """
        valid_scores = []
        summed_score = 0

        def add_score(_score: int, _summed_score: int) -> int:
            _summed_score += score
            valid_scores.append(score)
            return _summed_score

        for op in ops:
            if op == 'C':
                cancelled_score = valid_scores.pop()
                summed_score -= cancelled_score
            elif op == 'D':
                score = 2 * valid_scores[-1]
                summed_score = add_score(score, summed_score)
            elif op == '+':
                score = sum(valid_scores[-2::])
                summed_score = add_score(score, summed_score)
            else:
                score = int(op)
                summed_score = add_score(score, summed_score)

        return summed_score


class BaseballGame(unittest.TestCase):

    def test_case_1(self):
        ops = ["5", "2", "C", "D", "+"]
        expected_output = 30
        self.assertEqual(expected_output, Solution.calPoints(ops))

    def test_case_2(self):
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        expected_output = 27
        self.assertEqual(expected_output, Solution.calPoints(ops))
