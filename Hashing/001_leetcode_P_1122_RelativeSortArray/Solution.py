#
# Time : O(N); Space: O(1)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 1122: Relative Sort Array
#
# Description:
#
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
#
#
#
# Example 1:
#
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#
#
# Constraints:
#
#   * arr1.length, arr2.length <= 1000
#   * 0 <= arr1[i], arr2[i] <= 1000
#   * Each arr2[i] is distinct.
#   * Each arr2[i] is in arr1.
#
# **************************************************************************
# Source: https://leetcode.com/problems/relative-sort-array/ (Leetcode - Problem 1122 - Relative Sort Array)
#         https://practice.geeksforgeeks.org/problems/relative-sorting/0 (GeeksForGeeks - Relative Sorting)
#
#
# Similar to counting sort, in which case worst case time complexity would be O(N + k),
# where N is max(len(arr1), len(arr2)) and k is the range of the values in arr1 which would be [0, 1000].
#
from typing import List

import unittest


class Solution:
    # [No sort()] Python3 O(N + 1001) ~= O(N) Solution
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001
        ans = []
        for x in arr1:
            counts[x] += 1
        for x in arr2:
            ans.extend([x] * counts[x])
            counts[x] = 0
        for x, count in enumerate(counts):
            ans.extend([x] * count)
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_relativeSortArray(self) -> None:
        sol = Solution()
        for arr1, arr2, solution in (
            [
                [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                [2, 1, 4, 3, 9, 6],
                [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
            ],
            [[1, 2, 3, 4], [2, 3], [2, 3, 1, 4]],
        ):
            self.assertEqual(solution, sol.relativeSortArray(arr1, arr2))


if __name__ == "__main__":
    unittest.main()
