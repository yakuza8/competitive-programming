import unittest


class Solution:

    @staticmethod
    def alphabetBoardPath(target: str) -> str:
        """
        On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
        Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

        We may make the following moves:
            'U' moves our position up one row, if the position exists on the board;
            'D' moves our position down one row, if the position exists on the board;
            'L' moves our position left one column, if the position exists on the board;
            'R' moves our position right one column, if the position exists on the board;
            '!' adds the character board[r][c] at our current position (r, c) to the answer.

        (Here, the only positions that exist on the board are positions with letters on them.)
        Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
        You may return any path that does so.

        Example 1:
        Input: target = "leet"
        Output: "DDR!UURRR!!DDD!"

        Example 2:
        Input: target = "code"
        Output: "RR!DDRR!UUL!R!"

        Constraints:
            1 <= target.length <= 100
            target consists only of English lowercase letters.

        Runtime: 28 ms, faster than 66.39% of Python3 online submissions for Alphabet Board Path.
        Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Alphabet Board Path.
        """
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        char_position_map = {}
        for row_index, row in enumerate(board):
            for column_index, column in enumerate(row):
                char_position_map[column] = (row_index, column_index)

        y, x = 0, 0
        moves = []
        for target_ch in target:
            target_y, target_x = char_position_map[target_ch]

            x_move = target_x - x
            y_move = target_y - y

            x_move_string = int(abs(x_move)) * ('R' if x_move > 0 else 'L')
            y_move_string = int(abs(y_move)) * ('D' if y_move > 0 else 'U')

            if target_ch == 'z':
                moves.append(x_move_string + y_move_string)
            else:
                moves.append(y_move_string + x_move_string)
            moves.append('!')

            y, x = target_y, target_x

        return ''.join(moves)


class AlphabetBoardPath(unittest.TestCase):

    def test_case_1(self):
        target = "leet"
        expected_output = "DDR!UURRR!!DDD!"
        self.assertEqual(expected_output, Solution.alphabetBoardPath(target))

    def test_case_2(self):
        target = "code"
        expected_output = "RR!DDRR!UUL!R!"
        self.assertEqual(expected_output, Solution.alphabetBoardPath(target))
