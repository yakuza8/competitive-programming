import unittest
from enum import Enum
from typing import List


class State(Enum):
    DEATH = 0
    LIVE = 1


class Transition(Enum):
    DEATH_TO_DEATH = -1
    DEATH_TO_LIVE = 0
    LIVE_TO_DEATH = 1
    LIVE_TO_LIVE = 2


class Solution:
    @staticmethod
    def gameOfLife(board: List[List[int]]) -> None:
        """
        According to Wikipedia's article: "The Game of Life, also known simply as Life, is a
        cellular automaton devised by the British mathematician John Horton Conway in 1970."

        The board is made up of an m x n grid of cells, where each cell has an initial state: live
        (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight
        neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the
        above Wikipedia article):

        Any live cell with fewer than two live neighbors dies as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population.
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        The next state is created by applying the above rules simultaneously to every cell in the
        current state, where births and deaths occur simultaneously. Given the current state of the
        m x n grid board, return the next state.
        """
        row_len, column_len = len(board), len(board[0])

        for row_index in range(row_len):
            for column_index in range(column_len):
                live_cell = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        tr, tl = row_index + i, column_index + j
                        if 0 <= tr < row_len and 0 <= tl < column_len:
                            if board[tr][tl] >= Transition.LIVE_TO_DEATH.value:
                                live_cell += 1
                current_cell = board[row_index][column_index]
                if current_cell == State.DEATH.value:
                    if live_cell == 3:
                        board[row_index][column_index] = Transition.DEATH_TO_LIVE.value
                    else:
                        board[row_index][column_index] = Transition.DEATH_TO_DEATH.value
                else:
                    if live_cell <= 1:
                        board[row_index][column_index] = Transition.LIVE_TO_DEATH.value
                    elif live_cell <= 3:
                        board[row_index][column_index] = Transition.LIVE_TO_LIVE.value
                    else:
                        board[row_index][column_index] = Transition.LIVE_TO_DEATH.value

        for row_index in range(row_len):
            for column_index in range(column_len):
                transition = board[row_index][column_index]
                if transition in (Transition.DEATH_TO_DEATH.value, Transition.LIVE_TO_DEATH.value):
                    board[row_index][column_index] = State.DEATH.value
                else:
                    board[row_index][column_index] = State.LIVE.value


class GameOfLife(unittest.TestCase):
    def test_case_1(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        Solution.gameOfLife(board)
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.assertListEqual(board, expected)

    def test_case_2(self):
        board = [[1, 1], [1, 0]]
        Solution.gameOfLife(board)
        expected = [[1, 1], [1, 1]]
        self.assertListEqual(board, expected)
