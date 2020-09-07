#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 75. Sort Colors
#
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
#
# We define the pivot index as the index where the sum of all the numbers to the left of the index
# is equal to the sum of all the numbers to the right of the index.
#
# If no such index exists, we should return -1. If there are multiple pivot indexes,
# you should return the left-most pivot index.
#
# Example 1:
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
#
# Example 2:
#
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
# Constraints:
#
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
#
# **************************************************************************
# Source: https://leetcode.com/problems/find-pivot-index/ (Leetcode - Problem 724 - Find Pivot Index)
#         https://practice.geeksforgeeks.org/problems/equilibrium-point/0 (GeeksForGeeks - Equilibrium point)
#
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# As we iterate through the array of numbers, we need to keep track of the sum of the values on the current
# number's left and its right.
#
# The following debugger trace demonstrates the values of the variables in each loop
# before the left == right line
#
# Input: [1, 7, 3, 6, 5, 6]
#
# index: 0, num: 1, left: 0, right: 27
# index: 1, num: 7, left: 1, right: 20
# index: 2, num: 3, left: 8, right: 17
# index: 3, num: 6, left: 11, right: 11 <-- Found!!!
#
from typing import List

import unittest


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_pivotIndex(self) -> None:
        s = Solution()
        for nums, solution in (
            [
                [1, 7, 3, 6, 5, 6],
                3,
            ],  # The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
            [
                [1, 3, 5, 2, 2],
                2,
            ],  # equilibrium point is at position 3 as elements below it (1+3) = elements after it (2+2)
            [
                [1, 2, 3],
                -1,
            ],  # no index that satisfies the conditions in the problem statement, so return -1
        ):
            self.assertEqual(
                solution,
                s.pivotIndex(nums),
                """Should find the pivot index as the index where the sum of all the numbers to the left of the 
                             index is equal to the sum of all the numbers to the right of the index""",
            )


if __name__ == "__main__":
    unittest.main()
