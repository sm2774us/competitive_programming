#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Longest Common Substring
#
# Description:
#
# Given two strings X and Y. The task is to find the length of the longest common substring.
#
# Input:
# First line of the input contains number of test cases T. Each test case consist of three lines, first of which contains 2 space separated integers N and M denoting the size of string X and Y strings respectively. The next two lines contains the string X and Y.
#
# Output:
# For each test case print the length of longest  common substring of the two strings .
#
# Constraints:
# 1 <= T <= 200
# 1 <= N, M <= 100
#
# Example:
# Input:
# 2
# 6 6
# ABCDGH
# ACDGHR
# 3 2
# ABC
# AC
#
# Output:
# 4
# 1
#
# Example:
# Testcase 1: CDGH is the longest substring present in both of the strings.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/longest-common-substring/0 (GeeksForGeeks - Longest Common Substring)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):
    # TC: O(MN)
    # SC: O(MN)
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        res = 0
        R, C = len(text1), len(text2)
        dp = [[0] * (C + 1) for i in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res

    # If len(text2) > len(text1) then we can optimize further.
    # TC: O(min(M, N))
    # SC: O(N) => 1D array v/s 2D array in previous solution
    def longestCommonSubstringImproved(self, text1: str, text2: str) -> int:
        res = 0
        R, C = len(text1), len(text2)
        dp = [0] * (C + 1)
        for i in range(1, R + 1):
            for j in range(C, 0, -1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                res = max(res, dp[j])
            # print dp
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestCommonSubstring(self) -> None:
        sol = Solution()
        for text1, text2, solution in (["ABCDGH", "ACDGHR", 4], ["ABC", "AC", 1]):
            self.assertEqual(solution, sol.longestCommonSubstring(text1, text2))
            self.assertEqual(solution, sol.longestCommonSubstringImproved(text1, text2))


# main
if __name__ == "__main__":
    unittest.main()
