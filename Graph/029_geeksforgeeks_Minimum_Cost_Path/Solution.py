#
# Time  : O(N*M)
# Space : O(N*M)
# @tag : Graph ; Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Minimum Cost Path
#
# Description:
#
# Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum. You can move in 4 directions : up, down, left an right.
#
# Note : It is assumed that negative cost cycles do not exist in input matrix.
#
# Input:
# The first line of input will contain number of testcases T. Then T test cases follow. Each test case contains 2 lines. The first line of each test case contains an integer N denoting the size of the grid. Next line of each test contains a single line containing N*N space separated integers depicting the cost of respective cell from (0,0) to (N,N).
#
# Output:
# For each test case output a single integer depecting the minimum cost to reach the destination.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= grid[i][j] <= 104
#
# Example:
# Input:
# 2
# 5
# 31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
# 2
# 42 93 7 14
#
# Output:
# 327
# 63
#
# Explanation:
# Testcase 1:
# Grid is:
# 31, 100, 65, 12, 18,
# 10, 13, 47, 157, 6,
# 100. 113, 174, 11, 33,
# 88, 124, 41, 20, 140,
# 99, 32, 111, 41, 20
# A cost grid is given in below diagram, minimum
# cost to reach bottom right from top left
# is 327 (31 + 10 + 13 + 47 + 65 + 12 + 18 + 6 + 33 + 11 + 20 + 41 + 20)
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-cost-path/0 (GeeksForGeeks - Minimum Cost Path)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List

import unittest

# Dynamic Programming Python implementation of Min Cost Path
# problem
R = 3
C = 3


class Solution:
    def minCost(self, cost: List[int], m: int, n: int) -> int:

        # Instead of following line, we can use int tc[m+1][n+1] or
        # dynamically allocate memoery to save space. The following
        # line is used to keep te program simple and make it working
        # on all compilers.
        tc = [[0 for x in range(C)] for x in range(R)]

        tc[0][0] = cost[0][0]

        # Initialize first column of total cost(tc) array
        for i in range(1, m + 1):
            tc[i][0] = tc[i - 1][0] + cost[i][0]

            # Initialize first row of tc array
        for j in range(1, n + 1):
            tc[0][j] = tc[0][j - 1] + cost[0][j]

            # Construct rest of the tc array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tc[i][j] = (
                    min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]
                )

        return tc[m][n]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minCost(self) -> None:
        sol = Solution()
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        self.assertEqual(8, sol.minCost(cost, 2, 2))


# main
if __name__ == "__main__":
    # Driver program to test above functions
    sol = Solution()
    cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    print(sol.minCost(cost, 2, 2))
    unittest.main()
