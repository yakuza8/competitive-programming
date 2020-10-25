import unittest
from typing import List


class Solution:
    @staticmethod
    def max_equal_row_after_some_flip(matrix: List[List[int]]) -> int:
        """
        Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in
        that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

        Return the maximum number of rows that have all values equal after some number of flips.

        Example 1:
        Input: [[0,1],[1,1]]
        Output: 1
        Explanation: After flipping no values, 1 row has all values equal.

        Example 2:
        Input: [[0,1],[1,0]]
        Output: 2
        Explanation: After flipping values in the first column, both rows have equal values.

        Example 3:
        Input: [[0,0,0],[0,0,1],[1,1,0]]
        Output: 2
        Explanation: After flipping values in the first two columns, the last two rows have equal values.

        Runtime: 1752 ms, faster than 61.14% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
        Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.

        Runtime: 1648 ms, faster than 89.14% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
        Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
        """
        '''
        from collections import defaultdict
        count_dict = defaultdict(int)
        decimal_count = len(matrix[0])
        max_number = (2 ** decimal_count) - 1
        middle = max_number / 2
        for row in matrix:
            summed_row = int(''.join((str(i) for i in row)), 2)
            count_dict[summed_row if summed_row < middle else max_number - summed_row] += 1
        return max(count_dict.values())
        '''
        from collections import Counter
        decimal_count = len(matrix[0])
        max_number = (2 ** decimal_count) - 1
        middle = max_number / 2
        r = []
        for row in matrix:
            res = 0
            for ele in row:
                res = (res << 1) | ele
            r.append(res if res < middle else max_number - res)
        count_dict = Counter(r)

        return count_dict.most_common()[0][1]


class MaxEqualRowAfterSomeFlip(unittest.TestCase):

    def test_case_1(self):
        m = [[0, 1], [1, 1]]
        self.assertEqual(1, Solution.max_equal_row_after_some_flip(m))

    def test_case_2(self):
        m = [[0, 1], [1, 0]]
        self.assertEqual(2, Solution.max_equal_row_after_some_flip(m))

    def test_case_3(self):
        m = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
        self.assertEqual(2, Solution.max_equal_row_after_some_flip(m))
