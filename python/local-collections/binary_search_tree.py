import unittest


class BinarySearchTree(object):
    """
    Unique item binary search tree implementation
    """

    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.root.put(key, value)

    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    def __iter__(self):
        if self.root is None:
            return None
        return self.root.__iter__()

class TreeNode(object):

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def put(self, key, value):
        if key != self.key:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key, value, parent=self)
                else:
                    self.left.put(key, value)
            else:
                if self.right is None:
                    self.right = TreeNode(key, value, parent=self)
                else:
                    self.right.put(key, value)
        else:
            print("Same value tried to be inserted. Key: {0} Value: {1}".format(key, value))

    def get(self, key):
        if self is None:
            return None
        if key == self.key:
            return self.value
        elif key < self.value:
            return self.left.get(key)
        else:
            return self.right.get(key)

    def __iter__(self):
        """
        In-order iterator of tree
        :return: Iterator of tree
        """
        if self.left is not None:
            for elem in self.left:
                yield elem
        yield (self.key, self.value)
        if self.right is not None:
            for elem in self.right:
                yield elem


class BinaryTreeUnittest(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BinarySearchTree()

    def test_case_get_1(self):
        """
        Try to get non existing item
        """
        key = 1
        self.assertIsNone(self.tree.get(key))

    def test_case_put_and_get(self):
        key = 1
        value = 2
        self.tree.put(key, value)
        obtained_value = self.tree.get(1)
        self.assertIsNotNone(value)
        self.assertEqual(value, obtained_value)

    def test_case_put_multiple_items(self):
        items = [(i, i) for i in range(5)]
        for (key, value) in items:
            self.tree.put(key, value)
        for i in self.tree:
            print(i)

    def test_iterator_empty_tree(self):
        self.assertIsNone(self.tree.__iter__())

    def test_iterator_with_items(self):
        items = [(3, 4), (8, 4), (1, 2), (2, 3), (19, 7)]
        for index, (key, value) in enumerate(items):
            self.tree.put(key, value)

            tree_as_list = list(self.tree)
            expected_list = sorted(items[:index + 1], key=lambda x: x[0])
            self.assertListEqual(expected_list, tree_as_list)


if __name__ == '__main__':
    unittest.main()
