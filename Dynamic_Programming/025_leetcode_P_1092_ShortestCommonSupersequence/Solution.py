#
# Time  : O(MN) dp
# Space : O(MN) * O(string), but actually we can also save the storage of string.
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1092: Shortest Common Supersequence
#
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.
#
# (A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)
#
#
#
# Example 1:
#
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation:
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
#
#
# Note:
#
#   1. 1 <= str1.length, str2.length <= 1000
#   2. str1 and str2 consist of lowercase English letters.
#
# **************************************************************************
# Source: https://leetcode.com/problems/shortest-common-supersequence/ (LeetCode - Problem 1092 - Shortest Common Supersequence)
#         https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1 (GeeksForGeeks - Shortest Common Supersequence)
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# Refer to: Visual_Explanation.md
#
#
from typing import List
import unittest


class Solution(object):

    # Solution_1: Find the LCS Problem ( Longest Common Subsequence )
    #
    # Change the problem to find the LCS
    #
    # - This is the same code for LCS that you're going to use it in this question
    #   as this demands the shortest common supersequence
    #   (We need this because the DP table has the longest common subsequence stored in table)
    #
    #  - If you think about it, the length of shortest common supersequence would be:
    #    len(str1) + len(str2) - LCS
    #
    #  - So what we are going to do is we would start from the last index of matrix
    #    and if we see that the elements are equal we are going to add them just once
    #    as they are LCS and if the elements are not equal then we add elements
    #    from both of them to find the required string.
    #
    # Don't go for the shortest code out there, also look for code reusability where it is required,
    # think about the concept where it was last used(Like LCS here)
    #
    def shortestCommonSupersequence_solution_1_LCS(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, c in enumerate(str1):
            for j, d in enumerate(str2):
                dp[i + 1][j + 1] = (
                    1 + dp[i][j] if c == d else max(dp[i + 1][j], dp[i][j + 1])
                )
        i, j, stk = m - 1, n - 1, []
        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                stk.append(str1[i])
                i -= 1
                j -= 1
            elif dp[i + 1][j] < dp[i][j + 1]:
                stk.append(str1[i])
                i -= 1
            else:
                stk.append(str2[j])
                j -= 1
        return str1[: i + 1] + str2[: j + 1] + "".join(reversed(stk))
        #
        # def lcs(str1, str2):
        #     n, m = len(str1), len(str2)
        #     dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        #     for i in range(n):
        #         for j in range(m):
        #             if str1[i] == str2[j]:
        #                 dp[i + 1][j + 1] = dp[i][j] + str1[i]
        #             else:
        #                 dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        #     return dp[-1][-1]
        #
        # res, i, j = "", 0, 0
        # for c in lcs(str1, str2):
        #     while str1[i] != c:
        #         res += str1[i]
        #         i += 1
        #     while str2[j] != c:
        #         res += str2[j]
        #         j += 1
        #     res += c
        #     i, j = i + 1, j + 1
        # return res + str1[i:] + str2[j:]

    # def shortestCommonSupersequence_solution_1_LCS(self, str1: str, str2: str) -> str:
    #     # Just make the dp table for finding the LCS and initialize with -1
    #     dp = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    #     dp = self.longestCommonSubsequence(str1, str2, dp)
    #
    #     i = len(str1)
    #     j = len(str2)
    #     res = ''
    #     # Start form the last index and check for string elements
    #     while i > 0 and j > 0:
    #         if str1[i - 1] == str2[j - 1]:
    #             res += str1[i - 1]
    #             i -= 1
    #             j -= 1
    #         elif dp[i][j - 1] > dp[i - 1][j]:
    #             res += str2[j - 1]
    #             j -= 1
    #         else:
    #             res += str1[i - 1]
    #             i -= 1
    #     # We would come out of the above while loop once any of the string becomes 0 but don't forget to add the other string as we are still missing their part.
    #     while i > 0:
    #         res += str1[i - 1]
    #         i -= 1
    #
    #     while j > 0:
    #         res += str2[j - 1]
    #         j -= 1
    #     # Once done with the loop just reverse to keep the order same as we started from the last
    #     return res[::-1]
    #
    # def longestCommonSubsequence(self, text1: str, text2: str, dp: List[List[int]]) -> List[List[int]]:
    #     for i in range(len(text1) + 1):
    #         for j in range(len(text2) + 1):
    #             if i == 0 or j == 0:
    #                 dp[i][j] = 0
    #
    #             elif text1[i - 1] == text2[j - 1]:
    #                 dp[i][j] = 1 + dp[i - 1][j - 1]
    #             else:
    #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Solution_2 : Solving using Dynamic Programming (without LCS)
    #
    # We can also directly get the answer without LCS, where dp stores Shortest Common Supersequence instead of LCS.
    # The first dimension of dp has been set to 2 to prevent from MLE.
    #
    def shortestCommonSupersequence_solution_2_Using_DP_without_LCS(
        self, str1: str, str2: str
    ) -> str:
        dp = [["" for _ in range(len(str1) + 1)] for _ in range(2)]
        for j in range(1, len(str1) + 1):
            dp[0][j] = str1[:j]
        cur = 1
        p = 0
        for i in range(1, len(str2) + 1):
            p = 1 - p
            dp[p][0] = str2[:cur]
            cur += 1
            for j in range(1, len(str1) + 1):
                if str2[i - 1] == str1[j - 1]:
                    dp[p][j] = dp[1 - p][j - 1] + str1[j - 1]
                else:
                    if len(dp[1 - p][j]) <= len(dp[p][j - 1]):
                        dp[p][j] = dp[1 - p][j] + str2[i - 1]
                    else:
                        dp[p][j] = dp[p][j - 1] + str1[j - 1]
        return dp[p][-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_shortestCommonSupersequence(self) -> None:
        sol = Solution()
        for str1, str2, solution in (
            ["abcd", "xycd", "abxycd"],
            ["efgh", "jghi", "efjghi"],
            ["abac", "cab", "cabac"],
        ):
            self.assertEqual(
                solution, sol.shortestCommonSupersequence_solution_1_LCS(str1, str2)
            )
            self.assertEqual(
                solution,
                sol.shortestCommonSupersequence_solution_2_Using_DP_without_LCS(
                    str1, str2
                ),
            )

    def test_shortestCommonSupersequenceLength_GeeksForGeeks_Variation(self) -> None:
        sol = Solution()
        for str1, str2, solution in (
            ["abcd", "xycd", 6],
            ["efgh", "jghi", 6],
            ["abac", "cab", 5],
        ):
            self.assertEqual(
                solution,
                len(sol.shortestCommonSupersequence_solution_1_LCS(str1, str2)),
            )
            self.assertEqual(
                solution,
                len(
                    sol.shortestCommonSupersequence_solution_2_Using_DP_without_LCS(
                        str1, str2
                    )
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
