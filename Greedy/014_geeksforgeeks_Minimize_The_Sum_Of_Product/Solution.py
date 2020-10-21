#
# Time  : O(N log N)
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
# You are given two arrays, A and B, of equal size N. The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] +…+ A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains three lines. The first line contains an integer N denoting the size of the arrays. In the second line are N space separated values of the array A[], and in the last line are N space separated values of the array B[].
#
# Output:
# For each test case, print the minimum sum.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= A[] <= 1018
#
# Example:
# Input:
# 2
# 3
# 3 1 1
# 6 5 4
# 5
# 6 1 9 5 4
# 3 4 8 2 4
# Output:
# 23
# 80
#
# Explanation:
# For testcase1: 1*6+1*5+3*4 = 6+5+12 = 23 is the minimum sum
# For testcase2: 2*9+3*6+4*5+4*4+8*1 =18+18+20+16+8 = 80 is the minimum sum
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product/0 (GeeksForGeeks - Minimize the heights)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest

# Python program to calculate minimum sum of product
# of two arrays.
class Solution:
    # Returns minimum sum of product of two arrays
    # with permutations allowed
    def getMinValue(self, A: List[int], B: List[int], n: int) -> int:
        # Sort A and B so that minimum and maximum
        # value can easily be fetched.
        A.sort()
        B.sort()

        # Multiplying minimum value of A and maximum
        # value of B
        result = 0
        for i in range(n):
            result += A[i] * B[n - i - 1]

        return result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getMinValue(self) -> None:
        sol = Solution()
        for A, B, solution in (
            [[3, 1, 1], [6, 5, 4], 23],
            [[6, 1, 9, 5, 4], [3, 4, 8, 2, 4], 80],
        ):
            self.assertEqual(solution, sol.getMinValue(A, B, len(A)))


# main
if __name__ == "__main__":
    # # Driver function
    # sol = Solution()
    # A = [3,1,1]
    # B = [6,5,4]
    # print(minValue(A, B, len(A)))
    unittest.main()
