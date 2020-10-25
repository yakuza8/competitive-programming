import unittest


class Solution:

    @staticmethod
    def count_and_say(n: int) -> str:
        base = "1"
        for i in range(1, n):
            chars = [ch for ch in base]
            new_chars = []
            count = 0
            ch = chars[0]
            for char in chars:
                if ch == char:
                    count = count + 1
                else:
                    new_chars.append(str(count))
                    new_chars.append(ch)
                    ch = char
                    count = 1
            new_chars.append(str(count))
            new_chars.append(ch)
            base = "".join(new_chars)

        return base


class CountAndSayUnittest(unittest.TestCase):

    def test_case_1(self):
        for i in range(1, 7):
            print(Solution.count_and_say(i))
