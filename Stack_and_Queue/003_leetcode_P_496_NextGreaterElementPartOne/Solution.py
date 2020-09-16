#
# Time : O(N); Space: O(N)
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 496: Next Greater Element I
#
# Description:
#
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
#
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
#
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
# Note:
#   All elements in nums1 and nums2 are unique.
#   The length of both nums1 and nums2 would not exceed 1000.
#
# **************************************************************************
# Source: https://leetcode.com/problems/next-greater-element-i/ (Leetcode - Problem 496 - Next Greater Element I)
#
from typing import List
import unittest


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater, stack = {}, []
        for n in nums2:
            while stack and n > stack[-1]:
                greater[stack.pop()] = n
            stack.append(n)
        return [greater[n] if n in greater else -1 for n in nums1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_nextGreaterElement(self) -> None:
        s = Solution()
        for nums1, nums2, solution in (
            [[4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]],
            [[2, 4], [1, 2, 3, 4], [3, -1]],
        ):
            self.assertEqual(
                solution,
                s.nextGreaterElement(nums1, nums2),
                "Should return the next Greater Number of a number x in nums1 is the first greater number to its right in nums2 otherwise -1",
            )


if __name__ == "__main__":
    unittest.main()
