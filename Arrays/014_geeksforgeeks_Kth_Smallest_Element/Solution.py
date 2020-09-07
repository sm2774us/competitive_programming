#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Kth smallest element
# **************************************************************************
# Given an array arr[] and a number K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
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
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0 ( Kth smallest element )
# Variant:
#          https://leetcode.com/problems/kth-largest-element-in-an-array/ ( Leetcode - Problem 215 - Kth Largest Element in an Array )
#
# Solution Hint: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
#                https://yuanzhe.me/2017/10/21/LeetCode-Heap-215-kth-largest-element-in-an-array/
#
from typing import List
import heapq

import unittest


class Solution:

    # O(nlgn) time
    def findKthSmallest1(self, nums: List[int], k: int) -> int:
        return sorted(nums)[k - 1]

    # O(nk) time, bubble sort idea, TLE
    def findKthSmallest2(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[k - 1]

    # O(nk) time, selection sort idea
    def findKthSmallest3(self, nums: List[int], k: int) -> int:
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] < nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]

    # O(k+(n-k)lgk) time, min-heap
    def findKthSmallest4(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def findKthSmallest5(self, nums: List[int], k: int) -> int:
        return heapq.nsmallest(k, nums)[k - 1]

    # choose the right-most element as pivot
    def partition(self, nums: List[int], l: int, r: int) -> int:
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    # O(n) time, quick selection
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1 :], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findKthSmallest(self) -> None:
        s = Solution()
        for nums, k, solution in (
            [
                [7, 10, 4, 3, 20, 15],
                3,
                7,
            ],  # The 3rd smallest element in the given array is 7.
            [
                [7, 10, 4, 20, 15],
                4,
                15,
            ],  # The 4th smallest element in the given array is 15.
            [
                [3, 10, 8, 20, 15],
                2,
                8,
            ],  # The 2nd smallest element in the given array is 8.
            [
                [9, 10, 8, 11, 16, 35, 46],
                5,
                16,
            ],  # The 5th smallest element in the given array is 16.
        ):
            self.assertEqual(
                solution,
                s.findKthSmallest(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthSmallest1(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthSmallest2(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthSmallest3(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthSmallest4(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthSmallest5(nums, k),
                "Should return the Kth smallest element in the array N",
            )


if __name__ == "__main__":
    unittest.main()
