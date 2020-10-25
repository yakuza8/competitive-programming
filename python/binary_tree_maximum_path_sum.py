# Definition for a binary tree node.
from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def maxPathSum(root: TreeNode) -> int:
        """
        Given a non-empty binary tree, find the maximum path sum.

        For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
        along the parent-child connections. The path must contain at least one node and does not need to go through the
        root.

        Example 1:
        ----------------------------------------------------------------------------------------------------------------
        Input: [1,2,3]

               1
              / \
             2   3

        Output: 6

        Example 2:
        ----------------------------------------------------------------------------------------------------------------
        Input: [-10,9,20,null,null,15,7]

           -10
           / \
          9  20
            /  \
           15   7

        Output: 42
        """

        def helper(_root: TreeNode) -> Tuple[int, int, int]:
            # print('Current value:', 'None' if _root is None else _root.val)
            if _root is None:
                return float('-inf'), float('-inf'), float('-inf')
            else:
                left_max, left_left, left_right = helper(_root.left)
                right_max, right_left, right_right = helper(_root.right)

                current_value = _root.val
                root_left_left = max(current_value + left_left, current_value)
                root_left_right = max(current_value + left_right, current_value)
                root_right_left = max(current_value + right_left, current_value)
                root_right_right = max(current_value + right_right, current_value)

                root_left = max(root_left_left, root_left_right)
                root_right = max(root_right_left, root_right_right)

                return_value = (
                    max(current_value, left_max, right_max, root_left, root_right, root_left + root_right - current_value),
                    root_left, root_right)
                # print('Current value:', current_value, '; Return:', return_value)
                return return_value

        return max(helper(root))
