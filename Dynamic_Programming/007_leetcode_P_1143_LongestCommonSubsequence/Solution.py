#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1143: Longest Common Subsequence
#
# Description:
#
# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
# without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
# while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
# Constraints:
#   * 1 <= text1.length <= 1000
#   * 1 <= text2.length <= 1000
#   * The input strings consist of lowercase English characters only.
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-common-subsequence/ (LeetCode - Problem 1143 - Longest Common Subsequence)
#         https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0 (GeeksForGeeks - Longest Common Subsequence)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# References:
# https://leetcode.com/problems/longest-common-subsequence/discuss/436719/Python-very-detailed-solution-with-explanation-and-walkthrough-step-by-step.
# https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
# https://leetcode.com/problems/longest-common-subsequence/discuss/598508/Python-DP-solution-with-Explanation-%2B-Thinking-process-%2B-Diagram
#
from functools import lru_cache

import unittest


class Solution(object):
    # Recursive solution
    # Time Complexity: O(2^n)
    def longestCommonSubsequenceUsingRecursion(self, text1: str, text2: str) -> int:
        def helper(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + helper(s1, s2, i + 1, j + 1)
            else:
                return max(helper(s1, s2, i + 1, j), helper(s1, s2, i, j + 1))

        return helper(text1, text2, 0, 0)

    # Recursive solution with Memoization
    # Time Complexity: O(m*n)
    def longestCommonSubsequenceUsingRecursionAndMemoization(
        self, text1: str, text2: str
    ) -> int:
        def helper(s1, s2, i, j, memo):
            if memo[i][j] < 0:
                if i == len(s1) or j == len(s2):
                    memo[i][j] = 0
                elif s1[i] == s2[j]:
                    memo[i][j] = 1 + helper(s1, s2, i + 1, j + 1, memo)
                else:
                    memo[i][j] = max(
                        helper(s1, s2, i + 1, j, memo), helper(s1, s2, i, j + 1, memo)
                    )
            return memo[i][j]

        m = len(text1)
        n = len(text2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return helper(text1, text2, 0, 0, memo)

    # Bottom up dynamic programming
    # Time Complexity: O(m*n)
    # Space Complexity: O(m*n)
    def longestCommonSubsequenceUsingDynamicProgrammingBottomUp(
        self, text1: str, text2: str
    ) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]

    # Dynamic Programming With Reduced Space Complexity
    # Time Complexity: O(m*n)
    # Space Complexity: O(MIN(m,n)
    def longestCommonSubsequenceUsingDynamicProgrammingWithReducedSpaceComplexity(
        self, text1: str, text2: str
    ) -> int:
        m = len(text1)
        n = len(text2)
        if m < n:
            return self.longestCommonSubsequenceUsingDynamicProgrammingWithReducedSpaceComplexity(
                text2, text1
            )
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
                else:
                    memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])

        return memo[m % 2][n]

    # Dynamic Programming With Reduced Space Complexity
    # Time Complexity: O(m*n)
    # Space Complexity: O(MIN(m,n)
    def longestCommonSubsequenceUsingDynamicProgrammingWithRecursionAndMemoization(
        self, text1: str, text2: str
    ) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0

            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1 + 1, ptr2 + 1)

            # Case 2
            else:
                return max(memo_solve(ptr1 + 1, ptr2), memo_solve(ptr1, ptr2 + 1))
                # ^    # ^ Case 2 - Option 1           ^ Case 2 - Option 2
                # | __You want the max() result from resulting branches in the tree

        return memo_solve(0, 0)  # Start the recursion stack from str1[0] and str2[0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestCommonSubsequence(self) -> None:
        sol = Solution()
        for text1, text2, solution in (
            ["abcde", "ace", 3],
            ["abc", "abc", 3],
            ["abc", "def", 0],
            ["ABCDGH", "AEDFHR", 3],
            ["ABC", "AC", 2],
        ):
            self.assertEqual(
                solution, sol.longestCommonSubsequenceUsingRecursion(text1, text2)
            )
            self.assertEqual(
                solution,
                sol.longestCommonSubsequenceUsingRecursionAndMemoization(text1, text2),
            )
            self.assertEqual(
                solution,
                sol.longestCommonSubsequenceUsingDynamicProgrammingBottomUp(
                    text1, text2
                ),
            )
            self.assertEqual(
                solution,
                sol.longestCommonSubsequenceUsingDynamicProgrammingWithReducedSpaceComplexity(
                    text1, text2
                ),
            )
            self.assertEqual(
                solution,
                sol.longestCommonSubsequenceUsingDynamicProgrammingWithRecursionAndMemoization(
                    text1, text2
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
