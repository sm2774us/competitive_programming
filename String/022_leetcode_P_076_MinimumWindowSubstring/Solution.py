#
# Time :
# Space:
#
# @tag : String
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
from typing import List
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
        st, c1, min_so_far, result, fmap = (
            0,
            Counter(t),
            len(s) + 1,
            "",
            defaultdict(int),
        )
        unique_ch = len(c1)
        for end in range(len(s)):
            if s[end] in c1:
                fmap[s[end]] += 1
                if fmap[s[end]] == c1[s[end]]:
                    unique_ch -= 1
                while st <= end and unique_ch == 0:
                    if end - st + 1 < min_so_far:
                        min_so_far, result = end - st + 1, s[st : end + 1]
                    if s[st] in fmap:
                        fmap[s[st]] -= 1
                        if fmap[s[st]] < c1[s[st]]:
                            unique_ch += 1
                    st += 1
        return result

    def minWindow_facebook_and_google_phone_screen(self, s: str, t: List[str]) -> str:
        """
        :type s: str
        :type t: List[str]
        :rtype: str
        """
        st, c1, min_so_far, result, fmap = (
            0,
            Counter(t),
            len(s) + 1,
            "",
            defaultdict(int),
        )
        unique_ch = len(c1)
        for end in range(len(s)):
            if s[end] in c1:
                fmap[s[end]] += 1
                if fmap[s[end]] == c1[s[end]]:
                    unique_ch -= 1
                while st <= end and unique_ch == 0:
                    if end - st + 1 < min_so_far:
                        min_so_far, result = end - st + 1, s[st : end + 1]
                    if s[st] in fmap:
                        fmap[s[st]] -= 1
                        if fmap[s[st]] < c1[s[st]]:
                            unique_ch += 1
                    st += 1
        return result

    # #
    # # The algorithm has two major phases.
    # #
    # # 1. Find the first window that contains all letters in t;
    # # 2. Keep expanding the window to the right by 1 char at a time, reducing left side if possible.
    # #    The best part is to make sure that THE ACTIVE WINDOW ALWAYS CONTAINS ALL LETTERS IN t.
    # #    In this case, every time the window is expanded, only the new char need to be checked.
    # #
    # #
    # def minWindow_concise(self, s: str, t: str) -> str:
    #     need, missing = Counter(t), len(t)
    #     i = I = J = 0
    #     for j, c in enumerate(s, 1):
    #         missing -= need[c] > 0
    #         need[c] -= 1
    #         if not missing:
    #             while need[s[i]] < 0: need[s[i]] += 1; i += 1
    #             if not J or j - i <= J - I: I, J = i, j
    #             need[s[i]] += 1;
    #             i += 1;
    #             missing += 1  # SPEEEEEEEED UP!
    #     return s[I : J]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minWindow(self) -> None:
        sol = Solution()

        for s, t, solution in (
            ["timetopractice", "toc", "toprac"],
            ["zoomlazapzo", "oza", "apzo"],
            ["ADOBECODEBANC", "ABC", "BANC"],
        ):
            self.assertEqual(
                solution,
                sol.minWindow(s, t),
                "Should return the minimum window in S which will contain all the characters in T",
            )
            # self.assertEqual(
            #     solution,
            #     sol.minWindow_concise(s, t),
            #     "Should return the minimum window in S which will contain all the characters in T",
            # )

    # Facebook | Phone Screen | Minimum Window Substring
    #
    # Given a string as a "source" string, find the smallest substring of source such that it contains
    # all characters in "search" string (which contains distinct characters).
    #
    # For example, for search string ['a','b','c'], source string "aefbcgaxy", the shortest string is "bcga".
    def test_minWindow_facebook_phone_screen(self) -> None:
        sol = Solution()
        s = "aefbcgaxy"
        t = ["a", "b", "c"]
        self.assertEqual(
            "bcga",
            sol.minWindow_facebook_and_google_phone_screen(s, t),
            "Should return the minimum window in S which will contain all the characters in T",
        )

    # Google | Phone | Minimum Window Substring
    #
    # I had one problem.
    #
    # Variation of https://leetcode.com/problems/minimum-window-substring/
    #
    # Given a string return the minimal substring that contain all the letters of the alphabet.
    #
    # def find(string, alphabet)
    # For eg. string = aabcad alphabet = ['a','b','c', 'd'] Output: "bcad"
    def test_minWindow_google_phone_screen(self) -> None:
        sol = Solution()
        s = "aabcad"
        t = ["a", "b", "c", "d"]
        self.assertEqual(
            "bcad",
            sol.minWindow_facebook_and_google_phone_screen(s, t),
            "Should return the minimum window in S which will contain all the characters in T",
        )


if __name__ == "__main__":
    unittest.main()
