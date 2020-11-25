#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 52: N-Queens II
#
# Description:
#
# Refer to LeetCode_Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/n-queens-ii/ (LeetCode - Problem 52 - N-Queens II)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):
    def totalNQueens(
        self,
        n: int,
        diag1: set = set(),
        diag2: set = set(),
        cols: set = set(),
        row: int = 0,
    ) -> int:
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in cols:
                continue
            diag1.add(row + col)
            diag2.add(row - col)
            cols.add(col)

            count += self.totalNQueens(n, diag1, diag2, cols, row + 1)

            diag1.remove(row + col)
            diag2.remove(row - col)
            cols.remove(col)
        return count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solveNQueens_LeetCode(self) -> None:
        sol = Solution()
        for n, solution in ([4, 2], [1, 1]):
            self.assertEqual(solution, sol.totalNQueens(n))


# main
if __name__ == "__main__":
    unittest.main()
