import unittest
from typing import List


class Solution:
    @staticmethod
    def odd_cells(n: int, m: int, indices: List[List[int]]) -> int:
        """
        Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices
        where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
        Return the number of cells with odd values in the matrix after applying the increment to all indices.

        Example 1:
        Input: n = 2, m = 3, indices = [[0,1],[1,1]]
        Output: 6

        Explanation: Initial matrix = [[0,0,0],[0,0,0]].
        After applying first increment it becomes [[1,2,1],[0,1,0]].
        The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

        Example 2:
        Input: n = 2, m = 2, indices = [[1,1],[0,0]]
        Output: 0
        Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.

        Constraints:
            1 <= n <= 50
            1 <= m <= 50
            1 <= indices.length <= 100
            0 <= indices[i][0] < n
            0 <= indices[i][1] < m
        """
        from collections import defaultdict
        row_dict = defaultdict(int)
        column_dict = defaultdict(int)

        for row, column in indices:
            row_dict[row] += 1
            column_dict[column] += 1

        odd_count = 0
        for row in range(n):
            row_count = row_dict[row]
            eq_check = 1 if row_count & 1 == 0 else 0
            for column in range(m):
                if column_dict[column] & 1 == eq_check:
                    odd_count += 1
        return odd_count


class OddValues(unittest.TestCase):

    def test_case_1(self):
        n = 2
        m = 3
        indeces = [[0, 1], [1, 1]]
        expected_result = 6
        self.assertEquals(expected_result, Solution.odd_cells(n, m, indeces))

    def test_case_2(self):
        n = 2
        m = 2
        indeces = [[1, 1], [0, 0]]
        expected_result = 0
        self.assertEquals(expected_result, Solution.odd_cells(n, m, indeces))
