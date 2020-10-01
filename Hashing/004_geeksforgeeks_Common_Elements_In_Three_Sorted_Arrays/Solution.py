#
# Time : O(n1 + n2 + n3); Space: O(n1 + n2 + n3)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Common elements
#
# Description:
#
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
#
# Example 1:
#
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.
#
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function commonElements()
# which take the 3 arrays A[], B[], C[] and their respective sizes n1, n2 and n3 as inputs and returns an array
# containing the common element present in all the 3 arrays in sorted order.
# If there are no such elements return an empty array. In this case the output will be printed as -1.
#
#
# Expected Time Complexity: O(n1 + n2 + n3)
# Expected Auxiliary Space: O(n1 + n2 + n3)
#
#
# Constraints:
# 1 <= n1, n2, n3 <= 10^5
# The array elements can be both positive or negative integers.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/common-elements1132/1 (GeeksForGeeks - Common Elements)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
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
    # Python function to print common elements in three sorted arrays
    def commonElements(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        n1, n2, n3 = len(A), len(B), len(C)
        # Initialize starting indexes for ar1[], ar2[] and ar3[]
        i, j, k = 0, 0, 0
        ans = []
        # Iterate through three arrays while all arrays have elements
        while (i < n1 and j < n2 and k < n3):

            # If x = y and y = z, print any of them and move ahead
            # in all arrays
            if (A[i] == B[j] and B[j] == C[k]):
                ans.append(A[i])
                i += 1
                j += 1
                k += 1

            # x < y
            elif A[i] < B[j]:
                i += 1

            # y < z
            elif B[j] < C[k]:
                j += 1

            # We reach here when x > y and z < y, i.e., z is smallest
            else:
                k += 1

        return ans

    def commonElementsUsingSet(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        # Converting the arrays into sets
        s1 = set(A)
        s2 = set(B)
        s3 = set(C)

        # Calculates intersection of
        # sets on s1 and s2
        set1 = s1.intersection(s2)

        # Calculates intersection of sets
        # on set1 and s3
        result_set = set1.intersection(s3)

        # Converts resulting set to list and return
        return(list(result_set))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_commonElements(self) -> None:
        sol = Solution()
        self.assertEqual([20, 80], sorted(sol.commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120])))
        self.assertEqual([20, 80], sorted(sol.commonElementsUsingSet([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120])))


if __name__ == "__main__":
    unittest.main()
