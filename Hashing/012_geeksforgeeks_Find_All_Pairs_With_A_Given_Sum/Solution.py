#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Find all pairs with a given sum
#
# Description:
#
# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.
#
# Output:
# For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N, M, X <= 106
# -106 <= A, B <= 106
#
# Example:
# Input:
# 2
# 5 5 9
# 1 2 4 5 7
# 5 6 3 4 8
# 2 2 3
# 0 2
# 1 3
# Output:
# 1 8, 4 5, 5 4
# 0 3, 2 1
#
# Explanation:
# Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0 (GeeksForGeeks - Find all pairs with a given sum)
#
#
from typing import List
from collections import Counter

import unittest


class Solution:
    def sum_pairs(
        self, array1: List[int], array2: List[int], req_sum: int
    ) -> List[int]:
        sum_lists = []

        # hash array1 for later searching
        hash1 = {x: x for x in array1}

        for y in array2:
            # Using Pythonic - EAFP ( "it’s easier to ask for forgiveness than permission") - https://docs.python.org/3.5/glossary.html#term-eafp
            #                  rather than LBYL ( "look before you leap" )
            try:
                # if hash1[req_sum-y] exists
                x = hash1[req_sum - y]
                sum_lists.append([x, y])
            except KeyError:
                # the other number for pairing with y not found
                continue

        return sum_lists

    def checkEqual(self, L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sum_pairs(self) -> None:
        sol = Solution()
        for a, b, req_sum, solution in (
            [[1, 2, 4, 5, 7], [5, 6, 3, 4, 8], 9, [[1, 8], [4, 5], [5, 4]]],
            [[0, 2], [1, 3], 3, [[0, 3], [2, 1]]],
        ):
            self.assertEqual(
                sol.checkEqual(solution, sol.sum_pairs(a, b, req_sum)), True
            )


if __name__ == "__main__":
    unittest.main()
