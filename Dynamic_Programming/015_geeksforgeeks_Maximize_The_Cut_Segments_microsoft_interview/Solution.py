#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Maximize The Cut Segments
#
# Description:
#
# Given an integer N denoting the Length of a line segment. you need to cut the line segment
# in such a way that the cut length of a line segment each time is integer either x , y or z,
# and after performing all cutting operation the total number of cutted segments must be maximum.
#
# Example:
#
# Input
# First line of input contains of an integer 'T' denoting number of test cases. First line of each testcase contains N . Second line of each testcase contains 3 space separated integers x , y and z.
#
# Output
# For each test case print in a new line an integer corresponding to the answer .
#
#
# Constraints
# 1<=t<=70
# 1<=N,x,y,z<=4000
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/cutted-segments/0 (GeeksForGeeks - Maximize The Cut Segments)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
#
# **************************************************************************
# Reference
# **************************************************************************
# https://www.techiedelight.com/rot-cutting/
#
import sys
from typing import List

import unittest


INT_MIN = -sys.maxsize - 1


class Solution(object):
    def max(self, a, b):
        return a if (a > b) else b

    # Problem: Given an integer N denoting the Length of a line segment.
    # You need to cut the line segment in such a way that the cut length of a line segment each time is either
    # x , y or z. Here x, y, and z are integers.
    # After performing all the cut operations, your total number of cut segments must be maximum.

    def maximizeTheCuts(self, prices: List[int], n: int) -> int:
        # base case
        if n <= 0:
            return 0
        dp = [-100000] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(3):
                if prices[j] <= i:
                    dp[i] = max(dp[i], 1 + dp[i - prices[j]])
        if dp[n] == -100000:
            return -1
        return dp[n]

    # Problem: Given a rod of length n inches and an array of prices that contains prices of all pieces of
    # size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

    def rodCut(self, prices: List[int], n: int) -> int:
        # base case
        if n <= 0:
            return 0

        """
        Computes maximum money that can be earned by cutting
        a rod of length len(price) (Bottom-Up Approach).
        Time Complexity : O((len(price))^2)
        Space Complexity : O(len(price))
        :param prices: List in which price[i] denotes price of rod of length i.
        :return: returns optimal solution for rod of length len(price).
        """
        length = len(prices)
        opt_price = [0] * (length + 1)

        for i in range(1, length + 1):
            opt_price[i] = max(
                [-1] + [prices[j] + opt_price[i - j - 1] for j in range(i)]
            )
        return opt_price[length]

    # Solution 1: Naive Recursive Solution
    #
    # TC: O(N^N)
    # SC: O(1)
    #
    # Function to find best way to cut a rod of length n
    # where rod of length i has a cost price[i-1]
    def rodCutNaiveRecursive(self, prices: List[int], n: int) -> int:
        # base case
        if n <= 0:
            return 0

        maxValue = INT_MIN

        # Recursively cut the rod in different pieces
        # and compare different configurations
        for i in range(0, n):
            maxValue = self.max(
                maxValue, prices[i] + self.rodCutNaiveRecursive(prices, n - i - 1)
            )

        return maxValue

    # Solution 2: Iterative Solution based on Dynamic Programming
    #
    # TC: O(N^2)
    # SC: O(N)
    #
    # Function to find best way to cut a rod of length n
    # where rod of length i has a cost price[i-1]
    def rodCutDynamicProgramming(self, prices: List[int], n: int) -> int:
        val = [0 for x in range(n + 1)]
        val[0] = 0
        # Build the table val[] in bottom up manner and return
        # the last entry from the table
        for i in range(1, n + 1):
            maxValue = INT_MIN
            for j in range(i):
                maxValue = max(maxValue, prices[j] + val[i - j - 1])
            val[i] = maxValue

        return val[n]

    def rodCutUnboundedKnapsack(
        self,
        prices: List[int],
        n: int,
        dp: List[List[int]],
        lengths: List[int],
        max_length: int,
    ) -> int:
        if n == 0 or max_length == 0:
            return 0

        # If the length of the rod is less
        # than the maximum length, max_length will
        # consider it.Now depending upon the profit,
        # either max_length  we will take it or discard it.
        if lengths[n - 1] <= max_length:
            dp[n][max_length] = max(
                prices[n - 1]
                + self.rodCutUnboundedKnapsack(
                    prices, n, dp, lengths, max_length - lengths[n - 1]
                ),
                self.rodCutUnboundedKnapsack(prices, n - 1, dp, lengths, max_length),
            )
        # If the length of the rod is
        # greater than the permitted size,
        # max_length we will not consider it.
        else:
            dp[n][max_length] = self.rodCutUnboundedKnapsack(
                prices, n - 1, dp, lengths, max_length
            )

        # return the maximum value obtained
        return dp[n][max_length]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maximizeTheCuts(self) -> None:
        sol = Solution()
        for prices, n, solution in ([[2, 1, 1], 4, 4], [[5, 3, 2], 5, 2]):
            self.assertEqual(solution, sol.maximizeTheCuts(prices, n))

    def test_rodCut(self) -> None:
        sol = Solution()
        for prices, solution in (
            [[2, 1, 1], 6],
            [[5, 3, 2], 15],
            [[1, 5, 8, 9, 10, 17, 17, 20], 22],
        ):
            # self.assertEqual(solution, sol.rodCut(prices, len(prices)))
            self.assertEqual(solution, sol.rodCutNaiveRecursive(prices, len(prices)))
            self.assertEqual(
                solution, sol.rodCutDynamicProgramming(prices, len(prices))
            )
            # list called 'dp' for the purpose of memoization
            n = len(prices)
            dp = [[0] * (n + 1) for i in range(n + 1)]
            self.assertEqual(
                solution,
                sol.rodCutUnboundedKnapsack(
                    prices,
                    len(prices),
                    dp,
                    [i + 1 for i, _ in enumerate(prices)],
                    len(prices),
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
