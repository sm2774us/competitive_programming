#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 877: Stone Game
#
# Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
#
# The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
#
#
#
# Example 1:
#
# Input: piles = [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
#
#
# Constraints:
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
#
# **************************************************************************
# Source: https://leetcode.com/problems/stone-game/ (LeetCode - Problem 877 - Stone Game)
# **************************************************************************
#
#
# References:
# **************************************************************************
# https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
# https://leetcode.com/problems/stone-game/discuss/154604/Python-recursive-dp-mini-max
# https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
#
#
from typing import List
from functools import lru_cache

import unittest


class Solution(object):

    # Solution_1
    #
    def stoneGame_solution_1_minimax(self, piles: List[int]) -> bool:
        """
        :type piles: List[int]
        :rtype: bool
        """

        @lru_cache(None)
        def pmin(i, j):
            if i == j:
                return 0
            return min(pmax(i + 1, j), pmax(i, j - 1))

        @lru_cache(None)
        def pmax(i, j):
            if i == j:
                return piles[i]
            return max(piles[i] + pmin(i + 1, j), pmin(i, j - 1) + piles[j])

        p1 = pmax(0, len(piles) - 1)
        p2 = sum(piles) - p1
        return p1 > p2

    # Solution_2 : minimax idea - DP 2D solution
    #
    def stoneGame_solution_2_minimax_DP_2D(self, piles: List[int]) -> bool:
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles) - 1, -1, -1):
            for j in range(
                i + 1, len(piles), 2
            ):  # j>i and (j-i+1) is even | make it faster
                if i + 1 == j:
                    dp[i][j] = max(piles[i], piles[j])
                else:
                    dp[i][j] = max(
                        piles[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                        piles[j] + min(dp[i + 1][j - 1], dp[i][j - 2]),
                    )

        return dp[0][-1] > sum(piles) - dp[0][-1]

    def stoneGame_solution_3_DP_1D(self, piles: List[int]) -> bool:
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_stoneGame(self) -> None:
        sol = Solution()
        piles = [5, 3, 4, 5]
        self.assertEqual(True, sol.stoneGame_solution_1_minimax(piles))
        self.assertEqual(True, sol.stoneGame_solution_2_minimax_DP_2D(piles))
        self.assertEqual(True, sol.stoneGame_solution_3_DP_1D(piles))


# main
if __name__ == "__main__":
    unittest.main()
