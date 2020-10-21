#
# Time : O(n log n)
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 991: Broken Calculator
#
# Description:
#
# On a broken calculator that has a number showing on its display, we can perform two operations:
#
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
#
# Return the minimum number of operations needed to display the number Y.
#
#
# Example 1:
# #########################################
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
#
# Example 2:
# #########################################
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
#
# Example 3:
# #########################################
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
#
# Example 4:
# #########################################
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
#
#
# Note:
#
#   1) 1 <= X <= 10^9
#   2) 1 <= Y <= 10^9
#
# **************************************************************************
# Source: https://leetcode.com/problems/broken-calculator/ (LeetCode - Problem 991 - Broken Calculator)
#         https://practice.geeksforgeeks.org/problems/find-optimum-operation4504/1 (GeeksForGeeks - Minimum Operations)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Instead of thinking backward by incrementing and dividing Y, we can think this problem forwardly.
#
# Intuition: We want to first decrement X to some extent, then start to multiply it until it gets close to Y.
# This process equals to decrementing from a number X*(2^N) to Y, where X*(2^N) >= Y, and the number we are decrementing is no longer 1, instead, it is 2^N
#
# Therefore, we can be greedy.
# 1) Step1: Find the smallest N, for which X*(2^N) >= Y
# 2) Step2: Start counting the number of decrements we need to do, where we are using 2^N to decrement, until we cannot get any closer to Y.
# 3) Step3: Then, use 2^(N-1) to decrement until we cannot get any closer to Y.
# 4) Step4: Use 2^(N-2) to decrement, and do this recursively until we are using2^0, which is 1 to decrement.
# 5) Finally, return the number of decrements we have made, remember to plus N, which is the number of multiplication.
#
#
from typing import List

import unittest


class Solution(object):
    # def brokenCalc(self, X, Y):
    #     multiple = 1
    #     res = 0
    #     while X * multiple < Y:
    #         multiple *= 2
    #         res += 1
    #     diff = X * multiple - Y
    #     while diff:
    #         res += diff / multiple
    #         diff -= diff / multiple * multiple
    #         multiple /= 2
    #     return res

    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if Y <= X:
            return X - Y

        count = 0
        N = 1
        while X * 2 ** N < Y:
            N += 1
        remain = (X * 2 ** N) - Y
        count += N
        while N >= 0:
            count += remain // (2 ** N)
            remain %= 2 ** N
            N -= 1

        return count

    def minOperations(self, Y):
        X = 1
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if Y <= X:
            return X - Y

        count = 0
        N = 1
        while X * 2 ** N < Y:
            N += 1
        remain = (X * 2 ** N) - Y
        count += N
        while N >= 0:
            count += remain // (2 ** N)
            remain %= 2 ** N
            N -= 1

        return count + 1


class BrokenCalculatorLeetCodeTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_brokenCalc(self) -> None:
        sol = Solution()
        for X, Y, solution in ([2, 3, 2], [5, 8, 2], [3, 10, 3], [1024, 1, 1023]):
            self.assertEqual(solution, sol.brokenCalc(X, Y))


class MinimumOperationsGeeksForGeeksTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minOperations(self) -> None:
        sol = Solution()
        for Y, solution in ([8, 4], [7, 5]):
            self.assertEqual(solution, sol.minOperations(Y))


# main
if __name__ == "__main__":
    unittest.main()
