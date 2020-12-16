#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Maximum Index
#
# Given an array A[] of N positive integers.
# The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].
#
# Example 1:
#
# Input:
# N = 2
# A[] = {1,10}
# Output: 1
# Explanation: A[0]<=A[1] so (j-i)
# is 1-0 = 1.
# Example 2:
#
# Input:
# N = 9
# A[] = {34,8,10,3,2,80,30,33,1}
# Output: 6
# Explanation: In the given array
# A[1] < A[7] satisfying the required
# condition(A[i] <= A[j]) thus giving
# the maximum difference of j - i
# which is 6(7-1).
#
#
# Your Task:
# The task is to complete the function maxIndexDiff() which finds and returns maximum index difference. Printing the output will be handled by driver code.
#
# Constraints:
# 1 ≤ N ≤ 107
# 0 ≤ A[i] ≤ 1018
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).
#
# **************************************************************************
# Source:
#   https://practice.geeksforgeeks.org/problems/maximum-index-1587115620/1 (GeeksForGeeks - Maximum Index)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# Reference:
#   https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
# **************************************************************************
#
from typing import List

import unittest


class Solution:

    # Solution 1 - Brute Force Algorithm
    #
    # For a given array arr[], returns
    # the maximum j – i such that
    # arr[j] > arr[i]
    #
    # TC: O(N^2)
    #
    def maxIndexDiff_solution_1(self, arr: List[int], n: int) -> int:
        maxDiff = -1
        for i in range(0, n):
            j = n - 1
            while j > i:
                if arr[j] > arr[i] and maxDiff < (j - i):
                    maxDiff = j - i
                j -= 1

        return maxDiff

    # Solution 2 - Enhanced Brute Force Algorithm
    #
    # For a given array arr,
    # calculates the maximum j – i
    # such that arr[j] > arr[i]
    #
    # TC: O(N * log(N))
    # SC: O(N)
    #
    def maxIndexDiff_solution_2(self, arr: List[int], n: int) -> int:
        maxFromEnd = [-38749432] * (n + 1)

        # Create an array maxfromEnd
        for i in range(n - 1, 0, -1):
            maxFromEnd[i] = max(maxFromEnd[i + 1], arr[i])

        maxDiff = 0
        for i in range(0, n):
            low = i + 1
            high = n - 1
            ans = i

            while low <= high:
                mid = int((low + high) / 2)

                if arr[i] <= maxFromEnd[mid]:

                    # We store this as current
                    # answer and look for further
                    # larger number to the right side
                    ans = max(ans, mid)
                    low = mid + 1
                else:
                    high = mid - 1

            # Keeping a track of the
            # maximum difference in indices
            maxDiff = max(maxDiff, ans - i)

        return maxDiff

    # Solution 3 - Most Efficient Solution
    #
    # For a given array arr[],
    # returns the maximum j - i
    # such that arr[j] > arr[i]
    # TC: O(N)
    # SC: O(N)
    #
    def maxIndexDiff_solution_3(self, arr: List[int], n: int) -> int:
        # Construct leftMinArr[] such that
        # leftMinArr[i] stores the minimum
        # value from (arr[0], arr[1], ... arr[i])
        leftMinArr = [0 for i in range(n)]
        leftMinArr[0] = arr[0]
        for i in range(1, n):
            leftMinArr[i] = min(arr[i], leftMinArr[i - 1])

        # Construct rightMaxArr[] such that
        # rightMaxArr[j] stores the maximum
        # value from (arr[j], arr[j + 1], ... arr[n-1])
        rightMaxArr = [0 for i in range(n)]
        rightMaxArr[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            rightMaxArr[i] = max(arr[i], rightMaxArr[i + 1])
        i, j, maxDiff = 0, 0, 0

        # Traverse both arrays from left
        # to right to find optimum j - i
        # This process is similar to merge() of MergeSort
        while i < len(leftMinArr) and j < len(rightMaxArr):
            if leftMinArr[i] <= rightMaxArr[j]:
                maxDiff = max(maxDiff, j - i)
                j += 1
            else:
                i += 1
        return maxDiff


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxIndexDiff(self) -> None:
        s = Solution()
        for arr, solution in ([[1, 10], 1], [[34, 8, 10, 3, 2, 80, 30, 33, 1], 6]):
            self.assertEqual(
                solution,
                s.maxIndexDiff_solution_1(arr, len(arr)),
                "Should find the maximum index (j-1) subject to the constraint of A[i] <= A[j] in the given array",
            )
            self.assertEqual(
                solution,
                s.maxIndexDiff_solution_2(arr, len(arr)),
                "Should find the maximum index (j-1) subject to the constraint of A[i] <= A[j] in the given array",
            )
            self.assertEqual(
                solution,
                s.maxIndexDiff_solution_3(arr, len(arr)),
                "Should find the maximum index (j-1) subject to the constraint of A[i] <= A[j] in the given array",
            )


if __name__ == "__main__":
    unittest.main()
