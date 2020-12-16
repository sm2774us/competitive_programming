#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 600: Non-negative Integers without Consecutive Ones
#
# Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.
#
# Example 1:
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
#
# Note: 1 <= n <= 109
#
# **************************************************************************
# Source: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/ (Leetcode - Problem 600 - Non-negative Integers without Consecutive Ones)
#         https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1 (GeeksForGeeks - Consecutive 1's not allowed)
#
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# LeetCode - Problem 600 - Non-negative Integers without Consecutive Ones :
# **************************************************************************
# Refer to Solution_Explanation.md
#
# GeeksForGeeks - Consecutive 1's not allowed
# **************************************************************************
# Refer to GFG_Solution_Explanation.md
#
from typing import List

import unittest


class Solution(object):

    # Solution 1: Fibonacci numbers based solution
    #
    # x, y are used to calculate Fibonacci numbers.
    # num & 1 and num & 2 will check if num ends with 11 in binary.
    #
    # Why can I use fibonacci numbers?
    # a(n) = the number of valid integers less than 2^n
    # a(5) = the number of valid integers less than 0b100000
    # It equals to the number of valid integers in [0b0, 0b10000[ and in [0b10000, 0b11000[.
    # The number of valid integers [0b0, 0b10000[, which is like '0b0XXXX', equals to a(4).
    # The number of valid integers [0b10000, 0b11000[, which is like '0b101XX', equals to a(3).
    # So a(5) = a(4) + a(3).
    # This rule is the same for other values of n, and it is the same as Fibonacci numbers
    # recurrence relation definition.
    #
    # ----------------------------------------------------------------------------------------
    # The solution is based on 2 facts:
    # ----------------------------------------------------------------------------------------
    #
    # 1) The number of length k string without consecutive 1 is Fibonacci sequence f(k);
    #    For example, if k = 5, the range is 00000-11111. We can consider it as two ranges,
    #    which are 00000-01111 and 10000-10111. Any number >= 11000 is not allowed due to consecutive 1.
    #    The first case is actually f(4), and the second case is f(3), so f(5)= f(4)+f(3).
    #
    # 2) Scan the number from most significant digit, i.e. left to right, in binary format.
    #    If we find a '1' with k digits to the right, count increases by f(k) because
    #    we can put a '0' at this digit and any valid length k string behind; After that,
    #    we continue the loop to consider the remaining cases, i.e., we put a '1' at this digit.
    #    If consecutive 1s are found, we exit the loop and return the answer.
    #    By the end of the loop, we return count+1 to include the number n itself.
    # ----------------------------------------------------------------------------------------
    #    For example, if n is 10010110,
    #    we find first '1' at 7 digits to the right, we add range 00000000-01111111, which is f(7);
    #    second '1' at 4 digits to the right, add range 10000000-10001111, f(4);
    #    third '1' at 2 digits to the right, add range 10010000-10010011, f(2);
    #    fourth '1' at 1 digits to the right, add range 10010100-10010101, f(1);
    #
    #    Those ranges are continuous from 00000000 to 10010101.
    #    And any greater number <= n will have consecutive 1.
    #
    def findIntegers_solution_1(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        x, y = 1, 2
        res = 0
        num += 1
        while num:
            if num & 1 and num & 2:
                res = 0
            res += x * (num & 1)
            num >>= 1
            x, y = y, x + y
        return res

    def findIntegers_solution_1_shorter_version(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        res, x, y, num = 0, 1, 2, num + 1
        while num:
            res, x, y, num = (
                res if not num & 1 else x if num & 2 else res + x,
                y,
                x + y,
                num >> 1,
            )
        return res

    def findIntegers_solution_2(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        num = list(map(int, bin(num)[2:]))
        oneSmall, zeroSmall, oneEven, zeroEven = 0, 0, 0, 1
        for x in num:
            isOne = x == 1
            (oneSmall, zeroSmall, oneEven, zeroEven) = (
                zeroSmall,
                zeroSmall
                + oneSmall
                + (oneEven if isOne else 0)
                + (zeroEven if isOne else 0),
                zeroEven if isOne else 0,
                (zeroEven if not isOne else 0) + (oneEven if not isOne else 0),
            )
        return oneSmall + zeroSmall + oneEven + zeroEven

    def non_consecutive_1_GFG(self, n: int):
        # a : ending with 0 (can append both 0 or 1 to it)
        # b : ending with 1 (can append only 0 to it)
        a = [0] * n
        b = [0] * n

        # a[0] = 1
        # b[0] = 1
        a[0] = b[0] = 1

        # 1 -> n-1 (use DP)
        for i in range(1, n):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        return a[n - 1] + b[n - 1]


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_findIntegers(self):
        s = Solution()
        for num, solution in ([5, 5], [8, 6]):
            self.assertEqual(s.findIntegers_solution_1(num), solution)
            self.assertEqual(s.findIntegers_solution_1_shorter_version(num), solution)
            self.assertEqual(s.findIntegers_solution_2(num), solution)

    def test_non_consecutive_1_GFG(self):
        s = Solution()
        for num, solution in (
            [3, 5],
            [2, 3],
            [4, 8]  # For 4,  list having non-consecutive '1's is
            # [0001][0010][0100][1000][1010][1001][0101][0000]
            # Input :
            # 4
            # Output :
            # 8
        ):
            self.assertEqual(s.non_consecutive_1_GFG(num), solution)


if __name__ == "__main__":
    unittest.main()
