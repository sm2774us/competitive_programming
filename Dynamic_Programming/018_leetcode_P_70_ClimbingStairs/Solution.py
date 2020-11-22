#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 70: Climbing Stairs
#
# Description:
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#   * 1 <= n <= 45
#
# **************************************************************************
# Source: https://leetcode.com/problems/climbing-stairs/ (LeetCode - Problem 70 - Climbing Stairs)
# **************************************************************************
#
# References:
# **************************************************************************
# https://mathworld.wolfram.com/TribonacciNumber.html
# **************************************************************************
#
from typing import List
from functools import lru_cache

import unittest


class Solution(object):

    # Top down + memoization (dictionary)
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]

    # Solution_1 : Dynamic Programming - Top Down
    @lru_cache(None)
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # Bottom up, O(n) space
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]

    # Bottom up, constant space
    def climbStairs3(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]

    # Top down + memorization (list)
    def climbStairs4(self, n: int) -> int:
        if n == 1:
            return 1
        dic = [-1 for i in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    # Fibonacci Solution
    def climbStairs5(self, n: int) -> int:
        return int(
            (5 ** 0.5 / 5)
            * (((1 + 5 ** 0.5) / 2) ** (n + 1) - ((1 - 5 ** 0.5) / 2) ** (n + 1))
        )

    # Matrix Power Solution
    def climbStairs6(self, n: int) -> int:
        def mul(A, B):
            N = 0, 1
            return [[sum(A[i][k] * B[k][j] for k in N) for j in N] for i in N]

        def pow(A, n):
            if n == 1:
                return A
            P = pow(A, n / 2)
            P = mul(P, P)
            return mul(P, A) if n % 2 else P

        return pow([[1, 1], [1, 0]], n + 1)[0][1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_climbStairs(self) -> None:
        sol = Solution()
        for n, solution in ([2, 2], [3, 3]):
            self.assertEqual(solution, sol.climbStairs(n))
            self.assertEqual(solution, sol.climbStairs1(n))
            self.assertEqual(solution, sol.climbStairs2(n))
            self.assertEqual(solution, sol.climbStairs3(n))
            self.assertEqual(solution, sol.climbStairs4(n))
            self.assertEqual(solution, sol.climbStairs5(n))
            # self.assertEqual(solution, sol.climbStairs6(n))


# main
if __name__ == "__main__":
    unittest.main()
