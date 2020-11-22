#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Maximum sum increasing subsequence
#
# Description:
#
# Given an array arr of N positive integers, the task is to find the maximum sum increasing subsequence of the given array.
#
# Example 1:
#
# Input: N = 5, arr[] = {1, 101, 2, 3, 100}
# Output: 106
# Explanation:The maximum sum of a
# increasing sequence is obtained from
# {1, 2, 3, 100}
# Example 2:
#
# Input: N = 3, arr[] = {1, 2, 3}
# Output: 6
# Explanation:The maximum sum of a
# increasing sequence is obtained from
# {1, 2, 3}
# Your Task:
# You don't need to read input or print anything. Complete the function maxSumIS() which takes N and array arr as input parameters and returns the maximum value.
#
# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(N)
#
# Constraints:
# 1 ≤ N ≤ 103
# 1 ≤ arr[i] ≤ 105
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1 (GeeksForGeeks - Maximum sum increasing subsequence)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# Reference
# **************************************************************************
# https://www.techiedelight.com/increasing-subsequence-with-maximum-sum/
#
from typing import List
import math

import unittest


class Solution(object):
    # Solution 1: Recursive Solution to find maximum sum of an increasing sub-sequence
    #
    # TC: O(2^N) Exponential
    # SC: O(1)
    #
    # Function to find maximum sum of increasing subsequence
    def maxSumISRecursive(
        self, A: List[int], n: int, i: int = 0, prev: float = math.inf, sum: int = 0
    ) -> int:
        # Base case: nothing is remaining
        if i == n:
            return sum

        # case 1: exclude the current element and process the
        # remaining elements
        excl = self.maxSumISRecursive(A, n, i + 1, prev, sum)

        # case 2: include the current element if it is greater
        # than previous element
        incl = sum
        if A[i] > prev:
            incl = self.maxSumISRecursive(A, n, i + 1, A[i], sum + A[i])

        # return maximum of above two choices
        return max(incl, excl)

    # Solution 2: Iterative Solution based on Dynamic Programming
    #             to find maximum sum of an increasing sub-sequence
    #
    # TC: O(N^2)
    # SC: O(N)
    #
    # Function to find maximum sum of increasing subsequence
    def maxSumISDynamicProgramming(self, A: List[int], n: int) -> int:
        # list to store sub-problem solution. sum[i] stores the maximum
        # sum of the increasing sub-sequence that ends with A[i]
        sum = [0] * n

        # base case
        sum[0] = A[0]

        # start from second element in the list
        for i in range(1, n):

            # do for each element in sublist A[0..i-1]
            for j in range(i):

                # find increasing sub-sequence with maximum sum that ends with
                # A[j] where A[j] is less than the current element A[i]
                if sum[i] < sum[j] and A[i] > A[j]:
                    sum[i] = sum[j]

            # include A[i] in MSIS
            sum[i] += A[i]

        # find increasing sub-sequence with maximum sum
        return max(sum)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSumIS(self) -> None:
        sol = Solution()
        for A, solution in ([[1, 101, 2, 3, 100], 106], [[1, 2, 3], 6]):
            # self.assertEqual(solution, sol.maxSumISRecursive(A, len(A)))
            # self.assertEqual(solution, sol.maxSumISRecursive(A, len(A), 0, math.inf, 0))
            self.assertEqual(solution, sol.maxSumISDynamicProgramming(A, len(A)))


# main
if __name__ == "__main__":
    unittest.main()
