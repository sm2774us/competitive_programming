#
# Time  :
# Space :
#
# @tag : Divide And Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Google | Phone Screen | Kth Largest Element of Two Sorted Arrays
#
# Description:
#
# iven two sorted arrays nums1 and nums2 of size m and n respectively and an int k. Find the k-th largest element of these arrays.
# Note that it is the k-th largest element in the sorted order, not the k-th distinct element.
#
# Example 1:
#
# Input: nums1 = [-2, -1, 3, 5, 6, 8], nums2 = [0, 1, 2, 5, 9], k = 4
# Output: 5
# Explanation: Union of above arrays will be [-2, -1, 0, 1, 2, 3, 5, 5, 6, 8, 9] and the 4th largest element is 5.
# Example 2:
#
# Input: nums1 = [2, 4], nums2 = [6], k = 1
# Output: 6
# Explanation: union of above arrays will be [2, 4, 6] and the 1st largest element is 6.
# You may assume k is always valid, 1 ≤ k ≤ m + n.
#
# Follow-up:
#   Can you do it in O(logk) time?
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/351782/Google-or-Phone-Screen-or-Kth-Largest-Element-of-Two-Sorted-Arrays (Google | Phone Screen | Kth Largest Element of Two Sorted Arrays)
#         https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0 (GeeksForGeeks - K-th element of two sorted Arrays)
# **************************************************************************
#
from typing import List
from math import inf

import unittest


class Solution(object):
    def kthLargest(self, nums1: List[int], nums2: List[int], k: int) -> int:

        N1, N2 = len(nums1), len(nums2)

        if N1 + N2 < k:
            return inf

        i = N1 - 1
        j = N2 - 1
        current = inf

        while k > 0 and i >= 0 and j >= 0:
            # print(i, j, nums1[i], nums2[j])
            if nums1[i] > nums2[j]:
                current = nums1[i]
                i -= 1
            else:
                current = nums2[j]
                j -= 1
            # print(current, k)
            k -= 1

        return current


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_kthLargest(self) -> None:
        sol = Solution()
        for nums1, nums2, k, solution in (
            [[-2, -1, 3, 5, 6, 8], [0, 1, 2, 5, 9], 4, 5],
            [[2, 4], [6], 1, 6],
            [[2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 6],
        ):
            self.assertEqual(solution, sol.kthLargest(nums1, nums2, k))


# main
if __name__ == "__main__":
    unittest.main()
