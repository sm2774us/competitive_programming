#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 486: Predict the Winner
#
# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
#
# Example 1:
#
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
#
#
# Example 2:
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
#
#
# Constraints:
#
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.
#
# **************************************************************************
# Source: https://leetcode.com/problems/predict-the-winner/ (LeetCode - Problem 486 - Predict The Winner)
# **************************************************************************
#
# Reference:
# **************************************************************************
# https://en.wikipedia.org/wiki/Nim
#
#
from typing import List
import unittest


class Solution(object):

    # Solution_1 : Recursion with memoization
    #
    # Time Complexity   : O(n^2)
    # Space Complexity  : O(n)
    def predictTheWinner_Solution_1(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """

        def helper(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            score = max(nums[j] - helper(i, j - 1), nums[i] - helper(i + 1, j))
            memo[(i, j)] = score

            return score

        memo = {}
        return helper(0, len(nums) - 1) >= 0

    # Solution_2 : Dynamic Programming, dp[i][j] is the margin of the score when it's current player's turn and the array left are nums[i]..nums[j] inclusively.
    #
    # Time Complexity   : O(n^2)
    # Space Complexity  : O(n^2)
    def predictTheWinner_Solution_2(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = nums[:]

        for s in range(1, n):
            newdp = [0] * n
            for j in range(s, n):
                i = j - s
                newdp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

            dp = newdp
        return dp[-1] >= 0

    # Solution_2 : Dynamic Programming, dp[i][j] is the margin of the score when it's current player's turn and the array left are nums[i]..nums[j] inclusively.
    #
    # Time Complexity   : O(n^2)
    # Space Complexity  : O(n^2)
    def predictTheWinner_Solution_2(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # dp[i][j] the person's effective score when pick, facing nums[i..j]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for s in range(len(nums)):
            for i in range(len(nums) - s):
                j = i + s
                if i == j:
                    dp[i][i] = nums[i]
                else:
                    dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
        return dp[0][-1] >= 0

    # Solution_3 : the dp updates the hill diagonal which depends only on previous hill diagonal, so it could be turned to a 1-D DP.
    #
    # Time Complexity   : O(n^2)
    # Space Complexity  : O(n)
    def predictTheWinner_Solution_3(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = nums[:]

        for s in range(1, n):
            newdp = [0] * n
            for j in range(s, n):
                i = j - s
                newdp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

            dp = newdp
        return dp[-1] >= 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_predictTheWinner(self) -> None:
        sol = Solution()
        for nums, solution in ([[1, 5, 2], False], [[1, 5, 233, 7], True]):
            self.assertEqual(solution, sol.predictTheWinner_Solution_1(nums))
            self.assertEqual(solution, sol.predictTheWinner_Solution_2(nums))
            self.assertEqual(solution, sol.predictTheWinner_Solution_3(nums))


# main
if __name__ == "__main__":
    unittest.main()
