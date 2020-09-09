# Time : O(N); Space: O(N), using Knuth-Morris-Pratt Algorithm (KMP)
# @tag : String, Knuth-Morris-Pratt Algorithm (KMP)
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 786: Rotate String
#
# Description:
#
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only
# if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:
#
# A and B will have length at most 100.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/rotate-string/ (Leetcode - Problem 796 - Rotate String)
# Variant   : https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0 (GeeksForGeeks - Check if string is rotated by two places)
#
# Solution Explanation
# **************************************************************************
# 1) LeetCode - Problem - 786: Rotate String ( KMP - T: O(N) ; S: O(N) )
# **************************************************************************
# In computer science, the Knuth–Morris–Pratt string-searching algorithm (or KMP algorithm) searches for occurrences
# of a "word" W within a main "text string" S by employing the observation that when a mismatch occurs,
# the word itself embodies sufficient information to determine where the next match could begin,
# thus bypassing re-examination of previously matched characters.
#
# References:
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
#
# CLRS, ch 32
# https://web.stanford.edu/class/cs97si/10-string-algorithms.pdf
#
# **************************************************************************
# 2) GeeksForGeeks - Check if string is rotated by two places
# **************************************************************************
# 1- There can be only two cases:
#     a) Clockwise rotated
#     b) Anti-clockwise rotated
#
# 2- If clockwise rotated that means elements
#    are shifted in right.
#    So, check if a substring[2.... len-1] of
#    string2 when concatenated with substring[0,1]
#    of string2 is equal to string1. Then, return true.
#
# 3- Else, check if it is rotated anti-clockwise
#    that means elements are shifted to left.
#    So, check if concatenation of substring[len-2, len-1]
#    with substring[0....len-3] makes it equals to
#    string1. Then return true.
#
# 4- Else, return false.
from functools import reduce

import unittest


class Solution:
    # Probing
    # O(T): O(n ^ 2)
    # O(S): O(n)
    def rotateStringOneLiner(self, A: str, B: str) -> bool:
        return A == B or any(A[i:] + A[:i] == B for i, v in enumerate(A) if v == B[0])

    """
    KMP algorithm
    time: O(N)
    space: O(N)
    """

    def rotateStringUsingKnuthMorrisPrattAlgorithm(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B

        # calculate pi table, it captures the length of the
        # longest prefix that is also the suffix
        pi = [0] * (N + 1)
        left, pi[0] = -1, -1
        for right in range(1, N + 1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left

        # do matching
        j = 0
        for i in range(1, (2 * N) + 1):
            while j >= 0 and B[j + 1] != A[i]:
                j = pi[j]
            j += 1
            if j == N:
                return True

        return False

    def checkIfStringsIsRotatedByTwoPlacesGeeksForGeeks(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        clock_rot = ""
        anticlock_rot = ""
        l = len(B)

        # Initialize string as anti-clockwise rotation
        anticlock_rot = anticlock_rot + B[l - 2 :] + B[0 : l - 2]

        # Initialize string as clock wise rotation
        clock_rot = clock_rot + B[2:] + B[0:2]

        # check if any of them is equal to string1
        return A == clock_rot or A == anticlock_rot


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_rotateStringLeetCode(self) -> None:
        s = Solution()
        for A, B, solution in (["abcde", "cdeab", True], ["abcde", "abced", False]):
            self.assertEqual(
                solution,
                s.rotateStringOneLiner(A, B),
                "Should return whether A can become B after some number of shifts on A",
            )
            self.assertEqual(
                solution,
                s.rotateStringUsingKnuthMorrisPrattAlgorithm(A, B),
                "Should return whether A can become B after some number of shifts on A",
            )

    def test_checkIfStringsIsRotatedByTwoPlacesGeeksForGeeks(self) -> None:
        s = Solution()
        for A, B, solution in (
            ["amazon", "azonam", True],
            ["geeksforgeeks", "geeksgeeksfor", False],
        ):
            self.assertEqual(
                solution,
                s.checkIfStringsIsRotatedByTwoPlacesGeeksForGeeks(A, B),
                "Should return whether A can become B after exactly two shifts on A",
            )


if __name__ == "__main__":
    unittest.main()
