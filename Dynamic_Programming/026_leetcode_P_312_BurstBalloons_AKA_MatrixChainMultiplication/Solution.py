#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 312: Burst Balloons
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. If the you burst balloon i
# you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i.
# After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
# **************************************************************************
# Source: https://leetcode.com/problems/burst-balloons/ (LeetCode - Problem 312 - Burst Balloons)
# **************************************************************************
#
#
from typing import List
import math
import unittest


class Solution(object):

    # Solution_1
    #
    # If you think of bursting a balloon as multiplying two adjacent matrices,
    # then this problem is exactly the classical DP problem Matrix-chain multiplication
    # found in section 15.2 in the book Introduction to Algorithms (2nd edition).
    #
    # For example, given [3,5,8] and bursting 5, the number of coins you get is the number of scalar multiplications
    # you need to do to multiply two matrices A[3*5] and B[5*8]. So in this example, the original problem
    # is actually the same as given a matrix chain A[1*3]*B[3*5]*C[5*8]*D[8*1],
    # fully parenthesize it so that the total number of scalar multiplications is maximized,
    # although the orignal matrix-chain multiplication problem in the book asks to minimize it.
    # Then you can see it clearly as a classical DP problem.
    #
    def maxCoins_solution_1_matrix_chain_multiplication(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums) - 1
        mp = [[0 for i in range(n)] for j in range(n)]

        for p in range(1, n):
            for j in range(p, n):
                i = j - p
                mp[i][j] = max(
                    mp[i][k] + mp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1]
                    for k in range(i, j)
                )

        return mp[0][n - 1]

    # Solution_2 : Top Down DP
    #
    # Analysis:
    # We need to find a way to divide the problems. If we start from the first balloon,
    # we can't determine the left/right for the number in each sub-problem, If we start from the last balloon, we can.
    #
    # We can see the transformation equation is very similar to the one for matrix multiplication.
    #
    # dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) # i < k < j
    # This is a typical interval DP problem. Because the order of the number extracted matters,
    # we need to do a O(n^3) DP. If we only need to expand the interval to the left or right,
    # we only need to do a O(n^2) DP.
    def maxCoins_solution_2_top_down_DP(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(
                    coins,
                    nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j),
                )
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)

    # Solution_3 : Bottom Up DP
    #
    def maxCoins_solution_3_bottom_up_DP(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]  # padding
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for i in range(left + 1, right):
                    # dp[left][right] = the maximum coins we get after bursting all the balloons between left and right (excluding left and right themselves)
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right],
                    )
                    # maximum coins of bursting all the balloon on the left side of i
                    # maximum value of bursting all the balloon on the right side of i
                    # bursting balloon i last when left side and right side are gone
        return dp[0][
            n - 1
        ]  # since we pad nums on both sides with [1], it really covers the entire range of the original nums (remember boundaries are excluded)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxCoins(self) -> None:
        sol = Solution()
        nums = [3, 1, 5, 8]
        self.assertEqual(167, sol.maxCoins_solution_1_matrix_chain_multiplication(nums))
        self.assertEqual(167, sol.maxCoins_solution_2_top_down_DP(nums))
        self.assertEqual(167, sol.maxCoins_solution_3_bottom_up_DP(nums))


# main
if __name__ == "__main__":
    unittest.main()
