#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 887: Super Egg Drop
#
# Description:
#
# You are given K eggs, and you have access to a building with N floors from 1 to N.
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor
# higher than F will break, and any egg dropped at or below floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X
# (with 1 <= X <= N).
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what F is,
# regardless of the initial value of F ?
#
#
# Example 1:
#
# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
#
# Example 2:
#
# Input: K = 2, N = 6
# Output: 3
# Example 3:
#
# Input: K = 3, N = 14
# Output: 4
#
# Note:
#   * 1 <= K <= 100
#   * 1 <= N <= 10000
#
# **************************************************************************
# Source: https://leetcode.com/problems/super-egg-drop/ (LeetCode - Problem 887 - Super Egg Drop)
#         https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1 (GeeksForGeeks - Egg Dropping Puzzle)
# **************************************************************************
#
# References:
# **************************************************************************
# https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
#
import math

# import sys
import unittest

# x=1500
# sys.setrecursionlimit(x)


class Solution(object):

    # Solution_1 : Brute Force Solution
    # Time Complexity: O(kn^2)
    def superEggDrop_solution_1_brute_force(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[math.inf] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]

    # Solution_2 : Optimization1: choosing k for each dp[i][j]
    # Time Complexity: O(knlogn)
    def superEggDrop_solution_2_optimization_one(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        def dfs(i, j):
            if i == 1:
                return j
            if j == 0:
                return 0
            if j == 1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            res = math.inf
            while lo < hi:
                mid = (lo + hi) / 2
                left, right = dfs(i - 1, mid - 1), dfs(i, j - mid)
                res = min(res, 1 + max(left, right))
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            return res
            # while lo < hi:
            #     mid = (lo + hi) / 2
            #     left, right = dfs(i - 1, mid - 1), dfs(i, j - mid)
            #     if left < right:
            #         lo = mid + 1
            #     else:
            #         hi = mid
            # res = 1 + max(dfs(i - 1, lo - 1), dfs(i, j - lo))
            # d[i, j] = res
            # return res

        d = {}
        return dfs(K, N)

    # Solution_3 : Optimization2: choosing k_1...k_N for each dp[i][1...N]
    # Time Complexity: O(kn)
    def superEggDrop_solution_3_optimization_two(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # dp = [[math.inf] * (N + 1) for _ in range(K + 1)]
        # for i in range(1, K + 1):
        #     dp[i][0] = 0
        #     dp[i][1] = 1
        # for j in range(1, N + 1):
        #     dp[1][j] = j
        #
        # for i in range(2, K + 1):
        #     k = 1
        #     for j in range(2, N + 1):
        #         while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
        #             k += 1
        #         dp[i][j] = 1 + dp[i - 1][k - 1]
        # return dp[K][N]
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        # print(dp)

        # For 0 egg we need no trial and for 1 egg we need to check i floors
        for i in range(N + 1):
            dp[0][i] = 0
            dp[1][i] = i

        # If we only have one floor then we only check once for any No. of eggs
        for j in range(K + 1):
            dp[j][1] = 1

        # Apply Looping on rest cases
        for i in range(2, K + 1):
            x = 1
            for j in range(2, N + 1):
                while x < j + 1:
                    if dp[i][x - 1] >= dp[i - 1][j - x]:
                        dp[i][j] = 1 + dp[i][x - 1]
                        break
                    x += 1
        return dp[-1][-1]

    # Solution_4 : Op
    # timization3: space complexity
    # Time Complexity : O(kn)
    # Space Complexity: O(n)
    def superEggDrop_solution_4_optimization_three(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = range(N + 1)
        for i in range(2, K + 1):
            k = 1
            ndp = [0, 1] + [math.inf] * (N - 1)
            for j in range(2, N + 1):
                while k < j + 1 and ndp[j - k] > dp[k - 1]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp = ndp
        return dp[N]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_superEggDrop(self) -> None:
        sol = Solution()
        for K, N, solution in ([1, 2, 2], [2, 6, 3], [3, 14, 4], [2, 10, 4], [3, 5, 3]):
            self.assertEqual(solution, sol.superEggDrop_solution_1_brute_force(K, N))
            # Solution_2 : Recursive Solution [ Optimization1: choosing k for each dp[i][j] }
            #              Throws a => "RecursionError: maximum recursion depth exceeded in comparison"
            # self.assertEqual(solution, sol.superEggDrop_solution_2_optimization_one(K, N))
            self.assertEqual(
                solution, sol.superEggDrop_solution_3_optimization_two(K, N)
            )
            self.assertEqual(
                solution, sol.superEggDrop_solution_4_optimization_three(K, N)
            )


# main
if __name__ == "__main__":
    unittest.main()
