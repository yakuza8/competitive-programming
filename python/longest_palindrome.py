import unittest


class Solution:

    @staticmethod
    def longest_palindrome(s: str) -> int:
        """
        Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
        This is case sensitive, for example "Aa" is not considered a palindrome here.

        Note:
        Assume the length of given string will not exceed 1,010.
        """
        from collections import defaultdict
        char_dict = defaultdict(int)

        for ch in s:
            char_dict[ch] += 1

        length_of_longest_palindrome = 0
        odd_exist = False
        for count in char_dict.values():
            if count % 2 == 0:
                length_of_longest_palindrome += count
            else:
                length_of_longest_palindrome += count - 1
                odd_exist = True
        return length_of_longest_palindrome + (1 if odd_exist else 0)


class LongestPalindrome(unittest.TestCase):

    def test_case_1(self):
        m = "abccccdd"
        expected_output = 7
        self.assertEqual(expected_output, Solution.longest_palindrome(m))

    def test_case_2(self):
        m = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        expected_output = 983
        self.assertEqual(expected_output, Solution.longest_palindrome(m))
