#
# Time  :
# Space :
#
# @tag : Dynamic Programming ; Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 646: Maximum Length of Pair Chain
#
# Description:
#
# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
#   Input: [[1,2], [2,3], [3,4]]
#   Output: 2
#   Explanation: The longest chain is [1,2] -> [3,4]
#
# Note:
#   1. The number of given pairs will be in the range [1, 1000].
#
# **************************************************************************
# Source: https://leetcode.com/problems/maximum-length-of-pair-chain/ (LeetCode - Problem 646 - Maximum Length of Pair Chain)
#         https://practice.geeksforgeeks.org/problems/max-length-chain/1 (GeeksForGeeks - Max length chain)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List
import math

import unittest


class Solution(object):
    def findLongestChainUsingGreedy(self, pairs: List[List[int]]) -> int:
        cur, res = -math.inf, 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur, res = p[1], res + 1
        return res

    def findLongestChainUsingDP(self, pairs: List[List[int]]) -> int:
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLongestChain(self) -> None:
        sol = Solution()
        for pairs, solution in (
            [[[1, 2], [2, 3], [3, 4]], 2],
            [[[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]], 3],
            [[[5, 10], [1, 11]], 1],
        ):
            self.assertEqual(solution, sol.findLongestChainUsingGreedy(pairs))
            self.assertEqual(solution, sol.findLongestChainUsingDP(pairs))


# main
if __name__ == "__main__":
    unittest.main()
