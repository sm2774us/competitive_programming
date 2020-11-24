#
# Time  :
# Space :
#
# @tag : Divide And Conquer ; Binary Search
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 704: Binary Search
#
# Description:
#
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Note:
#
#   1. You may assume that all elements in nums are unique.
#   2. n will be in the range [1, 10000].
#   3. The value of each element in nums will be in the range [-9999, 9999].
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-search/ (LeetCode - Problem 704 - Binary Search)
#         https://practice.geeksforgeeks.org/problems/binary-search/1 (GeeksForGeeks - Binary Search)
# **************************************************************************
#
# References:
# **************************************************************************
# https://en.wikipedia.org/wiki/Binary_search_algorithm
#
from typing import List
import bisect

import unittest


class Solution(object):

    # Solution_1 : Standard Binary Search
    #
    # | O(T): O(lgn) | O(S): O(1) | Rt: 252ms |
    #
    def search_standard_binary_search_solution_1(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

    # Solution_2 : All-Check Binary Search
    #
    # | O(T): O(lgn) | O(S): O(1) | Rt: 260ms |
    #
    def search_all_check_binary_search_solution_2(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Solution_3 : Binary Search using Python built-in - bisect
    #
    # | O(T): O(lgn) | O(S): O(1) |
    #
    def search_using_bisect_python_builtin_solution_3(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_search(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[1, 2, 3, 4, 5], 4, 3],
            [[11, 22, 33, 44, 55], 445, -1],
            [[-1, 0, 3, 5, 9, 12], 9, 4],
            [[-1, 0, 3, 5, 9, 12], 2, -1],
        ):
            self.assertEqual(
                solution, sol.search_standard_binary_search_solution_1(nums, target)
            )
            self.assertEqual(
                solution, sol.search_all_check_binary_search_solution_2(nums, target)
            )
            self.assertEqual(
                solution,
                sol.search_using_bisect_python_builtin_solution_3(nums, target),
            )


# main
if __name__ == "__main__":
    unittest.main()
