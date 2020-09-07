#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 54. Spiral Matrix
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# **************************************************************************
# Source: https://leetcode.com/problems/spiral-matrix/ (Leetcode - Problem 54 - Spiral Matrix)
#         https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix/0 (GeeksForGeeks - Spirally traversing a matrix)
#
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        row_start = 0
        row_end = len(matrix) - 1

        col_start = 0
        col_end = len(matrix[0]) - 1

        res = []
        while row_start <= row_end and col_start <= col_end:

            # right
            for j in range(col_start, col_end + 1):
                res.append(matrix[row_start][j])
            row_start += 1

            # down
            for i in range(row_start, row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1

            # left
            if row_start <= row_end:
                for j in range(col_end, col_start - 1, -1):
                    res.append(matrix[row_end][j])

                row_end -= 1

            # up
            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1

        return res


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_spiralOrder(self):
        s = Solution()
        for matrix, solution in (
            [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]],
            [
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            ],
        ):
            self.assertEqual(s.spiralOrder(matrix), solution)


if __name__ == "__main__":
    unittest.main()
