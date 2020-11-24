#
# Time  :
# Space :
#
# @tag : Divide And Conquer ; Binary Search
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 4: Median of two sorted arrays
#
# Description:
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
# Constraints:
#
#   * nums1.length == m
#   * nums2.length == n
#   * 0 <= m <= 1000
#   * 0 <= n <= 1000
#   * 1 <= m + n <= 2000
#   * -106 <= nums1[i], nums2[i] <= 106
#
# **************************************************************************
# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/ (LeetCode - Problem 004 - Median of Two Sorted Arrays)
#         https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/ (GeeksForGeeks - Median of two sorted arrays of different sizes)
# **************************************************************************
#
# References:
# **************************************************************************
# https://www.youtube.com/watch?v=LPFhl65R7ww
#
from typing import List
from statistics import median
import sys

import unittest


class Solution(object):

    # def median(self, lst):
    #     quotient, remainder = divmod(len(lst), 2)
    #     if remainder:
    #         return sorted(lst)[quotient]
    #     return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2

    # Solution_1
    #
    def findMedianSortedArrays_solution_1(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if not nums1 and not nums2:
            return None
        if not nums2:
            return median(nums1)
        if not nums1:
            return median(nums2)
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2:
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
        l, r = 0, N2 * 2
        while l <= r:
            j = (l + r) >> 1
            i = N1 + N2 - j
            L1 = -sys.maxsize - 1 if i == 0 else nums1[(i - 1) >> 1]
            L2 = -sys.maxsize - 1 if j == 0 else nums2[(j - 1) >> 1]
            R1 = sys.maxsize if i == 2 * N1 else nums1[i >> 1]
            R2 = sys.maxsize if j == 2 * N2 else nums2[j >> 1]
            if L1 > R2:
                l = j + 1
            elif L2 > R1:
                r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0

    # Solution_2
    #
    def findMedianSortedArrays_solution_2(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if not nums1 and not nums2:
            return None
        if not nums2:
            return median(nums1)
        if not nums1:
            return median(nums2)
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_search(self) -> None:
        sol = Solution()
        for nums1, nums2, solution in (
            [[-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3],
            [[2, 3, 5, 8], [10, 12, 14, 16, 18, 20], 11],
            [[1, 3], [2], 2],
            [[1, 2], [3, 4], 2.5],
            [[0, 0], [0, 0], 0],
            [[], [1], 1],
            [[2], [], 2],
        ):
            self.assertEqual(
                solution, sol.findMedianSortedArrays_solution_1(nums1, nums2)
            )
            self.assertEqual(
                solution, sol.findMedianSortedArrays_solution_2(nums1, nums2)
            )


# main
if __name__ == "__main__":
    unittest.main()
