import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data) + ' : [' + str(self.children) + ']'


class Solution:

    def __init__(self):
        self.nodes = {}
        self.queries = []
        self._path_processed = {}

    def kittys_calculations_on_a_tree(self, query):
        """
        https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem
        """
        from itertools import combinations

        result = 0
        for left, right in combinations(query, 2):
            left_path, right_path = self._path_processed[left], self._path_processed[right]

            while len(left_path) > 0 and len(right_path) > 0 and left_path[0] == right_path[0]:
                left_path = left_path[1:]
                right_path = right_path[1:]
            distance = len(left_path) + len(right_path)
            result += left * right * distance

        return int(result % (1e9 + 7))

    @staticmethod
    def _prepare_all_the_paths(head, node_set, prev_nodes, mappings):
        new_prev_node = prev_nodes[:]
        new_prev_node.append(head.data)
        if head.data in node_set:
            mappings[head.data] = new_prev_node
        for child in head.children:
            Solution._prepare_all_the_paths(child, node_set, new_prev_node, mappings)

    def read_input(self):
        n, q = map(int, input().split())
        for _ in range(n - 1):
            parent, child = sorted(map(int, input().split()))
            if parent not in self.nodes:
                parent_node = Node(parent)
                self.nodes[parent] = parent_node
            else:
                parent_node = self.nodes[parent]
            child_node = Node(child)
            self.nodes[child] = child_node
            parent_node.children.append(child_node)
        for _ in range(q):
            _ = int(input())
            nodes = set(map(int, input().split()))
            self.queries.append(nodes)

    def solve(self):
        self._prepare_all_the_paths(self.nodes[1], set.union(*[query for query in self.queries]),
                                    [], self._path_processed)

        for query in self.queries:
            result = self.kittys_calculations_on_a_tree(query)
            print(result)


class KittysCalculationsOnATree(unittest.TestCase):

    def test_case_1(self):
        s = Solution()
        s.read_input()
        s.solve()
