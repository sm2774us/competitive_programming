#
# Time : O(n log n)
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 164: Maximum Gap
#
# Description:
#
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example 1:
#
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.
# Example 2:
#
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# Note:
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
# Try to solve it in linear time/space.
#
# **************************************************************************
# Source: https://leetcode.com/problems/maximum-gap/ (LeetCode - Problem 164 - Maximum Gap)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
#
# Intuition
# **************************************************************************
# 1) We want to make sure those two numbers forming the maximum difference fall into separate buckets so that we do not
#    need to worry about the numbers in the same bucket.
#    To achieve this we want the size of each bucket to be less than the maximum difference.
#
# 2) Assuming md denotes the maximum difference, then we have :
#    md * (len(nums) - 1) >= b - a, so md >= (b - a) / (len(nums) - 1)
#    , since md must be integer, we get
#    md >= math.ceil((b - a) / (len(num) - 1))
#    , thus we make
#    size = math.ceil((b - a) / (len(num) - 1)).
#
# 3) Then by making the number of buckets to be
#    (b - a) // size + 1
#    , it is guaranteed that the final bucket size is less than maximum difference hence those two numbers
#    forming maximum difference will be in separate buckets.
#
# 4) Finally, we find the maximum difference between two adjacent buckets
#    (min value of current bucket and max value of previous bucket) and that will be the answer.
#
from typing import List
import math

import unittest

class Solution(object):
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = math.ceil((b - a) / (len(nums) - 1))
        bucket = [[None, None] for _ in range((b - a) // size + 1)]
        for n in nums:
            b = bucket[(n - a) // size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maximumGap(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[3,6,9,1], 3],
            [[10], 0]
        ):
            self.assertEqual(solution, sol.maximumGap(nums))


# main
if __name__ == "__main__":
    unittest.main()
