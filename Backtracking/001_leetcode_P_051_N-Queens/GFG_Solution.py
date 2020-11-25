#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks : N-Queen Problem
#
# Description:
#
# Refer to GFG_Problem_Description.md
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/n-queen-problem/0 (GeeksForGeeks - N-Queen Problem)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
#
#
from typing import List
from io import StringIO

import unittest


class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Append(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()


class Solution(object):
    def stringify_lst(self, lst, n):
        sb = StringBuilder()
        sb.Append("[")
        for i in range(n):
            for j in range(n):
                if lst[j][i] == 1:
                    sb.Append(str(j + 1))
                    sb.Append(" ")
        sb.Append("] ")
        return str(sb)

    def printlst(self, lst, n):
        print("[", end="")
        for i in range(n):
            for j in range(n):
                if lst[j][i] == 1:
                    print(j + 1, end=" ")
        print("]", end=" ")

    def safe(self, lst, row, col, n):
        for i in range(col):
            if lst[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if lst[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if lst[i][j] == 1:
                return False
        return True

    def solve(self, lst, n, col):
        if col == n:
            self.printlst(lst, n)
            return True
        res = False
        for i in range(n):
            if self.safe(lst, i, col, n):
                lst[i][col] = 1
                res = self.solve(lst, n, col + 1) or res
                lst[i][col] = 0
        return res

    def solve_and_return_str(self, lst, n, col):
        if col == n:
            res = self.stringify_lst(lst, n)
            return res
        sb = StringBuilder()
        for i in range(n):
            if self.safe(lst, i, col, n):
                lst[i][col] = 1
                sb.Append(self.solve_and_return_str(lst, n, col + 1))
                lst[i][col] = 0
        return str(sb)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solveNQueens_GeeksForGeeks(self) -> None:
        sol = Solution()
        n = 4
        lst = [[0 for i in range(n)] for i in range(n)]
        if sol.solve(lst, n, 0) == False:
            print("-1")
        else:
            print()
        self.assertEqual(
            "[2 4 1 3 ] [3 1 4 2 ]", sol.solve_and_return_str(lst, n, 0)[:-1]
        )


# main
if __name__ == "__main__":
    unittest.main()
