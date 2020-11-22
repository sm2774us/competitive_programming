#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 518: Coin Change 2
#
# Description:
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
#
# Note:
#
# You can assume that
#
#   * 0 <= amount <= 5000
#   * 1 <= coin <= 5000
#   * the number of coins is less than 500
#   * the answer is guaranteed to fit into signed 32-bit integer
#
# **************************************************************************
# Source: https://leetcode.com/problems/coin-change-2/ (LeetCode - Problem 518 - Coin Change 2)
#         https://practice.geeksforgeeks.org/problems/coin-change2448/1 (GeeksForGeeks - Coin Change)
# **************************************************************************
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
#
from typing import List

# Cartesian product of input iterables.
# Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
from itertools import product
import unittest


class Solution(object):

    # Dynamic Programming - Knapsack - Solution ( Using 2D Array )
    #
    # TC: O(amount*N)
    # SC: O(amount*N)
    #
    # where N is number of different coins, because we need only O(1) to update each cell.
    #
    # In the code I use index i+1 instead of i, because we start from 1st column, not 0th.
    #
    # Update Space complexity can be reduced to O(amount), because for every j we look at most one row back.
    # Solution for reduced space complexity => changeUsingDP_KnapSack_1D_Array_Solution
    #
    def changeUsingDP_KnapSack_2D_Array_Solution(
        self, amount: int, coins: List[int]
    ) -> int:
        # Using 2D array.
        N = len(coins)
        if N == 0:
            return int(N == amount)

        dp_sum = [[0] * N for _ in range(amount + 1)]
        for i in range(N):
            dp_sum[0][i] = 1

        for i, j in product(range(amount), range(N)):
            dp_sum[i + 1][j] = dp_sum[i + 1][j - 1]
            if i + 1 - coins[j] >= 0:
                dp_sum[i + 1][j] += dp_sum[i + 1 - coins[j]][j]

        return dp_sum[-1][-1]

    # Dynamic Programming - Knapsack - Solution ( Using 1D Array )
    #
    # TC: O(amount*N)
    # SC: O(amount)
    #
    def changeUsingDP_KnapSack_1D_Array_Solution(
        self, amount: int, coins: List[int]
    ) -> int:
        # Using 1D array.
        N = len(coins)
        if N == 0:
            return int(N == amount)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] = dp[j] + dp[j - coins[i]]

        return dp[-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_change(self) -> None:
        sol = Solution()
        for amount, coins, solution in (
            [5, [1, 2, 5], 4],
            [3, [2], 0],
            [4, [1, 2, 3], 4],
            [10, [2, 5, 3, 6], 5],
        ):
            self.assertEqual(
                solution, sol.changeUsingDP_KnapSack_2D_Array_Solution(amount, coins)
            )
            self.assertEqual(
                solution, sol.changeUsingDP_KnapSack_1D_Array_Solution(amount, coins)
            )


# main
if __name__ == "__main__":
    unittest.main()
