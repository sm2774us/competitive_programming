#
# Time : O(N); Space: O(N)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Description:
#
# 268. Missing Number
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
#
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using
# only constant extra space complexity?
#
# **************************************************************************
# Source: https://leetcode.com/problems/missing-number/ (Leetcode - Problem 268 - Missing Number)
#         https://practice.geeksforgeeks.org/problems/missing-number-in-array/0 (GeeksForGeeks - Missing number in array)
#
import operator
from typing import List
from functools import reduce

import unittest

class Solution:
    # # Time: O(n) ; Space: O(1)
    # # Sum of 0..n minus sum of the given numbers is the missing one.
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     return n * (n + 1) / 2 - sum(nums)

    # # Time: O(n) ; Space: O(1)
    # # Xor-ing the given numbers and 0..n.
    # def missingNumber(self, nums: List[int]) -> int:
    #     reduce(operator.xor, itertools.chain(nums, range(len(nums)+1))

    # # Time: O(n) ; Space: O(1)
    # # Xor-ing with O(1) space.
    # # Xoring 0..n results in [n, 1, n+1, 0][n % 4]. You can also spot the pattern
    # # by looking at xors of such ranges, and it's easy to explain as well.
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     return reduce(operator.xor, nums) ^ [n, 1, n+1, 0][n % 4]

    # Time: O(n) ; Space: O(1)
    # Set/array difference
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1)) - set(nums)).pop()

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_missingNumber(self) -> None:
        s = Solution()
        for nums, solution in (
            [ [3,0,1], 2 ],                 # [1,2] => 3  [3,2] => 5 ;  so 2 Triplets
            [ [9,6,4,2,3,5,7,0,1], 8 ]      # No triplet(s) possible, so -1
        ):
            self.assertEqual(solution, s.missingNumber(nums), "Should return the missing number from the array")

if __name__ == '__main__':
    unittest.main()

