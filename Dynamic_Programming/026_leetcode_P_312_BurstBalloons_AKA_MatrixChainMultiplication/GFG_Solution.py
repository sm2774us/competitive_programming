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
# Source: https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication/0 (GeeksForGeeks - Matrix Chain Multiplication)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.techiedelight.com/matrix-chain-multiplication/
#
# **************************************************************************
# Reference
# **************************************************************************
# https://www.techiedelight.com/matrix-chain-multiplication/
#
import math

import unittest


class Solution(object):
    # Solution 1:
    #
    # Time Complexity: O(2^N) [ Exponential ]
    def matrixChainMultiplication_solution_1(self, dims, i, j):

        # base case: one matrix
        if j <= i + 1:
            return 0

        # stores minimum number of scalar multiplications (i.e., cost)
        # needed to compute the matrix M[i+1]...M[j] = M[i..j]
        min = math.inf

        # take the minimum over each possible position at which the
        # sequence of matrices can be split

        """
            (M[i+1]) x (M[i+2]..................M[j])
            (M[i+1]M[i+2]) x (M[i+3.............M[j])
            ...
            ...
            (M[i+1]M[i+2]............M[j-1]) x (M[j])
        """

        for k in range(i + 1, j):

            # recur for M[i+1]..M[k] to get an i x k matrix
            cost = self.matrixChainMultiplication_solution_1(dims, i, k)

            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += self.matrixChainMultiplication_solution_1(dims, k, j)

            # cost to multiply two (i x k) and (k x j) matrix
            cost += dims[i] * dims[k] * dims[j]

            if cost < min:
                min = cost

        # return min cost to multiply M[j+1]..M[j]
        return min

    # Solution 2: Top-Down DP w/ Memoization
    def matrixChainMultiplication_solution_2_top_down_DP_with_memoization(
        self, dims, i, j, T
    ):
        # base case: one matrix
        if j <= i + 1:
            return 0

        # stores minimum number of scalar multiplications (i.e., cost)
        # needed to compute the matrix M[i+1]...M[j] = M[i..j]
        min = math.inf

        # if sub-problem is seen for the first time, solve it and
        # store its result in a lookup table
        if T[i][j] == 0:

            # take the minimum over each possible position at which the
            # sequence of matrices can be split

            """
                (M[i+1]) x (M[i+2]..................M[j])
                (M[i+1]M[i+2]) x (M[i+3.............M[j])
                ...
                ...
                (M[i+1]M[i+2]............M[j-1]) x (M[j])
            """

            for k in range(i + 1, j):

                # recur for M[i+1]..M[k] to get an i x k matrix
                cost = self.matrixChainMultiplication_solution_2_top_down_DP_with_memoization(
                    dims, i, k, T
                )

                # recur for M[k+1]..M[j] to get a k x j matrix
                cost += self.matrixChainMultiplication_solution_2_top_down_DP_with_memoization(
                    dims, k, j, T
                )

                # cost to multiply two (i x k) and (k x j) matrix
                cost += dims[i] * dims[k] * dims[j]

                if cost < min:
                    min = cost

            T[i][j] = min

        # return min cost to multiply M[j+1]..M[j]
        return T[i][j]

    # Solution 3: Bottom-Up DP
    def matrixChainMultiplication_solution_3_bottom_up_DP(self, dims):
        n = len(dims)

        # c[i,j] = minimum number of scalar multiplications (i.e., cost)
        # needed to compute the matrix M[i]M[i+1]...M[j] = M[i..j]
        # The cost is zero when multiplying one matrix
        c = [[0 for x in range(n + 1)] for y in range((n + 1))]

        for length in range(2, n + 1):  # Subsequence lengths

            for i in range(1, n - length + 2):

                j = i + length - 1
                c[i][j] = math.inf

                k = i
                while j < n and k <= j - 1:
                    cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                    if cost < c[i][j]:
                        c[i][j] = cost

                    k = k + 1

        return c[1][n - 1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_matrixChainMultiplication(self) -> None:
        sol = Solution()
        for dims, solution in (
            [[40, 20, 30, 10, 30], 26000],
            [[10, 20, 30, 40, 30], 30000],
            [[10, 20, 30], 6000],
        ):
            self.assertEqual(
                solution,
                sol.matrixChainMultiplication_solution_1(dims, 0, len(dims) - 1),
            )
            self.assertEqual(
                solution,
                sol.matrixChainMultiplication_solution_2_top_down_DP_with_memoization(
                    dims,
                    0,
                    len(dims) - 1,
                    [[0 for x in range(len(dims))] for y in range(len(dims))],
                ),
            )
            self.assertEqual(
                solution, sol.matrixChainMultiplication_solution_3_bottom_up_DP(dims)
            )


# main
if __name__ == "__main__":
    unittest.main()
