# Time : O(N^2); Space: O(N^2)
# @tag : String, Longest Common Sequence
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 1312: Minimum Insertion Steps to Make a String Palindrome
#
# Given a string s. In one step you can insert any character at any index of the string.
#
# Return the minimum number of steps to make s palindrome.
#
# A Palindrome String is one that reads the same backward as well as forward.
#
# **************************************************************************
# Palindrome Definition (https://en.wikipedia.org/wiki/Palindrome) :
# ***********************
# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
# such as madam, racecar.
#
# ***********************
#
# Example 1:
#
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we don't need any insertions.
# Example 2:
#
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:
#
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# Example 4:
#
# Input: s = "g"
# Output: 0
# Example 5:
#
# Input: s = "no"
# Output: 1
#
#
# Constraints:
#
# 1 <= s.length <= 500
# All characters of s are lower case English letters.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/ (Leetcode - Problem - 1312 - Minimum Insertion Steps to Make a String Palindrome)
#             https://practice.geeksforgeeks.org/problems/form-a-palindrome/0 (GeeksForGeeks - Form a palindrome)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# Intuition
# **************************************************************************
# Split the string s into to two parts,
# and we try to make them symmetrical by adding letters.
#
# The more common symmetrical subsequence they have,
# the less letters we need to add.
#
# Now we change the problem to find the length of longest common sequence.
# This is a typical dynamic problem.
#
#
# Explanation
# **************************************************************************
# 1) Step1.
# Initialize dp[n+1][n+1],
# wheredp[i][j] means the length of longest common sequence between
# i first letters in s1 and j first letters in s2.
#
# 2) Step2.
# Find the the longest common sequence between s1 and s2,
# where s1 = s and s2 = reversed(s)
#
# 3) Step3.
# return n - dp[n][n]
#
#
# Complexity
# **************************************************************************
# Time O(N^2)
# Space O(N^2)
#
#
from typing import List
import collections

import unittest


class Solution:
    # ~j = -j - 1
    #
    # Brief explanation for s[~j].
    # ~j = -j - 1
    # so while i ranges from 0 to n-1,
    # ~i ranges from -1 to -n.
    # This is nice because we can now traverse the list backward.
    # no need to write for i in range(len(n-1), 0, -1).
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[i + 1][j + 1] = (
                    dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
                )
        return n - dp[n][n]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minInsertions(self) -> None:
        sol = Solution()
        for s, solution in (
            ["zzazz", 0],
            ["mbadm", 2],
            ["leetcode", 5],
            ["g", 0],
            ["no", 1],
            ["abcd", 3],
            ["aba", 0],
            ["geeks", 3],
        ):

            self.assertEqual(
                solution,
                sol.minInsertions(s),
                "Should return the minimum number of insertions required to make string s a Palindrome",
            )


if __name__ == "__main__":
    unittest.main()
