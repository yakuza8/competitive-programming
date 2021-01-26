import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
        """
        Reverse a linked list from position m to n. Do it in one-pass.
        Note: 1 ≤ m ≤ n ≤ length of list.

        Example:
            Input: 1->2->3->4->5->NULL, m = 2, n = 4
            Output: 1->4->3->2->5->NULL
        """
        if head is None or m == n:
            return head

        _prev, _next = head, None

        back_head, front_tail = None, None

        for _ in range(m - 1):
            if _ == m - 2:
                back_head = _prev
            _prev = _prev.next
        front_tail = _prev
        _next = _prev.next
        for _ in range(n - m):
            new_next = _next.next
            _next.next = _prev
            _prev, _next = _next, new_next

        if back_head is not None:
            back_head.next = _prev
        else:
            head = _prev
        if front_tail is not None:
            front_tail.next = _next
        return head


class ReverseLinkedLinkII(unittest.TestCase):
    @staticmethod
    def _print_list(head: ListNode):
        while head is not None:
            print(head.val, end=", ")
            head = head.next

    def test_case_1(self):
        head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4,
                                                                                       next=ListNode(
                                                                                           val=5)))), )
        self._print_list(head)
        print()
        head = Solution.reverseBetween(head, 2, 4)
        self._print_list(head)

    def test_case_2(self):
        head = ListNode(val=1, next=ListNode(val=5))
        self._print_list(head)
        print()
        head = Solution.reverseBetween(head, 1, 2)
        self._print_list(head)
