import unittest
from typing import List


class Solution:
    @staticmethod
    def maxProfit(inventory: List[int], orders: int) -> int:
        """
        You have an inventory of different colored balls, and there is a customer that wants orders
        balls of any color.

        The customer weirdly values the colored balls. Each colored ball's value is the number of
        balls of that color you currently have in your inventory. For example, if you own 6 yellow
        balls, the customer would pay 6 for the first yellow ball. After the transaction, there are
        only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of
        the balls decreases as you sell more to the customer).

        You are given an integer array, inventory, where inventory[i] represents the number of balls
        of the ith color that you initially own. You are also given an integer orders, which
        represents the total number of balls that the customer wants. You can sell the balls in any
        order.

        Return the maximum total value that you can attain after selling orders colored balls. As
        the answer may be too large, return it modulo 109 + 7.

        Example 1:
        Input: inventory = [2,5], orders = 4
        Output: 14
        Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
        The maximum total value is 2 + 5 + 4 + 3 = 14.

        Example 2:
        Input: inventory = [3,5], orders = 6
        Output: 19
        Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
        The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

        Example 3:
        Input: inventory = [2,8,4,10,6], orders = 20
        Output: 110

        Example 4:
        Input: inventory = [1000000000], orders = 1000000000
        Output: 21
        Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000.
        500000000500000000 modulo 109 + 7 = 21.
        """

        def get_sales_aggregated(count, order_count, _backing_items, surplus=0):
            return (((count * (count + 1)) - (
                    (count - order_count) * (count - order_count + 1))) // 2) * _backing_items + (
                           surplus * (count - order_count))

        length = len(inventory)
        if length == 1:
            item_count = inventory[0]
            result = get_sales_aggregated(count=item_count, order_count=orders, _backing_items=1)
        else:
            result = 0
            ordered_inventory = sorted(inventory, reverse=True)

            for i in range(length - 1):
                if orders < 0:
                    break
                item_diff = ordered_inventory[i] - ordered_inventory[i + 1]
                backing_items = i + 1
                backing_item_count = backing_items * item_diff

                if orders >= backing_item_count:
                    order_count, surplus, total = item_diff, 0, item_diff * backing_items
                else:
                    order_count, surplus, total = orders // backing_items, orders % \
                                                  backing_items, orders
                result += get_sales_aggregated(ordered_inventory[i], order_count=order_count,
                                               _backing_items=backing_items, surplus=surplus)
                orders -= total
                ordered_inventory[i] -= item_diff

            while orders > 0:
                count = min(orders, length)
                result += ordered_inventory[-1] * count
                orders -= count
                ordered_inventory[-1] -= 1

        return int(result % (10 ** 9 + 7))


class SellDiminishingValuedColorBalls(unittest.TestCase):

    def test_case_1(self):
        inventory, orders = [2, 5], 4
        expected = 14
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))

    def test_case_2(self):
        inventory, orders = [3, 5], 6
        expected = 19
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))

    def test_case_3(self):
        inventory, orders = [2, 8, 4, 10, 6], 20
        expected = 110
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))

    def test_case_4(self):
        inventory, orders = [1000000000], 1000000000
        expected = 21
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))

    def test_case_5(self):
        inventory, orders = [773160767], 252264991
        expected = 70267492
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))

    def test_case_6(self):
        inventory, orders = [497978859, 167261111, 483575207, 591815159], 836556809
        expected = 373219333
        self.assertEqual(expected, Solution.maxProfit(inventory, orders))
