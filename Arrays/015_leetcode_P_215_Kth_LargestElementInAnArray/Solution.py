#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Kth smallest element
# **************************************************************************
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# **************************************************************************
# Source: https://leetcode.com/problems/kth-largest-element-in-an-array/ ( Leetcode - Problem 215 - Kth Largest Element in an Array )
#
# Variant:
#          https://practice.geeksforgeeks.org/problems/kth-smallest-element/0 ( Kth smallest element )
#
# Solution Hint: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
#                https://yuanzhe.me/2017/10/21/LeetCode-Heap-215-kth-largest-element-in-an-array/
#
from typing import List
import heapq

import unittest


class Solution:

    # O(nlgn) time
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    # O(nk) time, selection sort idea
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k - 1]

    # O(n) time, quick selection
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums) + 1 - k)

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
                [3, 2, 1, 5, 6, 4],
                2,
                5,
            ],  # The 2nd largest element in the given array is 5.
            [
                [3, 2, 3, 1, 2, 4, 5, 5, 6],
                4,
                4,
            ],  # The 4th largest element in the given array is 4.
            [
                [3, 10, 8, 20, 15],
                2,
                15,
            ],  # The 2nd largest element in the given array is 15.
            [
                [9, 10, 8, 11, 16, 35, 46],
                5,
                10,
            ],  # The 5th largest element in the given array is 10.
        ):
            self.assertEqual(
                solution,
                s.findKthLargest(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthLargest1(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthLargest2(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthLargest3(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthLargest4(nums, k),
                "Should return the Kth smallest element in the array N",
            )
            self.assertEqual(
                solution,
                s.findKthLargest5(nums, k),
                "Should return the Kth smallest element in the array N",
            )


if __name__ == "__main__":
    unittest.main()
