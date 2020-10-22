#
# Time  :
# Space :
#
# @tag : Dynamic Programming ; Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 300: Longest Increasing Subsequence
#
# Description:
#
# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
#
# Follow up:
#   Could you improve it to O(n log n) time complexity?
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-increasing-subsequence/ (LeetCode - Problem 300 - Longest Increasing Subsequence)
#         https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0 (GeeksForGeeks - Longest Increasing Subsequence)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# References:
# **************************************************************************
# https://edydfang.com/2019/11/19/longest-increasing-subsequence-problem-and-its-duality/
#
#
from typing import List

import unittest


class Solution(object):
    # Greedy Algorithm + Binary Search Algorithm
    # Time complexity: O(n log n)
    def lengthOfLIS_Using_Greedy_and_BinarySearch(self, nums: List[int]) -> int:
        # greedy and binary search
        tail_list = [0] * len(nums)
        size = 0
        for height in nums:
            # i: start index of rows
            # j: end index of rows
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                # note here we need <= to ensure in each row is strictly decreasing
                # according to the problem description
                if tail_list[m] <= height:
                    i = m + 1
                else:
                    j = m
            tail_list[i] = height
            size = max([i + 1, size])
        return size

    # DP
    # Time complexity: O(n^2)
    def lengthOfLIS_Using_DP(self, nums: List[int]) -> int:
        # DP, convert to Longest Non-decreasing Subsequence Problem (LNDS)
        # memo[i] LNDS including ending with arr[i]
        n = len(nums)
        if n == 0:
            return 0
        memo = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    memo[i] = max([memo[i], memo[j] + 1])
        return max(memo)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lengthOfLIS(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[10, 9, 2, 5, 3, 7, 101, 18], 4],
            [[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6],
            [[5, 8, 3, 7, 9, 1], 3],
        ):
            self.assertEqual(
                solution, sol.lengthOfLIS_Using_Greedy_and_BinarySearch(nums)
            )
            self.assertEqual(solution, sol.lengthOfLIS_Using_DP(nums))


# main
if __name__ == "__main__":
    unittest.main()
