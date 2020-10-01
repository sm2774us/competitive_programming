#
# Time : O(N); Space: O(1)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 76: Minimum Window Substring
#
# Description:
#
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#
# **************************************************************************
# Source: https://leetcode.com/problems/minimum-window-substring/ (Leetcode - Problem 76 - Minimum Window Substring)
#         https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string/0 (GeeksForGeeks - Smallest window in a string containing all the characters of another string)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# This is a Two-Pointer problem:
# **************************************************************************
#
# General Pattern to solve 2 pointer problems
#
# start, end = 0, len(input)
# // data-structures for your problem
# for end in range(len(input)):
#     if input[end] contributes to extending the solution:
#         update the impact of including input[end]
#         while st <= end and input[st:end+1] is a valid solution:
#             update for optimal solution
#             update for the impact of removing input[start]
#             start += 1
#
#
from collections import Counter
from collections import defaultdict

import unittest

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        st, c1, min_so_far, result, fmap = 0, Counter(t), len(s) + 1, "", defaultdict(int)
        unique_ch = len(c1)
        for end in range(len(s)):
            if s[end] in c1:
                fmap[s[end]] += 1
                if fmap[s[end]] == c1[s[end]]:
                    unique_ch -= 1
                while st <= end and unique_ch == 0:
                    if end - st + 1 < min_so_far:
                        min_so_far, result = end - st + 1, s[st:end + 1]
                    if s[st] in fmap:
                        fmap[s[st]] -= 1
                        if fmap[s[st]] < c1[s[st]]:
                            unique_ch += 1
                    st += 1
        return result

    
class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTheDifference(self) -> None:
        sol = Solution()

        def test_findTheDifference(self) -> None:
            sol = Solution()
            for s, t, solution in (
                    ["timetopractice", "toc", "toprac"],
                    ["zoomlazapzo", "oza", "apzo"],
                    ["ADOBECODEBANC", "ABC", "BANC"]
            ):
                self.assertEqual(
                    solution,
                    sol.minWindow(s, t),
                    "Should return the minimum window in S which will contain all the characters in T"
                )


if __name__ == "__main__":
    unittest.main()
