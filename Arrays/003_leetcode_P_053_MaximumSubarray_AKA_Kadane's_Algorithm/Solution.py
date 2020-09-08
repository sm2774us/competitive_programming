#
# Time : O(N); Space: O(N)
# @tag : Arrays [ Dynamic Programming ]
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Description:
#
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.
#
# Kadane's Algorithm (https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm):
# **************************************************************************
# The runtime complexity of Kadane's algorithm is O(n).
# **************************************************************************
# Source: https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6#:~:text=Given%20an%20array%2C%20the%20algorithm,can%20be%20of%20any%20dimension.&text=And%20since%20we%20want%20the,anew%20from%20the%20current%20element).
# Source: https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
# **************************************************************************
# Given an array, the algorithm to find the maximum subarray sum is called Kadane’s Algorithm.
# The array can be of any dimension.
# **************************************************************************
# Source:
#   https://leetcode.com/problems/maximum-subarray/ (Leetcode - Problem 53 - Maximum Subarray)
#   https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0 (GeeksForGeeks - Kadane's Algorithm)
#
from typing import List
from itertools import accumulate

import unittest


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     for i in range(1, len(nums)):
    #         if nums[i - 1] > 0:
    #             nums[i] += nums[i - 1]
    #     return max(nums)

    # Cut the if-condition above
    # def maxSubArray(self, nums: List[int]) -> int:
    #     for i in range(1, len(nums)):
    #         nums[i] = max(nums[i], nums[i-1] + nums[i])
    #     return max(nums)

    # Reduce to one-line using accumulate
    def maxSubArray(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: x + y if x > 0 else y))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSubArray(self) -> None:
        s = Solution()
        for nums, solution in (
            [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],  # [4,-1,2,1] has the largest sum = 6
            [[3, 2, -1, -2], 5],  # [3,2] has the largest sum = 5
            [[2, -1, 2], 3],  # [2,-1,2] has the largest sum = 3
        ):
            self.assertEqual(
                solution,
                s.maxSubArray(nums),
                """Should find the contiguous subarray with maximum sum 
                             and return the sum""",
            )


if __name__ == "__main__":
    unittest.main()
