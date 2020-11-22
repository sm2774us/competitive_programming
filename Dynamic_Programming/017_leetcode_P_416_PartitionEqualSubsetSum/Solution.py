#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 416: Partition Equal Subset Sum
#
# Description:
#
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
#
#
# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
# **************************************************************************
# Source: https://leetcode.com/problems/partition-equal-subset-sum/ (LeetCode - Problem 416 - Partition Equal Subset Sum)
# **************************************************************************
#
# Detailed Explanation of all Possible Solutions:
# **************************************************************************
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/462699/Whiteboard-Editorial.-All-Approaches-explained.
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):

    # Solution_1 : Dynamic Programming 0-1 Knapsack based Solution
    def canPartition_DP_ZeroOneKnapsack(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1:
            return False
        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[s] or (s >= x and dp[s - x]) for s in range(target + 1)]
            if dp[target]:
                return True
        return False

    # Solution_2 : DFS + Memoization
    def canPartition_DP_Memoization(self, nums: List[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0:
                return False
            if target == 0:
                return True
            if target in cache:
                return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i + 1 :], target - n, cache):
                    return True
            return False

        s = sum(nums)
        if s % 2 != 0:
            return False
        return dfs(nums, s // 2, set())


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canPartition(self) -> None:
        sol = Solution()
        for nums, solution in ([[1, 5, 11, 5], True], [[1, 2, 3, 5], False]):
            self.assertEqual(solution, sol.canPartition_DP_ZeroOneKnapsack(nums))
            self.assertEqual(solution, sol.canPartition_DP_Memoization(nums))


# main
if __name__ == "__main__":
    unittest.main()
