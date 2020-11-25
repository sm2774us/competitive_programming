#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 37: Sudoku Solver
#
# Description:
#
# Refer to LeetCode_Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/sudoku-solver/ (LeetCode - Problem 37 - Sudoku Solver)
#         https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1 (GeeksForGeeks - Solve the Sudoku)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):

    col_size = 9  # len(self.board)
    row_size = 9  # len(self.board[0])
    block_col_size = 3
    block_row_size = 3
    digits = "123456789"
    empty_symbol = "."

    # Solution_1 : Backtracking Solution
    #
    # Algorithm: backtracking (dfs) in an optimal order
    #
    # Keep track of candidates of each cell.
    # Find the cell with fewest candidates. Fill the cell with one of the candidates. Update the candidates of other cells.
    # Repeat step 2 until solved. Or if the board is not solvable anymore (there's any cell that is empty but has no candidates), undo step 2 and try the next candidate.
    #
    # Result on LeetCode:
    #
    # Runtime: 40 ms, faster than 99.51% of Python3 online submissions for Sudoku Solver.
    # Memory Usage: 13.1 MB, less than 65.46% of Python3 online submissions for Sudoku Solver.
    #
    def solveSudoku_solution_1(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.init(board)
        self.solve()

    def init(self, board):
        self.board = board

        # list all empty cells. a `cell` is a tuple `(row_index, col_index)`
        self.empty_cells = set(
            [
                (ri, ci)
                for ri in range(self.row_size)
                for ci in range(self.col_size)
                if self.board[ri][ci] == self.empty_symbol
            ]
        )

        # find candidates of each cell
        self.candidates = [
            [set(self.digits) for ci in range(self.col_size)]
            for ri in range(self.row_size)
        ]
        for ri in range(self.row_size):
            for ci in range(self.col_size):
                digit = self.board[ri][ci]
                if digit != self.empty_symbol:
                    self.candidates[ri][ci] = set()
                    self.update_candidates((ri, ci), digit)

    def solve(self):
        # if there are no empty cells, it's solved
        if not self.empty_cells:
            return True

        # get the cell with fewest candidates
        cell = min(
            self.empty_cells, key=lambda cell: len(self.candidates[cell[0]][cell[1]])
        )

        # try filling the cell with one of the candidates, and solve recursively
        ri, ci = cell
        for digit in list(self.candidates[ri][ci]):
            candidate_updated_cells = self.fill_cell(cell, digit)
            solved = self.solve()
            if solved:
                return True
            self.unfill_cell(cell, digit, candidate_updated_cells)

        # if no solution found, go back and try the next candidates
        return False

    def fill_cell(self, cell, digit):
        # fill the cell with the digit
        ri, ci = cell
        self.board[ri][ci] = digit

        # remove the cell from empty_cells
        self.empty_cells.remove(cell)

        # update the candidates of other cells
        # keep a list of updated cells. will be used when unfilling cells
        candidate_updated_cells = self.update_candidates(cell, digit)

        return candidate_updated_cells

    def unfill_cell(self, cell, digit, candidate_updated_cells):
        # unfill cell
        ri, ci = cell
        self.board[ri][ci] = self.empty_symbol

        # add the cell back to empty_cells
        self.empty_cells.add(cell)

        # add back candidates of other cells
        for ri, ci in candidate_updated_cells:
            self.candidates[ri][ci].add(digit)

    def update_candidates(self, filled_cell, digit):
        candidate_updated_cells = []
        for ri, ci in self.related_cells(filled_cell):
            if (self.board[ri][ci] == self.empty_symbol) and (
                digit in self.candidates[ri][ci]
            ):
                self.candidates[ri][ci].remove(digit)
                candidate_updated_cells.append((ri, ci))
        return candidate_updated_cells

    def related_cells(self, cell):
        return list(
            set(
                self.cells_in_same_row(cell)
                + self.cells_in_same_col(cell)
                + self.cells_in_same_block(cell)
            )
        )

    def cells_in_same_row(self, cell):
        return [(cell[0], ci) for ci in range(self.col_size)]

    def cells_in_same_col(self, cell):
        return [(ri, cell[1]) for ri in range(self.row_size)]

    def cells_in_same_block(self, cell):
        block_first_cell_ri = (cell[0] // self.block_row_size) * self.block_row_size
        block_first_cell_ci = (cell[1] // self.block_col_size) * self.block_col_size
        return [
            (block_first_cell_ri + in_block_ri, block_first_cell_ci + in_block_ci)
            for in_block_ri in range(self.block_row_size)
            for in_block_ci in range(self.block_col_size)
        ]

    # Solution_2 : DFS + Backtracking Solution
    #
    # Indeed, we dont need to try all the possible column index of the first row,
    # we can reverse the existing result to reduce time cost.
    def solveSudoku_solution_2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = [[True] * 9 for i in range(9)]
        col = [[True] * 9 for i in range(9)]
        sub = [
            [True] * 9 for i in range(9)
        ]  # 3*3 sub-box, from left to right, top to bottom.
        to_add = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = int(board[i][j]) - 1
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = False
                else:
                    to_add.append((i, j))

        def backtrack():
            if not to_add:
                return True
            i, j = to_add.pop()
            for d in range(9):
                if row[i][d] and col[j][d] and sub[i // 3 * 3 + j // 3][d]:
                    board[i][j] = str(d + 1)
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = False
                    if backtrack():
                        return True
                    board[i][j] = "."
                    row[i][d] = col[j][d] = sub[i // 3 * 3 + j // 3][d] = True
            to_add.append((i, j))
            return False

        backtrack()


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solveSudoku_solution_1(self) -> None:
        sol = Solution()
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        sudoku_solution = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        sol.solveSudoku_solution_1(board)
        self.assertEqual(sudoku_solution, board)
        board = [
            ["3", ".", "6", "5", ".", "8", "4", ".", "."],
            ["5", "2", ".", ".", ".", ".", ".", ".", "."],
            [".", "8", "7", ".", ".", ".", ".", "3", "1"],
            [".", ".", "3", ".", "1", ".", ".", "8", "."],
            ["9", ".", ".", "8", "6", "3", ".", ".", "5"],
            [".", "5", ".", ".", "9", ".", "6", ".", "."],
            ["1", "3", ".", ".", ".", ".", "2", "5", "."],
            [".", ".", ".", ".", ".", ".", ".", "7", "4"],
            [".", ".", "5", "2", ".", "6", "3", ".", "."],
        ]
        sudoku_solution = [
            ["3", "1", "6", "5", "7", "8", "4", "9", "2"],
            ["5", "2", "9", "1", "3", "4", "7", "6", "8"],
            ["4", "8", "7", "6", "2", "9", "5", "3", "1"],
            ["2", "6", "3", "4", "1", "5", "9", "8", "7"],
            ["9", "7", "4", "8", "6", "3", "1", "2", "5"],
            ["8", "5", "1", "7", "9", "2", "6", "4", "3"],
            ["1", "3", "8", "9", "4", "7", "2", "5", "6"],
            ["6", "9", "2", "3", "5", "1", "8", "7", "4"],
            ["7", "4", "5", "2", "8", "6", "3", "1", "9"],
        ]
        sol.solveSudoku_solution_1(board)
        self.assertEqual(sudoku_solution, board)

    def test_solveSudoku_solution_2(self) -> None:
        sol = Solution()
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        sudoku_solution = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        sol.solveSudoku_solution_2(board)
        self.assertEqual(sudoku_solution, board)
        board = [
            ["3", ".", "6", "5", ".", "8", "4", ".", "."],
            ["5", "2", ".", ".", ".", ".", ".", ".", "."],
            [".", "8", "7", ".", ".", ".", ".", "3", "1"],
            [".", ".", "3", ".", "1", ".", ".", "8", "."],
            ["9", ".", ".", "8", "6", "3", ".", ".", "5"],
            [".", "5", ".", ".", "9", ".", "6", ".", "."],
            ["1", "3", ".", ".", ".", ".", "2", "5", "."],
            [".", ".", ".", ".", ".", ".", ".", "7", "4"],
            [".", ".", "5", "2", ".", "6", "3", ".", "."],
        ]
        sudoku_solution = [
            ["3", "1", "6", "5", "7", "8", "4", "9", "2"],
            ["5", "2", "9", "1", "3", "4", "7", "6", "8"],
            ["4", "8", "7", "6", "2", "9", "5", "3", "1"],
            ["2", "6", "3", "4", "1", "5", "9", "8", "7"],
            ["9", "7", "4", "8", "6", "3", "1", "2", "5"],
            ["8", "5", "1", "7", "9", "2", "6", "4", "3"],
            ["1", "3", "8", "9", "4", "7", "2", "5", "6"],
            ["6", "9", "2", "3", "5", "1", "8", "7", "4"],
            ["7", "4", "5", "2", "8", "6", "3", "1", "9"],
        ]
        sol.solveSudoku_solution_2(board)
        self.assertEqual(sudoku_solution, board)


# main
if __name__ == "__main__":
    unittest.main()
