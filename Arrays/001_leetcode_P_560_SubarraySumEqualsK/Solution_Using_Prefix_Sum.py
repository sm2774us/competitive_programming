#
# Time : O(N); Space: O(N)
# @tag : Arrays ; Prefix Sum
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Leetcode - Problem 560 - Subarray Sum Equals K
#
# Description:
#
# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# For example,
#  Input:nums = [1,1,1], k = 2
#  Output: 2
#
# Constraints:
#   1) The length of the array is in range [1, 20,000].
#   2) The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
# **************************************************************************
# Source: https://leetcode.com/problems/subarray-sum-equals-k/ (Leetcode - Problem 560 - Subarray Sum Equals K)
#         https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0 (GeeksForGeeks - Subarray with given sum)
#
from collections import defaultdict
from typing import List

import unittest


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0

        sum_table = defaultdict(int)
        sum_table[0] = 1

        counter = 0

        for i in range(len(nums)):
            # update prefix sum
            prefix_sum += nums[i]

            """
            if prefix sum of ( s - k ) and prefix sum of s exist, then subarray with sum k must exist
            """
            counter += sum_table.get(prefix_sum - k, 0)

            # update sum table
            sum_table[prefix_sum] += 1

        return counter


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_subarraySum(self) -> None:
        s = Solution()
        # nums = [1, 1, 1]
        # k = 2
        # solution = 2
        # self.assertEqual(solution, s.subarraySum(nums, k), "Should return the total number of continuous subarrays whose sum equals to K")
        for nums, k, solution in (
            [[1, 1, 1], 2, 2],  # [1,1] [1,1]
            [[1, 2, 3], 3, 2],  # [1,2] [3]
            [
                [2, 2, 3, 0, 4, -1, 1, 6],
                7,
                5,
            ],  # [2,2,3] [2,2,3,0] [3,0,4] [3,0,4,-1,1] [1,6]
        ):
            self.assertEqual(
                solution,
                s.subarraySum(nums, k),
                "Should return the total number of continuous subarrays whose sum equals to K",
            )


if __name__ == "__main__":
    unittest.main()
