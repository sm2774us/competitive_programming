#
# Time : O(N); Space: O(1)
# @tag : Recursion ; DFS
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 62: Unique Paths
#
# Description:
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Example 1:
#
# Refer to Example_1.png
#
# Output: 1
#
# Input: m = 3, n = 7
# Output: 28
#
# Example 2:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
# Example 3:
#
# Input: m = 7, n = 3
# Output: 28
#
# Example 4:
#
# Input: m = 3, n = 3
# Output: 6
#
# Constraints:
#
#   * 1 <= m, n <= 100
#   * It's guaranteed that the answer will be less than or equal to 2 * 109.
#
# **************************************************************************
# Source: https://leetcode.com/problems/unique-paths/ (Leetcode - Problem 62 - Unique Paths)
#         https://practice.geeksforgeeks.org/problems/number-of-paths/0 (GeeksForGeeks - Number of paths)
#
#
import math

import unittest


class Solution:
    # math C(m+n-2,n-1)
    def uniquePathsUsingMath(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        return math.factorial(m + n - 2) / (
            math.factorial(n - 1) * math.factorial(m - 1)
        )

    # O(m*n) space
    def uniquePathsUsingDP_with_O_MN_space(self, m, n):
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # O(n) space
    def uniquePathsUsingDP_with_O_N_space(self, m, n):
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_uniquePaths(self) -> None:
        sol = Solution()
        for m, n, solution in ([3, 7, 28], [3, 2, 3], [7, 3, 28], [3, 3, 6]):
            self.assertEqual(
                solution,
                sol.uniquePathsUsingMath(m, n),
                "Should return the number of unique paths on (m X n) grid starting from top-left corner to the bottom-right corner",
            )
            self.assertEqual(
                solution,
                sol.uniquePathsUsingDP_with_O_MN_space(m, n),
                "Should return the number of unique paths on (m X n) grid starting from top-left corner to the bottom-right corner",
            )
            self.assertEqual(
                solution,
                sol.uniquePathsUsingDP_with_O_N_space(m, n),
                "Should return the number of unique paths on (m X n) grid starting from top-left corner to the bottom-right corner",
            )


if __name__ == "__main__":
    unittest.main()
