#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Array Subset of another array
#
# Description:
#
# Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n. Task is to check whether arr2[] is a subset of arr1[] or not. Both the arrays can be both unsorted or sorted. It may be assumed that elements in both array are distinct.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an two integers m and n denoting the size of arr1 and arr2 respectively. The following two lines contains the space separated elements of arr1 and arr2 respectively.
#
# Output:
# Print "Yes"(without quotes) if arr2 is subset of arr1.
# Print "No"(without quotes) if arr2 is not subset of arr1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= m,n <= 105
# 1 <= arr1[i], arr2[j] <= 105
#
# Example:
# Input:
# 3
# 6 4
# 11 1 13 21 3 7
# 11 3 7 1
# 6 3
# 1 2 3 4 5 6
# 1 2 4
# 5 3
# 10 5 2 23 19
# 19 5 3
#
# Output:
# Yes
# Yes
# No
#
# Explanation:
# Testcase 1: (11, 3, 7, 1) is a subset of first array.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0 (GeeksForGeeks - Array Subset of another array)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List
from collections import Counter

import unittest


class Solution:
    def containedInFirst(self, a: List[int], b: List[int]) -> bool:
        a_count = Counter(a)
        b_count = Counter(b)
        for key in b_count:
            # if a_count.__contains__(key) == False:
            # or more pythonic
            # [ Time Complexity for 'in' statement => { lists - Average: O(n) ; set/dict - Average: O(1), Worst: O(n) } ]
            if not key in a_count:
                return False
            if b_count[key] > a_count[key]:
                return False
        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_containedInFirst(self) -> None:
        sol = Solution()
        for a, b, solution in (
            [[11, 1, 13, 21, 3, 7], [11, 3, 7, 1], True],
            [[1, 2, 3, 4, 5, 6], [1, 2, 4], True],
            [[10, 5, 2, 23, 19], [19, 5, 3], False],
        ):
            self.assertEqual(solution, sol.containedInFirst(a, b))


if __name__ == "__main__":
    unittest.main()
