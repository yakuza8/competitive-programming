# Definition for a binary tree node.
import unittest
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({0}, {1}, {2})'.format(self.val, self.left, self.right)


class Solution:

    @staticmethod
    def bstFromPreorder(preorder: List[int]) -> TreeNode:
        """
        Return the root node of a binary search tree that matches the given preorder traversal.
        (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a
        value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder
        traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

        Example 1:
        Input: [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]


        Note:
            1 <= preorder.length <= 100
            The values of preorder are distinct.
        """
        root = None

        if preorder:
            root = TreeNode(preorder[0])
            current_head = root

            node_stack = [root]
            for value in preorder[1:]:
                current_node = TreeNode(value)
                if value < current_head.val:
                    node_stack.append(current_node)
                    current_head.left = current_node
                    current_head = current_node
                else:
                    while node_stack and node_stack[-1].val < value:
                        current_head = node_stack.pop()
                    node_stack.append(current_node)
                    current_head.right = current_node
                    current_head = current_node
                print()
        return root

    @staticmethod
    def preorder_traversal(root: TreeNode) -> List[int]:
        def helper(_root: TreeNode, accumulate_list: List[int]) -> None:
            if _root is not None:
                accumulate_list.append(_root.val)
                helper(_root.left, accumulate_list)
                helper(_root.right, accumulate_list)

        preorder = []
        helper(root, preorder)
        return preorder


class ConstructBinaryTreeFromPreorderTraversal(unittest.TestCase):

    def test_case_1(self):
        preorder = [8, 5, 1, 7, 10, 12]
        expected_result = [8, 5, 1, 7, 10, 12]
        self.assertListEqual(expected_result, Solution.preorder_traversal(Solution.bstFromPreorder(preorder)))
