import unittest
from typing import List


class Solution:
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word, return true if word exists in the
        grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent
        cells are horizontally or vertically neighboring. The same letter cell may not be used more
        than once.

        Example 1:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: true

        Example 2:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        Output: true

        Example 3:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
        Output: false

        Constraints:
            m == board.length
            n = board[i].length
            1 <= m, n <= 6
            1 <= word.length <= 15
            board and word consists of only lowercase and uppercase English letters.


        Follow up: Could you use search pruning to make your solution faster with a larger board?
        """
        max_row, max_column = len(board), len(board[0])
        for row_index in range(max_row):
            for column_index in range(max_column):
                visited_set = set()
                if Solution.dfs(board=board, row_index=row_index, column_index=column_index,
                                visited_set=visited_set, word=word, max_row=max_row,
                                max_column=max_column):
                    return True
        return False

    @staticmethod
    def dfs(board, row_index, column_index, visited_set, word, max_row, max_column):
        current_index = (row_index, column_index)
        # If the word is processed fully
        if not word:
            return True
        # If we already visit this index
        if current_index in visited_set:
            return False
        # If we have a matching first character
        if board[row_index][column_index] == word[0]:
            if len(word) == 1:
                return True
            visited_set.add(current_index)
            changes = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dy, dx in changes:
                new_row, new_column = row_index + dy, column_index + dx
                if 0 <= new_row < max_row and 0 <= new_column < max_column:
                    result = Solution.dfs(board=board, row_index=new_row, column_index=new_column,
                                          visited_set=visited_set, word=word[1:], max_row=max_row,
                                          max_column=max_column)
                    if result:
                        return True

            visited_set.remove(current_index)
        return False


class WordSearch(unittest.TestCase):

    def test_case_1(self):
        board, word = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'
        expected_result = True
        self.assertEqual(expected_result, Solution.exist(board=board, word=word))

    def test_case_2(self):
        board, word = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'
        expected_result = True
        self.assertEqual(expected_result, Solution.exist(board=board, word=word))

    def test_case_3(self):
        board, word = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'
        expected_result = False
        self.assertEqual(expected_result, Solution.exist(board=board, word=word))

    def test_case_4(self):
        board, word = [['a']], 'a'
        expected_result = True
        self.assertEqual(expected_result, Solution.exist(board=board, word=word))
