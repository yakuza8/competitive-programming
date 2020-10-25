import unittest


class Solution:
    @staticmethod
    def defang_ip_addr(address: str) -> str:
        """
        Given a valid (IPv4) IP address, return a defanged version of that IP address.
        A defanged IP address replaces every period "." with "[.]".

        Example 1:
        Input: address = "1.1.1.1"
        Output: "1[.]1[.]1[.]1"

        Example 2:
        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"

        :param address: Valid IP4  address
        :return: Defanged version of the input parameter

        Runtime: 20 ms, faster than 98.85% of Python3 online submissions for Defanging an IP Address.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
        """
        return '[.]'.join(address.split('.'))

    @staticmethod
    def defang_ip_addr_regex(address: str) -> str:
        """
        Given a valid (IPv4) IP address, return a defanged version of that IP address.
        A defanged IP address replaces every period "." with "[.]".

        Example 1:
        Input: address = "1.1.1.1"
        Output: "1[.]1[.]1[.]1"

        Example 2:
        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"

        :param address: Valid IP4  address
        :return: Defanged version of the input parameter
        """
        import re
        return re.sub('\.', '[.]', address)


class DefangedIPAddressUnittest(unittest.TestCase):

    def test_case_1(self):
        address = "1.1.1.1"
        expected_result = "1[.]1[.]1[.]1"
        self.assertEquals(expected_result, Solution.defang_ip_addr(address))

    def test_case_2(self):
        address = "255.100.50.0"
        expected_result = "255[.]100[.]50[.]0"
        self.assertEquals(expected_result, Solution.defang_ip_addr(address))


class DefangedIPAddress2Unittest(unittest.TestCase):

    def test_case_1(self):
        address = "1.1.1.1"
        expected_result = "1[.]1[.]1[.]1"
        self.assertEquals(expected_result, Solution.defang_ip_addr_regex(address))

    def test_case_2(self):
        address = "255.100.50.0"
        expected_result = "255[.]100[.]50[.]0"
        self.assertEquals(expected_result, Solution.defang_ip_addr_regex(address))
