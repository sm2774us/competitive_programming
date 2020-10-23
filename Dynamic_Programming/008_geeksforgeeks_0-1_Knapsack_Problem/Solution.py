#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : 0 - 1 Knapsack Problem
#
# Description:
#
# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum
# total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights
# associated with N items respectively. Also given an integer W which represents knapsack capacity,
# find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than
# or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines.
# The first line consists of N the number of items.
# The second line consists of W, the maximum capacity of the knapsack.
# In the next line are N space separated positive integers denoting the values of the N items,
# and in the fourth line are N space separated positive integers denoting the weights of the corresponding items.
#
# Output:
# For each testcase, in a new line, print the maximum possible value you can get with the given conditions that you can obtain for each test case in a new line.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 1000
# 1 ≤ W ≤ 1000
# 1 ≤ wt[i] ≤ 1000
# 1 ≤ v[i] ≤ 1000
#
# Example:
# Input:
# 2
# 3
# 4
# 1 2 3
# 4 5 1
# 3
# 3
# 1 2 3
# 4 5 6
# Output:
# 3
# 0
# Explanation:
# Test Case 1: With W = 4, you can either choose the 0th item or the 2nd item. Thus, the maximum value you can generate is the max of val[0] and val[2], which is equal to 3.
# Test Case 2: With W = 3, there is no item you can choose from the given list as all the items have weight greater than W. Thus, the maximum value you can generate is 0.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# Reference
# **************************************************************************
# Edicative
# LeetCode: https://leetcode.com/problems/ones-and-zeroes/discuss/95808/0-1-knapsack-in-python
# GeeksForGeeks: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# Github: https://github.com/kaushikthedeveloper/GeeksforGeeks-python/blob/master/Scripts/0-1%20Knapsack%20Problem%20(%20DP%20).py
#
from typing import List

import unittest


class Solution(object):

    # TC: O(2^n) [ Exponential ], where ‘n’ represents the total number of items
    #     This can also be confirmed from the above recursion tree.
    #     As we can see that we will have a total of ‘31’ recursive calls –
    #     calculated through (2^n) + (2^n) - 1, which is asymptotically equivalent to O(2^n).
    #
    # SC: O(n)
    #     This space will be used to store the recursion stack.
    #     Since our recursive algorithm works in a depth-first fashion,
    #     which means, we can’t have more than ‘n’ recursive calls on the call stack at any time.
    def knapsackBruteForce(
        self, profits: List[int], weights: List[int], capacity: int
    ) -> int:
        def knapsack_recursive(
            profits: List[int], weights: List[int], capacity: int, currentIndex: int
        ) -> int:
            # base checks
            if capacity <= 0 or currentIndex >= len(profits):
                return 0

            # recursive call after choosing the element at the currentIndex
            # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
            profit1 = 0
            if weights[currentIndex] <= capacity:
                profit1 = profits[currentIndex] + knapsack_recursive(
                    profits, weights, capacity - weights[currentIndex], currentIndex + 1
                )

            # recursive call after excluding the element at the currentIndex
            profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)

            return max(profit1, profit2)

        return knapsack_recursive(profits, weights, capacity, 0)

    # If len(text2) > len(text1) then we can optimize further.
    # TC: O(min(M, N))
    # SC: O(N) => 1D array v/s 2D array in previous solution
    def knapsackTopDownDynamicProgrammingWithMemoization(
        self, profits: List[int], weights: List[int], capacity: int
    ) -> int:
        def knapsack_recursive(dp, profits, weights, capacity, currentIndex):

            # base checks
            if capacity <= 0 or currentIndex >= len(profits):
                return 0

            # if we have already solved a similar problem, return the result from memory
            if dp[currentIndex][capacity] != -1:
                return dp[currentIndex][capacity]

            # recursive call after choosing the element at the currentIndex
            # if the weight of the element at currentIndex exceeds the capacity, we
            # shouldn't process this
            profit1 = 0
            if weights[currentIndex] <= capacity:
                profit1 = profits[currentIndex] + knapsack_recursive(
                    dp,
                    profits,
                    weights,
                    capacity - weights[currentIndex],
                    currentIndex + 1,
                )

            # recursive call after excluding the element at the currentIndex
            profit2 = knapsack_recursive(
                dp, profits, weights, capacity, currentIndex + 1
            )

            dp[currentIndex][capacity] = max(profit1, profit2)
            return dp[currentIndex][capacity]

        # create a two dimensional array for Memoization, each element is initialized to '-1'
        dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
        return knapsack_recursive(dp, profits, weights, capacity, 0)

    def knapsackBottomUpDynamicProgramming(
        self, profits: List[int], weights: List[int], capacity: int
    ) -> int:
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity + 1)] for y in range(n)]

        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i - 1][c - weights[i]]
                # exclude the item
                profit2 = dp[i - 1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)

        # maximum profit will be at the bottom-right corner.
        return dp[n - 1][capacity]

    def knapsackBottomUpDynamicProgrammingWithReducedSpaceComplexity(
        self, profits: List[int], weights: List[int], capacity: int
    ) -> int:
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        # we only need one previous row to find the optimal solution, overall we need '2' rows
        # the above solution is similar to the previous solution, the only difference is that
        # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
        dp = [[0 for x in range(capacity + 1)] for y in range(2)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[0][c] = dp[1][c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(0, capacity + 1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
                # exclude the item
                profit2 = dp[(i - 1) % 2][c]
                # take maximum
                dp[i % 2][c] = max(profit1, profit2)

        return dp[(n - 1) % 2][capacity]

    def knapsackBottomUpDynamicProgrammingWithReducedSpaceComplexityPartTwo(
        self, profits: List[int], weights: List[int], capacity: int
    ) -> int:
        # basic checks
        n = len(profits)
        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [0 for x in range(capacity + 1)]

        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity + 1):
            if weights[0] <= c:
                dp[c] = profits[0]

        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(capacity, -1, -1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[c - weights[i]]
                # exclude the item
                profit2 = dp[c]
                # take maximum
                dp[c] = max(profit1, profit2)

        return dp[capacity]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_knapsack(self) -> None:
        sol = Solution()
        for profits, weights, capacity, solution in (
            [[1, 2, 3], [4, 5, 1], 4, 3],
            [[1, 2, 3], [4, 5, 6], 3, 0],
        ):
            self.assertEqual(
                solution, sol.knapsackBruteForce(profits, weights, capacity)
            )
            self.assertEqual(
                solution,
                sol.knapsackTopDownDynamicProgrammingWithMemoization(
                    profits, weights, capacity
                ),
            )
            self.assertEqual(
                solution,
                sol.knapsackBottomUpDynamicProgramming(profits, weights, capacity),
            )
            self.assertEqual(
                solution,
                sol.knapsackBottomUpDynamicProgrammingWithReducedSpaceComplexity(
                    profits, weights, capacity
                ),
            )
            self.assertEqual(
                solution,
                sol.knapsackBottomUpDynamicProgrammingWithReducedSpaceComplexityPartTwo(
                    profits, weights, capacity
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
