import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s, tmp = [], self
        while tmp:
            s.append(str(tmp.val))
            tmp = tmp.next
        return '[' + ', '.join(s) + ']'


class Solution:
    @staticmethod
    def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the list after sorting it in ascending order.

        Example 1:
            Input: head = [4,2,1,3]
            Output: [1,2,3,4]

        Example 2:
            Input: head = [-1,5,3,4,0]
            Output: [-1,0,3,4,5]

        Example 3:
            Input: head = []
            Output: []

        Constraints:
            The number of nodes in the list is in the range [0, 5 * 104].
            -105 <= Node.val <= 105

        """
        if not head:
            return None

        slow, fast = ListNode(next=head), head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        if head == fast:
            return head

        left, right = head, slow.next
        slow.next = None
        return Solution.merge(Solution.sortList(left), Solution.sortList(right))

    @staticmethod
    def merge(left: ListNode, right: ListNode) -> Optional[ListNode]:
        ans = tmp = ListNode()
        while left and right:
            if left.val < right.val:
                smaller, left = left, left.next
            else:
                smaller, right = right, right.next
            tmp.next = smaller
            tmp = tmp.next
        tmp.next = left if left else right
        return ans.next


class SortList(unittest.TestCase):
    def test_case_1(self):
        head = ListNode(val=4, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=3))))
        expected_result = [1, 2, 3, 4]
        self.assertEqual(str(expected_result), str(Solution.sortList(head)))

    def test_case_2(self):
        head = ListNode(val=-1, next=ListNode(val=5, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=0)))))
        expected_result = [-1, 0, 3, 4, 5]
        self.assertEqual(str(expected_result), str(Solution.sortList(head)))

    def test_case_3(self):
        head = None
        expected_result = None
        self.assertEqual(str(expected_result), str(Solution.sortList(head)))
