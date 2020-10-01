#
# Time : O(N^3); Space: O(N)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Swapping pairs make sum equal
#
# Description:
#
# Given two arrays of integers A[] and B[] of size N and M, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.
#
# Example 1:
#
# Input: N = 6, M = 4
# A[] = {4, 1, 2, 1, 1, 2}
# B[] = (3, 6, 3, 3)
#
# Output: 1
# Explanation: Sum of elements in A[] = 11
# Sum of elements in B[] = 15, To get same
# sum from both arrays, we can swap following
# values: 1 from A[] and 3 from B[]
#
# Example 2:
#
# Input: N = 4, M = 4
# A[] = {5, 7, 4, 6}
# B[] = {1, 2, 3, 8}
#
# Output: 1
# Explanation: We can swap 6 from array
# A[] and 2 from array B[]
#
# Your Task:
# This is a function problem. You don't need to take any input, as it is already accomplished by the driver code.
# You just need to complete the function findSwapValues() that takes array A, array B, integer N, and integer M
# as parameters and returns 1 if there exists any such pair otherwise returns -1.
#
# Expected Time Complexity: O(MlogM+NlogN).
# Expected Auxiliary Space: O(1).
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1 (GeeksForGeeks - Swapping pairs make sum equal)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
import unittest


class Solution:
    # Returns sum of elements in list
    def getSum(self, X):
        sum = 0
        for i in X:
            sum += i
        return sum

    # Finds value of
    # a - b = (sumA - sumB) / 2
    def getTarget(self, A, B):
        # Calculations of sumd from both lists
        sum1 = self.getSum(A)
        sum2 = self.getSum(B)

        # Because that target must be an integer
        if (sum1 - sum2) % 2 != 0:
            return 0
        return (sum1 - sum2) / 2

    def findSwapValues(self, A, B):
        # Call for sorting the lists
        A.sort()
        B.sort()

        # Note that target can be negative
        target = self.getTarget(A, B)

        # target 0 means, answer is not possible
        if target == 0:
            return False
        i, j = 0, 0
        while i < len(A) and j < len(B):
            diff = A[i] - B[j]
            if diff == target:
                return True
            # Look for a greater value in list A
            elif diff < target:
                i += 1
            # Look for a greater value in list B
            else:
                j += 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_fourSum(self) -> None:
        sol = Solution()
        for A, B, solution in (
            [[4, 1, 2, 1, 1, 2], [3, 6, 3, 3], True],
            [[5, 7, 4, 6], [1, 2, 3, 8], True],
        ):
            self.assertEqual(solution, sol.findSwapValues(A, B))


if __name__ == "__main__":
    unittest.main()
