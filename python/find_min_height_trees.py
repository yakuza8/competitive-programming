import unittest
from typing import List


class Solution:

    @staticmethod
    def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
        """
        For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then
        a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs)
        Given such a graph, write a function to find all the MHTs and return a list of their root labels.

        Format
        The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of
        undirected edges (each edge is a pair of labels). You can assume that no duplicate edges will appear in edges.
        Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

        Example 1 :
        Input: n = 4, edges =
                0
                |
                1
               / \
              2   3
        Output: [1]

        Example 2 :
        Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
             0  1  2
              \ | /
                3
                |
                4
                |
                5
        Output: [3, 4]

        Note:
        According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are
        connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
        The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
        """
        from collections import defaultdict
        if not edges:
            return list(range(n))

        edge_counts = defaultdict(int)
        adjacency_matrix = defaultdict(set)
        for edge in edges:
            node1, node2 = edge
            edge_counts[node1] += 1
            edge_counts[node2] += 1
            adjacency_matrix[node1].add(node2)
            adjacency_matrix[node2].add(node1)

        remaining_elements = n
        leaves = []
        non_leaves = []

        while True:
            possible_leaf_node_count = 0

            for node, edge_count in edge_counts.items():
                if edge_count == 1:
                    remaining_elements -= 1
                    leaves.append(node)
                elif edge_count == 2:
                    non_leaves.append(node)
                    possible_leaf_node_count += 1
                elif edge_count > 2:
                    non_leaves.append(node)

            if remaining_elements == 1:
                return non_leaves

            if possible_leaf_node_count == 0:
                return leaves

            for leaf in leaves:
                del edge_counts[leaf]
                for other_node in adjacency_matrix[leaf]:
                    if other_node in adjacency_matrix:
                        adjacency_matrix[other_node].remove(leaf)
                    edge_counts[other_node] -= 1
                del adjacency_matrix[leaf]

            leaves = []
            non_leaves = []


class FindMinHeightTree(unittest.TestCase):

    def test_case_1(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        expected_result = [1]
        self.assertEqual(expected_result, sorted(Solution.findMinHeightTrees(n, edges)))

    def test_case_2(self):
        n = 6
        edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        expected_result = [3, 4]
        self.assertEqual(expected_result, sorted(Solution.findMinHeightTrees(n, edges)))
