#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Chocolate Distribution Problem
# **************************************************************************
# Given an array A of positive integers of size N, where each value represents number of chocolates in a packet.
# Each packet can have variable number of chocolates.
# There are M students, the task is to distribute chocolate packets such that :
#
# 1. Each student gets one packet.
# 2. The difference between the number of chocolates given to the students having packet with maximum chocolates
#    and student having packet with minimum chocolates is minimum.
#
# Example 1:
#
# Input:
#   A = [3, 4, 1, 9, 56, 7, 9, 12] ( each value represents the # of chocolates in a packet )
#   M = 5 ( # of students )
# Output: 6
#
# Explanation:
# The minimum difference between maximum chocolates and minimum chocolates is 9-3=6
#
# Example 2:
#
# Input:
#   A = [7, 3, 2, 4, 9, 12, 56] ( each value represents the # of chocolates in a packet )
#   M = 3 ( # of students )
# Output: 2
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0 ( Chocolate Distribution Problem )
#
# Solution Hint: https://tutorialspoint.dev/algorithm/sorting-algorithms/chocolate-distribution-problem
#                https://www.planetmilav.com/pages/joyOfComutingUsingPython/joyOfComutingUsingPython.pdf
#
from typing import List
import sys

import unittest

class Solution:

    # arr[0..n-1] represents sizes of packets
    # m is number of students.
    # Returns minimum difference between maximum
    # and minimum values of distribution.
    def findMinDiff(self, arr: List[int], m: int) -> int:
        n = len(arr)
        # if there are no chocolates or number
        # of students is 0
        if (m == 0 or n == 0):
            return 0

        # Sort the given packets
        arr.sort()

        # Number of students cannot be more than
        # number of packets
        if (n < m):
            return -1

        # Largest number of chocolates
        min_diff = sys.maxsize

        # Find the subarray of size m such that
        # difference between last (maximum in case
        # of sorted) and first (minimum in case of
        # sorted) elements of subarray is minimum.
        first = 0
        last = 0
        i = 0
        while (i + m - 1 < n):

            diff = arr[i + m - 1] - arr[i]
            if (diff < min_diff):
                min_diff = diff
                first = i
                last = i + m - 1

            i += 1

        return (arr[last] - arr[first])

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMinDiff(self) -> None:
        s = Solution()
        for arr, m, solution in (
                [[3, 4, 1, 9, 56, 7, 9, 12], 5, 6],
                [[7, 3, 2, 4, 9, 12, 56], 3, 2]
        ):
            self.assertEqual(solution, s.findMinDiff(arr, m), "Should return the minimum difference between maximum chocolates and minimum chocolates")

if __name__ == '__main__':
    unittest.main()