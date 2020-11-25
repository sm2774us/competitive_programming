#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 51: N-Queens
#
# Description:
#
# Refer to LeetCode_Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/n-queens/ (LeetCode - Problem 51 - N-Queens)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):

    # Solution_1 : Backtracking Solution
    #
    # Runtime: 52 ms, faster than 95.31% of Python3 online submissions for N-Queens.
    # Memory Usage: 14.3 MB, less than 26.71% of Python3 online submissions for N-Queens.
    #
    # Goal: Place a queen somewhere such that no queen are attacking each other
    # Approach: backtracking
    # - each recursive layer will decide on a row and also the placement of the queen
    # - the constraint is making sure we do not place a queen where its in sight of another queen. How?
    #     1) make sure it is not on the same column --> create a column set
    #     2) make sure it is not in same diagonal path --> create a diagonal set (calculated via r+c)
    #     3) make sure it is not in a antidiagonal path --> create a antidiagonal set (calculated via r-c)
    #
    #     We dont need to worry about rows because it is handled by the backtracking parameter that always recurse
    #     to next level of the row
    #
    #     ** note: if you dont know why r+c and r-c are diagonal paths --> Draw it out and check why it does!!
    #
    def solveNQueens_solution_1_backtracking(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """

        if n == 0:
            return []

        col = set()
        diagonal = set()  # determined by r+c
        antidiagonal = set()  #
        output = []
        result = []

        def backtrack(r):
            nonlocal n, col, diagonal, antidiagonal, output, result
            if r == n:
                result.append(output[:])
                return

            for c in range(n):
                if c in col or (r + c) in diagonal or (r - c) in antidiagonal:
                    continue

                col.add(c)
                diagonal.add(r + c)
                antidiagonal.add(r - c)
                output.append("." * c + "Q" + "." * (n - c - 1))
                backtrack(r + 1)

                col.remove(c)
                diagonal.remove(r + c)
                antidiagonal.remove(r - c)
                output.pop()

        backtrack(0)
        return result

    def solve_queen(
        self, board, row, res, n, col_flag, major_diag_flag, minor_diag_flag
    ):

        if row == n:
            new_board = list(board)
            res.append(new_board)
        else:
            for col in range(n):
                # for the square [row, col], it is in major diagonal `n + col - row - 1` and minor diagonal `row + col`
                # this depends on how you count the major and minor diagonals.
                if (
                    col_flag[col]
                    and major_diag_flag[n + col - row - 1]
                    and minor_diag_flag[row + col]
                ):
                    board[row * n + col] = "Q"
                    col_flag[col] = 0
                    major_diag_flag[n + col - row - 1] = 0
                    minor_diag_flag[row + col] = 0

                    self.solve_queen(
                        board,
                        row + 1,
                        res,
                        n,
                        col_flag,
                        major_diag_flag,
                        minor_diag_flag,
                    )

                    board[row * n + col] = "."
                    col_flag[col] = 1
                    major_diag_flag[n + col - row - 1] = 1
                    minor_diag_flag[row + col] = 1

    # Solution_2 : DFS + Backtracking Solution
    #
    # Indeed, we dont need to try all the possible column index of the first row,
    # we can reverse the existing result to reduce time cost.
    def solveNQueens_solution_2_dfs_and_backtracking(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = ["."] * (n ** 2)
        # can use  `board = [['.'] * n for _ in range(n)]` as well, but need to use `copy.deepcopy` later to copy the list of lists

        res = []

        # flags to indicate whether the a column, a major diagonal or a minor diagonal has been occupied by a Q or not
        col_flag = [1] * n
        major_diag_flag = [1] * (2 * n - 1)
        minor_diag_flag = [1] * (2 * n - 1)

        self.solve_queen(board, 0, res, n, col_flag, major_diag_flag, minor_diag_flag)

        result = []
        for r in res:
            b = []
            for i in range(n):
                b.append("".join(r[(i * n) : ((i + 1) * n)]))

            result.append(b)

        return result

    # Solution_3 : DFS - based solution
    def solveNQueens_solution_3_using_DFS(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def DFS(valid_configs, queens, yx_diffs, yx_sums):
            """`valid_configs` contains configurations of n queens that satisfy
            threat constraints.

            Each element in `queens` represents the position of a queen.
            Its row is indicated by the element *index* and its column is
            indicated by the element *value*. Given this, duplicate values
            in `queens` would mean two rows had a queen in the same column,
            which isn't allowed.

            yx_diffs and yx_sums both represent diagonals that are threatened
            by a queen in `queens`. As shown below, diagonals can be represented
            with a single integer calculated from the difference or sum of a
            position's row and columns indices. Differences (row - col) are
            left->right diagonals and sums are right->left diagonals.

            yx_diffs (row_idx - col_idx):
            3 |  3  2  1  0
            2 |  2  1  0 -1
            1 |  1  0 -1 -2
            0 |  0 -1 -2 -3
            r  ------------
              c  0  1  2  3

            yx_sums (row_idx + col_idx):
            3 |  3  4  5  6
            2 |  2  3  4  5
            1 |  1  2  3  4
            0 |  0  1  2  3
            r  ------------
              c  0  1  2  3
            """
            row_idx = len(queens)

            if row_idx == n:
                valid_configs.append(queens)
                return

            for col_idx in range(n):
                if (
                    not col_idx in queens
                    and not row_idx - col_idx in yx_diffs
                    and not row_idx + col_idx in yx_sums
                ):
                    DFS(
                        valid_configs,
                        queens + [col_idx],
                        yx_diffs + [row_idx - col_idx],
                        yx_sums + [row_idx + col_idx],
                    )

        result = []
        DFS(result, [], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solveNQueens_LeetCode(self) -> None:
        sol = Solution()
        for n, solution in (
            [4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]],
            [1, [["Q"]]],
        ):
            self.assertEqual(solution, sol.solveNQueens_solution_1_backtracking(n))
            self.assertEqual(
                solution, sol.solveNQueens_solution_2_dfs_and_backtracking(n)
            )
            self.assertEqual(solution, sol.solveNQueens_solution_3_using_DFS(n))


# main
if __name__ == "__main__":
    unittest.main()
