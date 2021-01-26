# Definition for a binary tree node.
import unittest


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    """
    Serialization is converting a data structure or object into a sequence of bits so that it can be
    stored in a file or memory buffer, or transmitted across a network connection link to be
    reconstructed later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree. There is no restriction
    on how your serialization/deserialization algorithm should work. You need to ensure that a
    binary search tree can be serialized to a string, and this string can be deserialized to the
    original tree structure.

    The encoded string should be as compact as possible.

    Example 1:
    Input: root = [2,1,3]
    Output: [2,1,3]

    Example 2:
    Input: root = []
    Output: []

    Constraints:
    The number of nodes in the tree is in the range [0, 104].
    0 <= Node.val <= 104
    The input tree is guaranteed to be a binary search tree.
    """

    def serialize(self, root: TreeNode) -> str:
        """ Encodes a tree to a single string. """
        nodes = []

        def helper(_root: TreeNode):
            if _root is not None:
                nodes.append(_root.val)
                helper(_root.left)
                helper(_root.right)  # else:  #    nodes.append(str(-1))

        helper(_root=root)
        # return ','.join(nodes)
        return str(nodes)

    def deserialize(self, data: str) -> TreeNode:
        """ Decodes your encoded data to tree. """

        def helper(_root, x):
            if x == -1:
                return
            if x < _root.val:
                if _root.left is None:
                    _root.left = TreeNode(x)
                else:
                    helper(_root.left, x)
            else:
                if _root.right is None:
                    _root.right = TreeNode(x)
                else:
                    helper(_root.right, x)

        nodes = eval(data)
        if nodes == []:
            return None
        root = TreeNode(nodes[0])
        for val in nodes[1:]:
            helper(root, val)
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

class SerializeAndDeserializeUnittest(unittest.TestCase):

    def test_case_1(self):
        tree = TreeNode(2, TreeNode(1), TreeNode(3))
        ser = Codec()
        tree_ser = ser.serialize(root=tree)
        new_tree = ser.deserialize(tree_ser)

    def test_case_2(self):
        tree = None
        ser = Codec()
        tree_ser = ser.serialize(root=tree)
        new_tree = ser.deserialize(tree_ser)
