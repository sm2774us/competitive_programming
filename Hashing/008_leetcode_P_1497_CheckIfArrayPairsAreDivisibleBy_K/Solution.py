#
# Time : O(N); Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 1497: Check If Array Pairs Are Divisible by k
#
# Description:
#
# Given an array of integers arr of even length n and an integer k.
#
# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
#
# Return True If you can find a way to do that or False otherwise.
#
#
#
# Example 1:
#
# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:
#
# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:
#
# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
# Example 4:
#
# Input: arr = [-10,10], k = 2
# Output: true
# Example 5:
#
# Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
# Output: true
#
#
# Constraints:
#   * arr.length == n
#   * 1 <= n <= 10^5
#   * n is even.
#   * -10^9 <= arr[i] <= 10^9
#   * 1 <= k <= 10^5
#
# **************************************************************************
# Source: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/ (Leetcode - Problem 1497 - Check If Array Pairs Are Divisible by k)
#         https://practice.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem/0 (GeeksForGeeks - Array Pair Sum Divisibility Problem)
#
# Solution Hints :
#   [ Count positive remainder and cancel the other whenever locate a pair - Template ] :
#       https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/discuss/709226/JavaPython-3-Count-positive-remainder-and-cancel-the-other-whenever-locate-a-pair.
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from typing import List

import unittest


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            a %= k
            theOther = (k - a) % k
            if cnt[theOther] > 0:
                cnt[theOther] -= 1
            else:
                cnt[a] += 1
        return all(c == 0 for c in cnt)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canArrange(self) -> None:
        sol = Solution()
        for arr, k, solution in (
            [[1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True],
            [[1, 2, 3, 4, 5, 6], 7, True],
            [[1, 2, 3, 4, 5, 6], 10, False],
            [[-10, 10], 2, True],
            [[-1, 1, -2, 2, -3, 3, -4, 4], 3, True],
        ):
            self.assertEqual(solution, sol.canArrange(arr, k))


if __name__ == "__main__":
    unittest.main()
