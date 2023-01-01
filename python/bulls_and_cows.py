import unittest


class Solution:
    @staticmethod
    def getHint(secret: str, guess: str) -> str:
        """
        You are playing the Bulls and Cows game with your friend.

        You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess,
        you provide a hint with the following info:

        The number of "bulls", which are digits in the guess that are in the correct position. The number of "cows",
        which are digits in the guess that are in your secret number but are located in the wrong position. Specifically,
        the non-bull digits in the guess that could be rearranged such that they become bulls. Given the secret number
        secret and your friend's guess guess, return the hint for your friend's guess.

        The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that
        both secret and guess may contain duplicate digits.

        Example 1:
            Input: secret = "1807", guess = "7810"
            Output: "1A3B"
            Explanation: Bulls are connected with a '|' and cows are underlined:
            "1807"
              |
            "7810"

        Example 2:
            Input: secret = "1123", guess = "0111"
            Output: "1A1B"
            Explanation: Bulls are connected with a '|' and cows are underlined:
            "1123"        "1123"
              |      or     |
            "0111"        "0111"
            Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be
            rearranged to allow one 1 to be a bull.

        Constraints:
            1 <= secret.length, guess.length <= 1000
            secret.length == guess.length
            secret and guess consist of digits only.
        """
        from collections import defaultdict

        bulls, cows = 0, 0
        secret_mapping, guess_mapping = defaultdict(int), defaultdict(int)

        for i, j in zip(secret, guess):
            if i == j:
                bulls += 1
            else:
                secret_mapping[i] += 1
                guess_mapping[j] += 1

        cows = sum(min(guess_mapping[ch], secret_mapping[ch]) for ch in guess_mapping)

        return f'{bulls}A{cows}B'


class BullsAndCows(unittest.TestCase):

    def test_case_1(self):
        secret, guess = '1807', '7810'
        expected_result = '1A3B'
        self.assertEqual(expected_result, Solution.getHint(secret, guess))

    def test_case_2(self):
        secret, guess = '1123', '0111'
        expected_result = '1A1B'
        self.assertEqual(expected_result, Solution.getHint(secret, guess))
