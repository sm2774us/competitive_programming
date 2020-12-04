#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Rightmost different bit
#
# Description:
#
# Given two numbers M and N. The task is to find the position of the rightmost different bit in the binary representation of numbers.
#
# Example 1:
#
# Input: M = 11, N = 9
# Output: 2
# Explanation: Binary representation of the given
# numbers are: 1011 and 1001,
# 2nd bit from right is different.
# Example 2:
#
# Input: M = 52, N = 4
# Output: 5
# Explanation: Binary representation of the given
# numbers are: 110100â€¬ and 0100,
# 5th-bit from right is different.
# User Task:
# The task is to complete the function posOfRightMostDiffBit() which takes two arguments m and n and returns the position of first different bits in m and n. If both m and n are the same then return -1 in this case.
#
# Expected Time Complexity: O(max(log m, log n)).
# Expected Auxiliary Space: O(1).
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1 (GeeksForGeeks - Rightmost different bit )
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# Reference:
# **************************************************************************
# https://qelifeblog.wordpress.com/2017/06/24/codefights-different-rightmost-bit/
#
from math import log2

import unittest


class Solution(object):

    # Function to find the position of
    # rightmost set bit in 'n'
    def getRightMostSetBit(self, n: int) -> int:
        if n == 0:
            return 0

        return int(log2(n & -n)) + 1

    # Function to find the position of
    # rightmost different bit in the
    # binary representations of 'm' and 'n'
    def posOfRightMostDiffBit(self, m: int, n: int) -> int:
        # position of rightmost different
        # bit
        return self.getRightMostSetBit(m ^ n)

    # Function to find the position of
    # rightmost different bit in the
    # binary representations of 'm' and 'n'
    # and return its value
    def valOfRightMostDiffBit(self, m: int, n: int) -> int:
        return (m ^ n) & -(m ^ n)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_posOfRightMostDiffBit(self) -> None:
        sol = Solution()
        for m, n, solution in ([11, 9, 2], [52, 4, 5]):
            self.assertEqual(solution, sol.posOfRightMostDiffBit(m, n))

    def test_valOfRightMostDiffBit(self) -> None:
        sol = Solution()
        for m, n, solution in ([13, 11, 2], [23, 7, 16]):
            self.assertEqual(solution, sol.valOfRightMostDiffBit(m, n))


# main
if __name__ == "__main__":
    unittest.main()
