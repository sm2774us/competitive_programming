#
# Time : O(N^3); Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 18: 4Sum
#
# Description:
#
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
# such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/4sum/ (Leetcode - Problem 18 - 4Sum)
#         https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers/0 (GeeksForGeeks - Find all four sum numbers)
#
#
# The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum.
# Some optimization was be made knowing the list is sorted.
#
from typing import List

import unittest


class Solution:
    # O(N^3) Solution
    # Complexity of: 2-sum is O(N),
    #                3-sum is O(N^2),
    #                4-sum is O(N^3),
    #                .
    #                .
    #                .
    #                and in general is complexity of k-sum is O(N^k-1)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums: List[int], target: int, N: int, cur: List[int]):
            if (
                len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target
            ):  # if minimum possible sum (every element is first element) > target
                return  # or maximum possible sum (every element is first element) < target, it's impossible to get target anyway
            if N == 2:  # 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # reduce to N-1 sum problem
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        findNsum(
                            nums[i + 1 :], target - nums[i], N - 1, cur + [nums[i]]
                        )

        res = []
        findNsum(sorted(nums), target, 4, [])
        return res

    def checkEqual(self, L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_fourSum(self) -> None:
        sol = Solution()
        self.assertEqual(
            sol.checkEqual(
                [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]],
                sol.fourSum([1, 0, -1, 0, -2, 2], 0),
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
