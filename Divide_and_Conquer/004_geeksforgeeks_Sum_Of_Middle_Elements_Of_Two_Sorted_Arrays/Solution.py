#
# Time  :
# Space :
#
# @tag : Divide And Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Sum of Middle Elements of two sorted arrays
#
# Description:
#
# Given 2 sorted arrays A and B of size N each. Print sum of middle elements of the array obtained after merging the given arrays.
#
# Input:
# The first line contains T denoting the number of testcases. Then follows description of testcases.
# Each case begins with a single positive integer N denoting the size of array. The second line contains the N space separated positive integers denoting the elements of array A. The third line contains N space separated positive integers denoting the elements of array B.
#
# Output:
# For each testcase, print the sum of middle elements of two sorted arrays. The number of the elements in the merged array are even so there will be 2 numbers in the center n/2 and n/2 +1. You have to print their sum.
#
# Constraints:
# 1 <= T <= 50
# 1 <= N <= 103
# 1 <= A[i] <= 106
# 1 <= B[i] <= 106
#
# Example:
# Input :
# 1
# 5
# 1 2 4 6 10
# 4 5 6 9 12
#
# Output :
# 11
#
# Explanation:
# Testcase 1: After merging two arrays, sum of middle elements is 11 (5 + 6).
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays/0 (GeeksForGeeks - Sum of Middle Elements of two sorted arrays)
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):
    def sum_of_middle_elements(self, lst1: List[int], lst2: List[int]) -> int:
        """
        :type lst1: List[int]
        :type lst2: List[int]
        :rtype: int
        """
        lst1 = lst1 + lst2
        lst1.sort()
        k = len(lst1)
        k1 = k // 2
        k = (k // 2) - 1
        s = lst1[k1] + lst1[k]
        return s


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sum_of_middle_elements(self) -> None:
        sol = Solution()
        lst1 = [1, 2, 4, 6, 10]
        lst2 = [4, 5, 6, 9, 12]
        self.assertEqual(11, sol.sum_of_middle_elements(lst1, lst2))


# main
if __name__ == "__main__":
    unittest.main()
