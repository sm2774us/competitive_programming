#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 88. Merge Sorted Array
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
# Constraints:
#   1) -10^9 <= nums1[i], nums2[i] <= 10^9
#   2) nums1.length == m + n
#   3) nums2.length == n
#
# **************************************************************************
# Source: https://leetcode.com/problems/merge-sorted-array/ (Leetcode - Problem 88 - Merge Sorted Array)
#         https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/ (GeeksForGeeks - Missing Without Extra Space )
#
from typing import List

import unittest

class Solution:
    # Time: O(n) ; Space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

    # # Time: O(N*log(N)) ; Space: O(1)
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     nums1[m:] = nums2[:n]
    #     nums1.sort()

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_missingNumber(self) -> None:
        s = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]; m = 3; nums2 = [2, 5, 6]; n = 3
        s.merge(nums1, m, nums2, n)
        self.assertEqual([1,2,2,3,5,6], nums1, "Should merge and sort array - nums1 - in-place")
        nums1 = [4, 5, 6, 0, 0, 0]; m = 3; nums2 = [1, 2]; n = 2
        s.merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 4, 5, 6, 0], nums1, "Should merge and sort array - nums1 - in-place")

if __name__ == '__main__':
    unittest.main()

