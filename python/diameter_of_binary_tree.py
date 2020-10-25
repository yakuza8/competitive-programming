# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def diameterOfBinaryTree(root: TreeNode) -> int:
        """
         Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree
         is the length of the longest path between any two nodes in a tree. This path may or may not pass through the
         root.

        Example:
        Given a binary tree

                  1
                 / \
                2   3
               / \
              4   5

        Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

        Note: The length of path between two nodes is represented by the number of edges between them.
        """

        def helper(r: TreeNode):
            if r is None:
                return -1, -1, -1
            else:
                l_left, l_right, l_max = helper(r.left)
                r_left, r_right, r_max = helper(r.right)

                root_left = max(l_left, l_right)
                root_right = max(r_left, r_right)

                return root_left + 1, root_right + 1, max(l_max, r_max, root_left + root_right + 2)

        return helper(root)[2]
