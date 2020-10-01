#
# Time : O(N*Log(N))
# Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Largest subarray with 0 sum
# Variant Of => LeetCode - Problem - 560: Subarray Sum Equals K
#
# Description:
#
# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
#
# Example 1:
#
# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.
# Your Task:
# You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.
#
# Expected Time Complexity: O(N*Log(N)).
# Expected Auxiliary Space: O(N).
#
# Constraints:
# 1 <= N <= 104
# -1000 <= A[i] <= 1000, for each valid i
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1 (GeeksForGeeks - Largest subarray with 0 sum)
#
# Solution Hint: https://stackoverflow.com/a/27280726 ( Stackoverflow - Accepted Answer - Q> Largest subarray with sum equal to 0 )
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Q> Largest subarray with sum equal to 0
#
# A> This is a typical interview question. Given an array that contains both positive and negative elements without 0,
# find the largest subarray whose sum equals 0.
#
# A nice, linear-time solution is based on the idea that whenever sum(i .. j) = 0,
# it must be that sum(0 .. i-1) = sum(0 .. j) and vice versa.
#
# 1. Essentially you compute the prefix sums sum(0 .. i) for all i, building up a hashtable hash_sum
# in which hash_sum[x] is a list of all positions i having sum(0 .. i) = x.
# 2. Then you go through this hashtable, one sum at a time, looking for any sum that was made by more than one prefix.
# 3. Among all such made-more-than-once sums, you choose the one that was made by a pair of prefixes
#    that are furthest apart -- this is the longest.
#
# NOTE:
#   * For a given sum x, the furthest-apart pair of prefixes that make that sum will always be the smallest
#     and largest entries in hash_sum[x], which will necessarily be the first and last entries
#     (because that's the order they were appended)
#   * So there's no need to loop over the elements in between.
#   * In fact you don't even need a second loop at all: you can keep a running maximum during your first loop,
#     by treating start_index as the rightmost endpoint.
#
#   * To handle an arbitrary difference k: Instead of finding the leftmost occurrence of a prefix summing to
#     current_sum, we need to find the leftmost occurrence of a prefix summing to current_sum - k.
#     But that's just first_with_sum[current_sum - k].

# **************************************************************************
#
from typing import List

from collections import Counter

import unittest


class Solution:
    # Python O(N) solution using Hash-Map.
    def sub_array_sum(self, array: List[int], k: int = 0) -> List[int]:
        start_index = -1
        first_with_sum = {}
        first_with_sum[0] = -1
        best_start = -1
        best_len = 0
        current_sum = 0
        for i in array:
            start_index += 1
            current_sum += i
            if current_sum - k in first_with_sum:
                if start_index - first_with_sum[current_sum - k] > best_len:
                    best_start = first_with_sum[current_sum - k] + 1
                    best_len = start_index - first_with_sum[current_sum - k]
            else:
                first_with_sum[current_sum] = start_index

        if best_len > 0:
            return array[best_start : best_start + best_len]
        else:
            return None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sub_array_sum(self) -> None:
        sol = Solution()
        self.assertEqual(
            [-2, 2, -8, 1, 7], sol.sub_array_sum([15, -2, 2, -8, 1, 7, 10, 23])
        )
        self.assertEqual(
            [-3, -7, 10], sol.sub_array_sum([15, -3, 2, -8, -3, -7, 10, 23])
        )
        self.assertEqual(
            [4, -9, -1, -2, -3, 1, 2, 3, 9, -4],
            sol.sub_array_sum([17, 15, 13, 4, -9, -1, -2, -3, 1, 2, 3, 9, -4, 7]),
        )


if __name__ == "__main__":
    unittest.main()
