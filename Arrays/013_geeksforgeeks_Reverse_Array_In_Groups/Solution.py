#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Reverse array in groups
# **************************************************************************
# Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
#
# Note: O(1) extra space is allowed. Also, try to modify the input array as required.
#
# Example:
#
# Given input            => N = [10, 20, 30, 40, 50, 60] & k = 2
#       output should be => [20, 10, 40, 30, 60, 50]
#
# **************************************************************************
#
# Approach:
# **************************************************************************
# Consider every sub-array of size k starting from the beginning of the array and reverse it.
# We need to handle some special cases. If k is not multiple of n where n is the size of the array,
# for the last group we will have less than k elements left, we need to reverse all remaining elements.
# If k = 1, the array should remain unchanged. If k >= n, we reverse all elements present in the array.
#
#           arr = [ 1, 2, 3, 4, 5, 6 ]
#             k = 3
#
#                   i
#                   |
#                  \ /
#                   *
# Step 1:   arr = [ 1, 2, 3, 4, 5, 6 ]
#           Left = 0, Right = 2
#           while(true)
#               |
#               +---> swaps the array from [ 0, 2 ]
#           arr = [ 3, 2, 1, 4, 5, 6 ]
#
#                            i
#                            |
#                           \ /
#                            *
# Step 2:   arr = [ 1, 2, 3, 4, 5, 6 ]
#           Left = 3, Right = 5
#           while(true)
#               |
#               +---> swaps the array from [ 3, 5 ]
#           arr = [ 3, 2, 1, 6, 5, 4 ]
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0 ( Reverse array in groups )
#
# Solution Hint: https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/
#
from typing import List

import unittest


class Solution:
    def arrayreverse(self, arr: List[int], k: int) -> None:
        n = len(arr)
        i = 0

        while i < n:

            left = i

            # To handle case when k is not
            # multiple of n
            right = min(i + k - 1, n - 1)

            # Reverse the sub-array [left, right]
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            i += k


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_arrayreverse(self) -> None:
        s = Solution()
        arr = [11, 22, 33, 44, 55, 66]
        k = 2
        s.arrayreverse(arr, k)
        self.assertEqual(
            [22, 11, 44, 33, 66, 55],
            arr,
            "Should reverse every sub-array of k group elements in the array N",
        )
        arr = [1, 2, 3, 4, 5]
        k = 3
        s.arrayreverse(arr, k)
        self.assertEqual(
            [3, 2, 1, 5, 4],
            arr,
            "Should reverse every sub-array of k group elements in the array N",
        )
        arr = [10, 20, 30, 40, 50, 60]
        k = 2
        s.arrayreverse(arr, k)
        self.assertEqual(
            [20, 10, 40, 30, 60, 50],
            arr,
            "Should reverse every sub-array of k group elements in the array N",
        )


if __name__ == "__main__":
    unittest.main()
