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
    def zig_zag(self, arr: List[int]) -> None:
        n = len(arr)
        result = [0 for x in range(n)]
        f = 0
        for i in range(1, n):
            j = i - 1
            if f == 0:
                f = 1
                if arr[j] > arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
            else:
                f = 0
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_zig_zag(self) -> None:
        s = Solution()
        arr = [4, 3, 7, 8, 6, 2, 1]
        s.zig_zag(arr)
        self.assertEqual([3, 7, 4, 8, 2, 6, 1], arr, "Should rearrange the elements of array in zig-zag fashion")
        arr = [1, 4, 3, 2]
        s.zig_zag(arr)
        self.assertEqual([1, 4, 2, 3], arr, "Should rearrange the elements of array in zig-zag fashion")

if __name__ == '__main__':
    unittest.main()