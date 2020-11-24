#
# Time  :
# Space :
#
# @tag : Divide And Conquer ; Partner Index ; Binary Search
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 540: Single Element in a Sorted Array
#
# Description:
#
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.
#
#
# Example 1:
#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#   * 1 <= nums.length <= 10^5
#   * 0 <= nums[i] <= 10^5
#
# **************************************************************************
# Source: https://leetcode.com/problems/single-element-in-a-sorted-array/ (LeetCode - Problem 540 - Single Element in a Sorted Array)
#         https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1 (GeeksForGeeks - Find the element that appears once in sorted array)
# **************************************************************************
#
# References:
# **************************************************************************
# https://en.wikipedia.org/wiki/Binary_search_algorithm
#
from typing import List

import unittest


class Solution(object):

    # Solution_1 :
    # Simply find the first index whose "partner index" (the index xor 1) holds a different value.
    def singleNonDuplicate_solution_1_using_partner_index(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # partner index like 01 23 45 ... if there is no single element
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            nei = mid + 1 if mid % 2 == 0 else mid - 1
            if nums[mid] == nums[nei]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    # Solution_2 :
    #
    # If every element in the sorted array were to appear exactly twice,
    # they would occur in pairs at indices i, i+1 for all even i.
    #
    # Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.
    #
    # When we insert the unique element into this list, the indices of
    # all the pairs following it will be shifted by one, negating the above relationship.
    #
    # So, for any even index i, we can compare nums[i] to nums[i+1].
    #
    # If they are equal, the unique element must occur somewhere after index i+1
    # If they aren't equal, the unique element must occur somewhere before index i+1
    # Using this knowledge, we can use binary search to find the unique element.
    #
    # We just have to make sure that our pivot index is always even,
    # so we can use mid = 2 * ((lo + hi) // 4) instead of the usual mid = (lo + hi) // 2.
    #
    # Time: O(logn)
    # Space: O(1)
    #
    def singleNonDuplicate_solution_2_binary_search(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_singleNonDuplicate(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[1, 1, 2, 3, 3, 4, 4, 8, 8], 2],
            [[3, 3, 7, 7, 10, 11, 11], 10],
            [[1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65], 4],
        ):
            self.assertEqual(
                solution, sol.singleNonDuplicate_solution_1_using_partner_index(nums)
            )
            self.assertEqual(
                solution, sol.singleNonDuplicate_solution_2_binary_search(nums)
            )


# main
if __name__ == "__main__":
    unittest.main()
