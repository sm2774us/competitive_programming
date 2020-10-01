#
# Time : O(N); Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 974: Subarray Sums Divisible by K
#
# Description:
#
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
#
#
#
# Example 1:
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
#
# Note:
#
#   * 1 <= A.length <= 30000
#   * -10000 <= A[i] <= 10000
#   * 2 <= K <= 10000
#
# **************************************************************************
# Source: https://leetcode.com/problems/subarray-sums-divisible-by-k/ (Leetcode - Problem 974 - Subarray Sums Divisible by K)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from typing import List

import unittest


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        d = [1] + [0] * K  # range of key is 0 <= key < K because key always mod by K
        acc = 0
        for a in A:
            acc = (
                acc + a
            ) % K  # it's works because a % k % k % k .... n times is still same as a % k
            if d[acc]:
                res += d[acc]
            d[acc] += 1
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_subarraysDivByK(self) -> None:
        sol = Solution()
        self.assertEqual(7, sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))


if __name__ == "__main__":
    unittest.main()
