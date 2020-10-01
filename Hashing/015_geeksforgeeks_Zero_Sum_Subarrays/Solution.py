#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Zero Sum Subarrays
# NOTE:
# This is a variant of - [ Leetcode - Problem 560 - Subarray Sum Equals K ] https://leetcode.com/problems/subarray-sum-equals-k/.
# And, as such, can be solved by using the same solution with a default value of the argument k set to 0.
# i.e.,
# change this:
# def subarraySum(self, nums: List[int], k: int) -> int:
# to:
# def subarraySum(self, nums: List[int], k: int = 0) -> int:
#
# Description:
#
# You are given an array of integers. You need to print the total count of sub-arrays having their sum equal to 0
#
# Input:
# First line of the input contains an integer T denoting the number of test cases. Each test case consists of two lines. First line of each test case contains an Integer N denoting the size of the array, and the second line contains N space separated integers.
#
# Output:
# For each test case, in a new line, print the total number of subarrays whose sum is equal to 0.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# -1010 <= Ai <= 1010
#
# Example:
# Input:
# 2
# 6
# 0 0 5 5 0 0
# 10
# 6  -1 -3 4 -2 2 4 6 -12 -7
# Output:
# 6
# 4
#
# Explanation:
# Testcase 1: There are 6 subarrays present whose sum is zero. The starting and ending indices are:
# (0,0) (1,1) (0,1) (4,4) (5,5) (4,5)
# Testcase 2: There are 4 subarrays present whose sum is zero. The starting and ending indices are:
# (1,3) (4,5) (1,5) (5,8)
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/zero-sum-subarrays/0 (GeeksForGeeks - Zero Sum Subarrays)
#
#
from typing import List
from collections import defaultdict
import unittest

class Solution:
    def subarrayZeroSum(self, nums: List[int], k: int = 0) -> int:
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

    def test_subarrayZeroSum(self) -> None:
        s = Solution()
        for nums, solution in (
            [[0,0,5,5,0,0], 6],
            [[6,-1,-3,4,-2,2,4,6,-12,-7], 4]
        ):
            self.assertEqual(
                solution,
                s.subarrayZeroSum(nums),
                "Should return the total number of subarrays whose sum equals to 0",
            )


if __name__ == "__main__":
    unittest.main()
