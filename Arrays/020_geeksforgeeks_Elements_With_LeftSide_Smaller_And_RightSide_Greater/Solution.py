#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Element with left side smaller and right side greater
#
# Given an unsorted array of size N. Find the first element in array
# such that all of its left elements are smaller and all right elements to it are greater than it.
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: 7
# Explanation: Elements on left of 5 are smaller than 5 and on right of it are greater than 5.
#
# Example 2:
#
# Input: [11,9,12]
# Output: -1
# Explanation: There is no such element in the array so return -1.
#
# **************************************************************************
# Source:
#   https://practice.geeksforgeeks.org/problems/unsorted-array/0 (GeeksForGeeks - Element with left side smaller and right side greater)
# Solution Hint:
#   https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
#   https://practice.geeksforgeeks.org/viewSol.php?subId=2ee30dad02eb8569e1d555abeb040fe4&pid=1977&user=sm2774us
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
#
# An Efficient Solution can solve this problem in O(n) time using O(n) extra space. Below is detailed solution.
#
# 1) Create two arrays leftMax[] and rightMin[].
# 2) Traverse input array from left to right and fill leftMax[] such that leftMax[i] contains
#    maximum element from 0 to i-1 in input array.
# 3) Traverse input array from right to left and fill rightMin[] such that rightMin[i] contains
#    minimum element from to n-1 to i+1 in input array.
# 4) Traverse input array. For every element arr[i],
#    check if arr[i] is greater than leftMax[i] and smaller than rightMin[i]. If yes, return i.
#
# A Further Optimization to the above approach is to use only one extra array and traverse input array only twice.
# The first traversal is the same as above and fills leftMax[]. Next traversal traverses from the right
# and keeps track of the minimum. The second traversal also finds the required element.
#
# Below image is a dry run of the above approach:
#
# Step 1: Find leftMax array
#         +---------+---+---+---+---+---+---+---+---+
#         | INT_MIN | 5 | 5 | 5 | 5 | 6 | 8 | 10| 10|
#         +---------+---+---+---+---+---+---+---+---+
#
# Step 2: Initialize rightMin
#         rightMin = INT_MAX
#
# Step 3:        +---+---+---+---+---+---+---+---+---+
#           arr  | 5 | 1 | 4 | 3 | 6 | 8 | 10| 7 | 9 |
#                +---+---+---+---+---+---+---+---+---+
#                                                  ^
#                                                  |
#                Here, leftMax[i] is not less than arr[i] update rightMin and decrement i
#                rightMin = 9
#
# Step 4:        +---+---+---+---+---+---+---+---+---+
#           arr  | 5 | 1 | 4 | 3 | 6 | 8 | 10| 7 | 9 |
#                +---+---+---+---+---+---+---+---+---+
#                                              ^
#                                              |
#                Here, leftMax[i] is not less than arr[i] update rightMin and decrement i
#                rightMin = 7
#
# Step 5:        +---+---+---+---+---+---+---+---+---+
#           arr  | 5 | 1 | 4 | 3 | 6 | 8 | 10| 7 | 9 |
#                +---+---+---+---+---+---+---+---+---+
#                                          ^
#                                          |
#               Here, leftMax[i] < arr[i], but rightMin < arr[i] update rightMin and decrement i
#               rightMin = 7
#
# Step 6:        +---+---+---+---+---+---+---+---+---+
#           arr  | 5 | 1 | 4 | 3 | 6 | 8 | 10| 7 | 9 |
#                +---+---+---+---+---+---+---+---+---+
#                                      ^
#                                      |
#                Here, leftMax[i] < arr[i], but rightMin < arr[i] update rightMin and decrement i
#                rightMin = 7
#
# Step 7:        +---+---+---+---+---+---+---+---+---+
#           arr  | 5 | 1 | 4 | 3 | 6 | 8 | 10| 7 | 9 |
#                +---+---+---+---+---+---+---+---+---+
#                                  ^
#                                  |
#               Here, leftMax[i] < arr[i], and rightMin > arr[i]
#               Required index found. Return i
#
from typing import List

import unittest

class Solution:
    def findElement(self, arr: List[int]) -> int:
        n = len(arr)

        for i in range(1,n):
            big = arr[0]
            f = 0
            for i in range(1, n - 1):
                if arr[i] >= big:
                    big = arr[i]
                    if arr[i] <= min(arr[i + 1:]):
                        return arr[i]
                        f = 1
                        break
            if f == 0:
                return -1

        # # leftMax[i] stores maximum of arr[0..i-1]
        # leftMax = [None] * n
        # leftMax[0] = float('-inf')
        #
        # # Fill leftMax[]1..n-1]
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i - 1], arr[i - 1])
        #
        # # Initialize minimum from right
        # rightMin = float('inf')
        #
        # # Traverse array from right
        # for i in range(n - 1, -1, -1):
        # #for i in range(0, n, 1):
        #     # Check if we found a required element
        #     if leftMax[i] < arr[i] and rightMin > arr[i]:
        #         return arr[i]
        #
        #     # Update right minimum
        #     rightMin = min(rightMin, arr[i])
        #
        # # If there was no element matching criteria
        # return -1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findElement(self) -> None:
        s = Solution()
        for arr, solution in (
                [[4, 2, 5, 7], 5],
                [[11, 9, 12], -1],
                [[4, 3, 2, 7, 8, 9], 7]
        ):
            self.assertEqual(solution, s.findElement(arr),
                             "Should return first element in array such that all of its left elements are smaller and all right elements to it are greater than it")

if __name__ == '__main__':
    unittest.main()