#
# Time  : O(n^2)
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Find the longest path in a matrix with given constraints
#
# Description:
#
# Given a n*n matrix where all numbers are distinct, find the maximum length path
# (starting from any cell) such that all cells along the path are in increasing order
# with a difference of 1.
#
# We can move in 4 directions from a given cell (i, j), i.e.,
# we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1)
# with the condition that the adjacent cells have a difference of 1.
#
# Example:
#
# Input:  mat[][] = {{1, 2, 9}
#                    {5, 3, 8}
#                    {4, 6, 7}}
# Output: 4
# The longest path is 6-7-8-9.
#
# **************************************************************************
# Source: https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/ (GeeksForGeeks - Find the longest path in a matrix with given constraints)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://tutorialspoint.dev/algorithm/dynamic-programming-algorithms/find-the-longest-path-in-a-matrix-with-given-constraints
#
# **************************************************************************
# Reference
# **************************************************************************
# https://www.techiedelight.com/rot-cutting/
#
import sys
from typing import List

import unittest

n = 3


class Solution(object):
    # Returns length of the longest path beginning with mat[i][j].
    # This function mainly uses lookup table dp[n][n]
    def findLongestFromACell(
        self, i: int, j: int, mat: List[List[int]], dp: List[List[int]]
    ) -> List[List[int]]:
        # Base case
        if i < 0 or i >= n or j < 0 or j >= n:
            return 0

        # If this subproblem is already solved
        if dp[i][j] != -1:
            return dp[i][j]

            # Since all numbers are unique and in range from 1 to n*n,
        # there is atmost one possible direction from any cell
        if j < n - 1 and ((mat[i][j] + 1) == mat[i][j + 1]):
            dp[i][j] = 1 + self.findLongestFromACell(i, j + 1, mat, dp)
            return dp[i][j]

        if j > 0 and (mat[i][j] + 1 == mat[i][j - 1]):
            dp[i][j] = 1 + self.findLongestFromACell(i, j - 1, mat, dp)
            return dp[i][j]

        if i > 0 and (mat[i][j] + 1 == mat[i - 1][j]):
            dp[i][j] = 1 + self.findLongestFromACell(i - 1, j, mat, dp)
            return dp[i][j]

        if i < n - 1 and (mat[i][j] + 1 == mat[i + 1][j]):
            dp[i][j] = 1 + self.findLongestFromACell(i + 1, j, mat, dp)
            return dp[i][j]

            # If none of the adjacent fours is one greater
        dp[i][j] = 1
        return dp[i][j]

    # Returns length of the longest path beginning with any cell
    def findLongestOverAll(self, mat: List[List[int]]) -> int:
        result = 1  # Initialize result

        # Create a lookup table and fill all entries in it as -1
        dp = [[-1 for i in range(n)] for i in range(n)]

        # Compute longest path beginning from all cells
        for i in range(n):
            for j in range(n):
                if dp[i][j] == -1:
                    self.findLongestFromACell(i, j, mat, dp)
                    # Update result if needed
                result = max(result, dp[i][j])
        return result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLongestOverAll(self) -> None:
        sol = Solution()
        mat = [[1, 2, 9], [5, 3, 8], [4, 6, 7]]
        self.assertEqual(4, sol.findLongestOverAll(mat))


# main
if __name__ == "__main__":
    unittest.main()
