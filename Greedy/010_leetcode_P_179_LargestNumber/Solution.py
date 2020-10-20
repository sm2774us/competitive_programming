#
# Time : O(n log n)
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 179: Largest Number
#
# Description:
#
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
#
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# Example 3:
#
# Input: nums = [1]
# Output: "1"
# Example 4:
#
# Input: nums = [10]
# Output: "10"
#
#
# Constraints:
#
#   * 1 <= nums.length <= 100
#   * 0 <= nums[i] <= 109
#
# **************************************************************************
# Source: https://leetcode.com/problems/largest-number/ (LeetCode - Problem 179 - Largest Number)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
#
# Intuition
# We want to compare the numbers, we need to sort.
# We give the smallest values Bob,
# give the biggest to Alice,
# and leave the second biggest to us.
# Then we repeat this process.
#
#
# Explanation
# We give small value to Bob,
# give the large value to Alice,
# and we pick the medium values.
#
# The final assignment will be like:
# S S S S S S M L M L M L M L M L
#
# The first third part is given to Bob,
# start from A[n/3], we pick one element from every two.
#
#
# Complexity
# Time O(sort)  => O(NlogN)
# Space O(sort) => O(N)
#
# Each time pick the remaining largest 2 and the smallest one to form a triple, choose the 2nd largest
# out of the triplet, repeats till the end;
# Therefore, we can simply sort the array and choose the 2nd, 4th, 6th, ..., from the largest, till we have n / 3 piles.
# We can equally start from the (piles.length / 3 + 1)th pile, followed by (piles.length / 3 + 3)th,
# (piles.length / 3 + 5)th, ..., till the end of the array piles.
#
from typing import List
from functools import cmp_to_key

import unittest

class Solution(object):
    # In an INTERVIEW situation => go with the Quick Sort approach and list the other possible methods ( without actually implementing them )

    def largestNumberUsingBuiltin(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
        return "".join(
            sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1 + n2 > n2 + n1 else (1 if n1 + n2 < n2 + n1 else 0))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    # bubble sort
    def largestNumberUsingBubbleSort(self, nums):
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))

    # selection sort
    def largestNumberUsingSelectionSort(self, nums):
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return str(int("".join(map(str, nums))))

    # insertion sort
    def largestNumberUsingInsertionSort(self, nums):
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos - 1], cur):
                nums[pos] = nums[pos - 1]  # move one-step forward
                pos -= 1
            nums[pos] = cur
        return str(int("".join(map(str, nums))))

    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res

    def mergeSort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = l + (r - l) // 2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(left, right)

    # merge sort
    def largestNumberUsingMergeSort(self, nums):
        nums = self.mergeSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

    def quickSort(self, nums, l, r):
        if l >= r:
            return
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos - 1)
        self.quickSort(nums, pos + 1, r)

    # quick sort, in-place
    def largestNumberUsingQuickSort(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_largestNumber(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[10,2], "210"],
            [[3,30,34,5,9], "9534330"]
        ):
            self.assertEqual(solution, sol.largestNumberUsingBuiltin(nums))
            self.assertEqual(solution, sol.largestNumberUsingBubbleSort(nums))
            self.assertEqual(solution, sol.largestNumberUsingSelectionSort(nums))
            self.assertEqual(solution, sol.largestNumberUsingInsertionSort(nums))
            self.assertEqual(solution, sol.largestNumberUsingMergeSort(nums))
            self.assertEqual(solution, sol.largestNumberUsingQuickSort(nums))


# main
if __name__ == "__main__":
    unittest.main()
