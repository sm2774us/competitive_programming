#
# Time  : O(amount * coins.length)
# Space : O(amount)
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 322: Coin Change
#
# Description:
#
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0
#
# Example 4:
#
# Input: coins = [1], amount = 1
# Output: 1
#
# Example 5:
#
# Input: coins = [1], amount = 2
# Output: 2
#
# Constraints:
#   * 1 <= coins.length <= 12
#   * 1 <= coins[i] <= 231 - 1
#   * 0 <= amount <= 104
#
# **************************************************************************
# Source: https://leetcode.com/problems/coin-change/ (LeetCode - Problem 322 - Coin Change)
#         https://deltap.geeksforgeeks.org/problems/-minimum-number-of-coins/0 (GeeksForGeeks - Minimum Number of Coins)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Assume dp[i] is the fewest number of coins making up amount i,
# then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
#
# **************************************************************************
# Complexity Analysis
# **************************************************************************
# Time Complexity   : O(amount * coins.length)
# Space Complexity  : O(amount)
#
from typing import List
import math
from collections import defaultdict

import unittest


class Solution(object):
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(lambda: math.inf)
        dp[0] = 0
        coins.sort()
        for a in range(1, amount + 1):
            for c in coins:
                dp[a] = min(dp[a], dp[a - c] + 1)
        return -1 if dp[amount] == math.inf else dp[amount]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_coinChange(self) -> None:
        sol = Solution()
        for coins, amount, solution in (
            [[1, 2, 5], 11, 3],
            [[2], 3, -1],
            [[1], 0, 0],
            [[1], 1, 1],
            [[1], 2, 2],
        ):
            self.assertEqual(solution, sol.coinChange(coins, amount))


# main
if __name__ == "__main__":
    unittest.main()
