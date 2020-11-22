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
# Source: https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1 (GeeksForGeeks - Minimum sum partition)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.techiedelight.com/minimum-sum-partition-problem/
#
#
import sys
from typing import List

import unittest

n = 3


class Solution(object):
    # Partition the set S into two subsets S1, S2 such that the
    # difference between the sum of elements in S1 and the sum
    # of elements in S2 is minimized
    def minPartition(self, S: List[int], n: int, S1: int = 0, S2: int = 0) -> int:
        # base case: if list becomes empty, return the absolute
        # difference between two sets
        if n < 0:
            return abs(S1 - S2)

        # Case 1. include current item in the subset S1 and recur
        # for remaining items (n - 1)
        inc = self.minPartition(S, n - 1, S1 + S[n], S2)

        # Case 2. exclude current item from subset S1 and recur for
        # remaining items (n - 1)
        exc = self.minPartition(S, n - 1, S1, S2 + S[n])

        return min(inc, exc)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLongestOverAll(self) -> None:
        sol = Solution()
        for S, solution in ([[10, 20, 15, 5, 25], 5], [[1, 6, 11, 5], 1], [[1, 4], 3]):
            self.assertEqual(solution, sol.minPartition(S, len(S) - 1))


# main
if __name__ == "__main__":
    unittest.main()
