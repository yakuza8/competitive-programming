import unittest
from typing import List


class Solution:

    @staticmethod
    def minCostConnectPoints(points: List[List[int]]) -> int:
        """
        You are given an array points representing integer coordinates of some points on a 2D-plane,
        where points[i] = [xi, yi].

        The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between
        them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

        Return the minimum cost to make all points connected. All points are connected if there is
        exactly one simple path between any two points.

        Example 1:
        Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        Output: 20
        Explanation:

        We can connect the points as shown above to get the minimum cost of 20.
        Notice that there is a unique path between every pair of points.

        Example 2:
        Input: points = [[3,12],[-2,5],[-4,1]]
        Output: 18

        Example 3:
        Input: points = [[0,0],[1,1],[1,0],[-1,1]]
        Output: 4

        Example 4:
        Input: points = [[-1000000,-1000000],[1000000,1000000]]
        Output: 4000000

        Example 5:
        Input: points = [[0,0]]
        Output: 0
        """
        from heapq import heappush, heappop
        points_length = len(points)
        if points_length == 0 or points_length == 1:
            return 0

        manhattan = lambda pt1, pt2: abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

        # Prim's Algorithm
        total_min_cost = 0
        V = set(tuple(pt) for pt in points)
        T = set()
        M = []

        # Keep (cost, index) pairs in the queue and pop wrt minimum cost first
        u = V.pop()
        T.add(u)
        for _ in range(points_length - 1):
            for v in V:
                heappush(M, (manhattan(u, v), v))
            while True:
                distance, pt = heappop(M)
                if pt not in T:
                    total_min_cost += distance
                    T.add(pt)
                    V.remove(pt)
                    u = pt
                    break
        return total_min_cost


class MinCostToConnectAllPoints(unittest.TestCase):

    def test_case_1(self):
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        output = Solution.minCostConnectPoints(points)
        expected = 20
        self.assertEqual(expected, output)

    def test_case_2(self):
        points = [[3, 12], [-2, 5], [-4, 1]]
        output = Solution.minCostConnectPoints(points)
        expected = 18
        self.assertEqual(expected, output)

    def test_case_3(self):
        points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
        output = Solution.minCostConnectPoints(points)
        expected = 4
        self.assertEqual(expected, output)

    def test_case_4(self):
        points = [[-1000000, -1000000], [1000000, 1000000]]
        output = Solution.minCostConnectPoints(points)
        expected = 4000000
        self.assertEqual(expected, output)

    def test_case_5(self):
        points = [[0, 0]]
        output = Solution.minCostConnectPoints(points)
        expected = 0
        self.assertEqual(expected, output)
