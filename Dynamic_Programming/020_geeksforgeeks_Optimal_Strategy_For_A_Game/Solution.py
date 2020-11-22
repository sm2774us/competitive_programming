#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Optimal Strategy For A Game
#
# Description:
#
# You are given an array A of size N. The array contains integers and is of even length.
# The elements of the array represent N coin of values V1, V2, ....Vn.
# You play against an opponent in an alternating way.
#
# In each turn, a player selects either the first or last coin from the row, removes it from the row permanently,
# and receives the value of the coin.
#
# You need to determine the maximum possible amount of money you can win if you go first.
#
# Example 1:
#
# Input:
# N = 4
# A[] = {5,3,7,10}
# Output: 15
# Explanation: The user collects maximum
# value as 15(10 + 5)

# Example 2:
#
# Input:
# N = 4
# A[] = {8,15,3,7}
# Output: 22
# Explanation: The user collects maximum
# value as 22(7 + 15)

# Your Task:
# Complete the function maximumAmount() which takes an array arr[] (represent values of N coins) and N
# as number of coins as a parameter and returns the maximum possible amount of money you can win if you go first.
#
# Expected Time Complexity : O(N*N)
# Expected Auxiliary Space: O(N*N)
#
# Constraints:
# 2 <= N <= 100
# 1 <= Ai <= 106
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1 (GeeksForGeeks - Optimal Strategy For A Game)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
# Refer to Optimized_Solution_Explanation.md
#
# **************************************************************************
# Reference
# **************************************************************************
# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-set-2/
#
from typing import List
import math

import unittest


class Solution(object):
    # Solution 1: Recursive Solution
    #
    # TC: O(N^2)    : Use of a nested for loop brings the time complexity to n2.
    # SC: O(N^2)    : As a 2-D table is used for storing states.
    def optimalStrategyOfGame_Solution_1(self, arr: List[int], n: int) -> int:

        # Create a table to store
        # solutions of subproblems
        table = [[0 for i in range(n)] for i in range(n)]

        # Fill table using above recursive
        # formula. Note that the table is
        # filled in diagonal fashion
        # (similar to http://goo.gl / PQqoS),
        # from diagonal elements to
        # table[0][n-1] which is the result.
        for gap in range(n):
            for j in range(gap, n):
                i = j - gap

                # Here x is value of F(i + 2, j),
                # y is F(i + 1, j-1) and z is
                # F(i, j-2) in above recursive
                # formula
                x = 0
                if (i + 2) <= j:
                    x = table[i + 2][j]
                y = 0
                if (i + 1) <= (j - 1):
                    y = table[i + 1][j - 1]
                z = 0
                if i <= (j - 2):
                    z = table[i][j - 2]
                table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
        return table[0][n - 1]

    # python program to find out maximum value from a
    # given sequence of coins
    def oSRec(self, arr: List[int], i: int, j: int, sum_of_array: int) -> int:
        if j == i + 1:
            return max(arr[i], arr[j])

        # For both of your choices, the opponent
        # gives you total Sum minus maximum of
        # his value
        return max(
            (sum_of_array - self.oSRec(arr, i + 1, j, sum_of_array - arr[i])),
            (sum_of_array - self.oSRec(arr, i, j - 1, sum_of_array - arr[j])),
        )

    # Solution 2: Optimized Recursive Solution
    #
    def optimalStrategyOfGame_Solution_2(self, arr: List[int], n: int) -> int:
        sum_of_array = 0
        sum_of_array = sum(arr)
        return self.oSRec(arr, 0, n - 1, sum_of_array)

    # Solution 3: Memoization Based Solution
    #
    def optimalStrategyOfGame_Solution_3(self, arr: List[int], n: int) -> int:
        """
        :param arr: given array
        :param n: given size of array
        :return: Integer
        """
        table = [[0] * n for x in range(n)]
        for gap in range(0, n):
            for j in range(gap, n):
                i = j - gap

                x = 0
                if (i + 2) <= j:
                    x = table[i + 2][j]
                y = 0
                if (i + 1) <= (j - 1):
                    y = table[i + 1][j - 1]
                z = 0
                if i <= (j - 2):
                    z = table[i][j - 2]
                table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))

        return table[0][n - 1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_optimalStrategyOfGame(self) -> None:
        sol = Solution()
        for arr, solution in ([[5, 3, 7, 10], 15], [[8, 15, 3, 7], 22]):
            self.assertEqual(
                solution, sol.optimalStrategyOfGame_Solution_1(arr, len(arr))
            )
            self.assertEqual(
                solution, sol.optimalStrategyOfGame_Solution_2(arr, len(arr))
            )
            self.assertEqual(
                solution, sol.optimalStrategyOfGame_Solution_3(arr, len(arr))
            )


# main
if __name__ == "__main__":
    unittest.main()
