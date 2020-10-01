#
# Time : O(N); Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 992: Subarrays with K Different Integers
#
# Description:
#
# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
#
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
#
# Return the number of good subarrays of A.
#
#
#
# Example 1:
#
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#
# Example 2:
#
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
#
#
# Note:
#
#   1. 1 <= A.length <= 20000
#   2. 1 <= A[i] <= A.length
#   3. 1 <= K <= A.length
#
# **************************************************************************
# Source: https://leetcode.com/problems/relative-sort-array/ (Leetcode - Problem 1122 - Relative Sort Array)
#         https://practice.geeksforgeeks.org/problems/relative-sorting/0 (GeeksForGeeks - Relative Sorting)
#
# Solution Hints :
#   Sliding Window Templates -
#       https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!
#       https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from typing import List

import unittest


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def subarraysWithAtMostKDistinct(A, K):
            import collections

            d = collections.defaultdict(int)
            left = right = 0
            no_dts = 0  # number of distinct integers
            res = 0

            while right < len(A):
                if d[A[right]] == 0:
                    no_dts += 1
                d[A[right]] += 1

                while no_dts == K + 1:
                    if d[A[left]] == 1:
                        no_dts -= 1
                    d[A[left]] -= 1
                    left += 1

                if no_dts <= K:
                    # right-left+1 is the current number of at most K distinct substrings
                    # in A[left:right+1] and ending with A[right]
                    res += right - left + 1
                right += 1
            return res

        return subarraysWithAtMostKDistinct(A, K) - subarraysWithAtMostKDistinct(
            A, K - 1
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_subarraysWithKDistinct(self) -> None:
        sol = Solution()
        for A, K, solution in ([[1, 2, 1, 2, 3], 2, 7], [[1, 2, 1, 3, 4], 3, 3]):
            self.assertEqual(solution, sol.subarraysWithKDistinct(A, K))


if __name__ == "__main__":
    unittest.main()
