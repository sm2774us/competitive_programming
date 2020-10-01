#
# Time : O(logN); Space: O(1)
# @tag : Recursion
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 390: Elimination Game
#
# Description:
#
# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
#
# Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6
#
# **************************************************************************
# Source: https://leetcode.com/problems/elimination-game/ (Leetcode - Problem 390 - Elimination Game)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Basically we calculate the next starting point, and we go forward and backwards each time.
# Step gets multiplied by two at each loop iteration.
# Complexity is θ(log N) because we divide n by 2 at each iteration. Size complexity is O(1).
#
#
import unittest


class Solution:
    # Recursive Solution
    def lastRemainingRecursive(self, n: int) -> int:
        def game(nums):
            return nums[0] if len(nums) == 1 else game(nums[1::2][::-1])

        return game(range(1, n + 1))

    # Iterative Solution
    def lastRemainingIterative(self, n: int) -> int:
        nums = range(1, n + 1)
        while len(nums) > 1:
            nums = nums[1::2][::-1]
        return nums[0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lastRemaining(self) -> None:
        sol = Solution()
        self.assertEqual(
            6,
            sol.lastRemainingRecursive(9),
            "Should return the last number that remains starting with a list of length n",
        )
        self.assertEqual(
            6,
            sol.lastRemainingIterative(9),
            "Should return the last number that remains starting with a list of length n",
        )


if __name__ == "__main__":
    unittest.main()
