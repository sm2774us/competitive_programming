#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Two numbers with sum closest to zero
#
# Given an integer array of N elements. You need to find the sum of two elements such that sum is closest to zero.
#
# Example 1:
#
# Input:
# N = 3
# arr[] = {-8 -66 -60}
# Output: -68
# Explanation: Sum of two elements closest to
# zero is -68 using numbers -60 and -8.
#
# Example 2:
#
# Input:
# N = 6
# arr[] = {-21 -67 -37 -18 4 -65}
# Output: -14
# Explanation: Sum of two elements closest to
# zero is -14 using numbers -18 and 4.
#
# Your Task:
# You don't need to read input or print anything. You just need to complete the function closestToZero() which takes an array arr[] and its size n as inputs and returns the sum closest to zero that can be formed by summing any two elements in the array.
#
#
# Expected Time Complexity: O(NlogN).
# Expected Auxiliary Space: O(1).
#
#
# Constraints:
# 1 ≤ N ≤ 103
# -106 ≤ a[i] ≤ 106
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/two-numbers-with-sum-closest-to-zero1737/1 (GeeksForGeeks - Two numbers with sum closest to zero)
#         Variant: https://leetcode.com/discuss/interview-question/241808/Google-Two-sum-closest (Google - OnSite - Two Sum - Closest to Target)
#         Variant: https://leetcode.com/problems/two-sum-less-than-k (LeetCode - Problem 1099 - Two Sum Less Than K)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# References:
# **************************************************************************
# https://github.com/ASK1995/Leetcode/blob/master/1099.%20Two%20Sum%20Less%20Than%20K
# https://leetcode.com/discuss/interview-question/241808/Google-Two-sum-closest
#
from typing import List

import unittest


class Solution(object):
    def partition(self, arr, si, ei):
        x = arr[ei]
        i = si - 1

        for j in range(si, ei):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
        return i + 1

    # Implementation of Quick Sort
    # arr[] --> Array to be sorted
    # si --> Starting index
    # ei --> Ending index
    def quickSort(self, arr, si, ei):
        pi = 0  # Partitioning index */
        if si < ei:
            pi = self.partition(arr, si, ei)
            self.quickSort(arr, si, pi - 1)
            self.quickSort(arr, pi + 1, ei)

    def minAbsSumPair(self, arr: List[int], n: int) -> int:

        # Variables to keep track
        # of current sum and minimum sum
        sum, min_sum = 0, 10 ** 9

        # left and right index variables
        l = 0
        r = n - 1

        # variable to keep track of
        # the left and right pair for min_sum
        min_l = l
        min_r = n - 1

        # Array should have at least two elements*/
        if n < 2:
            # print("Invalid Input", end="")
            return

        # Sort the elements */
        self.quickSort(arr, l, r)

        while l < r:
            sum = arr[l] + arr[r]

            # If abs(sum) is less
            # then update the result items
            if abs(sum) < abs(min_sum):
                min_sum = sum
                min_l = l
                min_r = r
            if sum < 0:
                l += 1
            else:
                r -= 1

        # print("The two elements whose sum is minimum are",
        #      arr[min_l], "and", arr[min_r])
        return arr[min_l] + arr[min_r]

    def twoSumLessThanK_Google_OnSite(self, nums: List[int], target: int) -> List[int]:
        if not nums and not target:
            return []

        nums.sort()
        i = 0
        j = len(nums) - 1
        stack = [0] * 2
        cur_closest = -1

        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] == target:
                j -= 1
            else:
                stack[0] = nums[i]
                stack[1] = nums[j]
                cur_closest = max(cur_closest, nums[i] + nums[j])
                i += 1
        # If you need to return the actual summation value instead of the two integers:
        # For example: LeetCode - Problem 1099 - Two Sum Less Than K
        # - https://leetcode.com/problems/two-sum-less-than-k
        # print(cur_closest)
        # return cur_closest
        return stack


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_minAbsSumPair(self):
        s = Solution()
        for nums, solution in (
            [[-8, -66, -60], -68],
            [[-21, -67, -37, -18, 4, -65], -14],
            [[1, 60, -10, 70, -80, 85], 5],
        ):
            self.assertEqual(s.minAbsSumPair(nums, len(nums)), solution)

    def test_twoSumLessThanK_Google_OnSite(self):
        s = Solution()
        for nums, target, solution in (
            [[1, 2, 3, 4, 5], 10, [4, 5]],
            [[-1, 2, 1, -4], 4, [2, 1]],
        ):
            self.assertEqual(
                s.twoSumLessThanK_Google_OnSite(nums, target), sorted(solution)
            )


if __name__ == "__main__":
    unittest.main()
