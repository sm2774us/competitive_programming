#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Minimize the heights
#
# Description:
#
# Given an array arr[] denoting heights of N towers and a positive integer K, modify the heights of each tower
# either by increasing or decreasing them by K only once.
# Find out the minimum difference of the heights of shortest and longest modified towers.
#
# Example 1:
#
# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation: The array can be modified as
# {3, 3, 6, 8}. The difference between
# the largest and the smallest is 8-3 = 5.
#
# Example 2:
#
# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output: 11
# Explanation: The array can be modified as
# {6 12 9 13 17}. The difference between
# the largest and the smallest is 17-6 = 11.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.
#
#
# Expected Time Complexity: O(N*logN)
# Expected Auxiliary Space: O(1)
#
# Constraints
# 1 <= K <= 104
# 1 <= N <= 105
# 1 <= Arr[i] <= 105
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1 (GeeksForGeeks - Minimize the heights)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest

# Python 3 program to find the minimum
# possible difference between maximum
# and minimum elements when we have to
# add / subtract every number by k
class Solution:
    # Modifies the array by subtracting /
    # adding k to every element such that
    # the difference between maximum and
    # minimum is minimized
    def getMinDiff(self, arr: List[int], n: int, k: int) -> int:

        if n == 1:
            return 0

        # Sort all elements
        arr.sort()

        # Initialize result
        ans = arr[n - 1] - arr[0]

        # Handle corner elements
        small = arr[0] + k
        big = arr[n - 1] - k

        if small > big:
            small, big = big, small

        # Traverse middle elements
        for i in range(1, n - 1):

            subtract = arr[i] - k
            add = arr[i] + k

            # If both subtraction and addition
            # do not change diff
            if subtract >= small or add <= big:
                continue

            # Either subtraction causes a smaller
            # number or addition causes a greater
            # number. Update small or big using
            # greedy approach (If big - subtract
            # causes smaller diff, update small
            # Else update big)
            if big - subtract <= add - small:
                small = subtract
            else:
                big = add

        return min(ans, big - small)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getMinDiff(self) -> None:
        sol = Solution()
        for a, k, solution in ([[1, 5, 8, 10], 2, 5], [[3, 9, 12, 16, 20], 3, 11]):
            self.assertEqual(solution, sol.getMinDiff(a, len(a), k))


# main
if __name__ == "__main__":
    # # Driver function
    # sol = Solution()
    # arr = [4, 6]
    # k = 10
    # print("Maximum difference is {}".format(sol.getMinDiff(arr, len(arr), k)))
    unittest.main()
