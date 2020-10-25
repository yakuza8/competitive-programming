from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def isValidSequence(root: TreeNode, arr: List[int]) -> bool:
        """
        Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given
        string is a valid sequence in such binary tree.

        We get the given string from the concatenation of an array of integers arr and the concatenation of all values
        of the nodes along a path results in a sequence in the given binary tree.

        Example 1:
        ----------------------------------------------------------------------------------------------------------------
        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
        Output: true
        Explanation:
        The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
        Other valid sequences are:
        0 -> 1 -> 1 -> 0
        0 -> 0 -> 0

        Example 2:
        ----------------------------------------------------------------------------------------------------------------
        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
        Output: false
        Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

        Example 3:
        ----------------------------------------------------------------------------------------------------------------
        Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
        Output: false
        Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

        Constraints:
            1 <= arr.length <= 5000
            0 <= arr[i] <= 9
            Each node's value is between [0 - 9].
        """
        '''
        def helper(_root: TreeNode, _arr: List[int]) -> bool:
            is_array_empty = not bool(_arr)
            is_root_none = _root is None
            if is_root_none and is_array_empty:
                return True
            elif (not is_root_none and is_array_empty) or (is_root_none and not is_array_empty):
                return False
            else:
                current_value = _root.val
                expected_value, *remaining_array = _arr
                print('Current value:', current_value, '; Expected value:', expected_value, '; Remaining:', remaining_array)

                if current_value == expected_value:
                    return helper(_root.left, remaining_array) or helper(_root.right, remaining_array)
                else:
                    return False
        '''

        def helper(_root: TreeNode, _arr: List[int]) -> bool:
            is_array_empty = not bool(_arr)
            is_root_none = _root is None
            if is_root_none or (not is_root_none and is_array_empty):
                print('Root:', _root, '; Array:', _arr, '; Returning False')
                return False
            else:
                current_value = _root.val
                expected_value, *remaining_array = _arr
                print('Current value:', current_value, '; Expected value:', expected_value, '; Remaining:',
                      remaining_array)

                if current_value == expected_value:
                    if not bool(remaining_array):
                        print('Array empty; Returning is_leaf:', is_leaf(_root))
                        return is_leaf(_root)
                    return helper(_root.left, remaining_array) or helper(_root.right, remaining_array)
                else:
                    return False

        def is_leaf(_root: TreeNode):
            if _root is None:
                return False
            return _root.left is None and _root.right is None

        return helper(root, arr)
