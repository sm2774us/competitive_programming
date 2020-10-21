#
# Time : O(n log n) time if input activities may not be sorted; otherwise O(n)
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Activity Selection
#
# Description:
#
# Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
#
# Note : The start time and end time of two activities may coincide.
#
# Input:
# The first line contains T denoting the number of testcases. Then follows description of testcases. First line is N number of activities then second line contains N numbers which are starting time of activies.Third line contains N finishing time of activities.
#
# Output:
# For each test case, output a single number denoting maximum activites which can be performed in new line.
#
# Constraints:
# 1<=T<=50
# 1<=N<=1000
# 1<=A[i]<=100
#
# Example:
# Input:
# 2
# 6
# 1 3 2 5 8 5
# 2 4 6 7 9 9
# 4
# 1 3 2 5
# 2 4 3 6
#
# Output:
# 4
# 4
#
# Explanation:
# Test Case 1: The following activities can be performed (in the same order):
# (1, 2)
# (3, 4)
# (5, 7)
# (8, 9)
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/activity-selection/0 (GeeksForGeeks - Activity Selection)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List

import unittest


class Solution:
    """The following implementation assumes that the activities
    are already sorted according to their finish time"""

    """Prints a maximum set of activities that can be done by a 
    single person, one at a time"""
    # a[]--> An array that contains start time of all activities
    # b[] --> An array that contains finish time of all activities
    def getMaxActivities(self, a: List[int], b: List[int]) -> int:
        pab = zip(a, b)
        c = 0
        curr = 0
        for x in sorted(pab, key=lambda x: x[1]):
            if curr <= x[0]:
                c += 1
                curr = x[1]
        # print(c)
        return c


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getMaxActivities(self) -> None:
        sol = Solution()
        a = [1, 3, 2, 5, 8, 5]
        b = [2, 4, 6, 7, 9, 9]
        self.assertEqual(4, sol.getMaxActivities(a, b))
        a = [1, 3, 2, 5]
        b = [2, 4, 3, 6]
        self.assertEqual(4, sol.getMaxActivities(a, b))


# main
if __name__ == "__main__":
    # sol = Solution
    # # Driver program to test above function
    # a = [1, 3, 2, 5, 8, 5]
    # b = [2, 4, 6, 7, 9, 9]
    # sol.getMaxActivities(a, b)
    unittest.main()
