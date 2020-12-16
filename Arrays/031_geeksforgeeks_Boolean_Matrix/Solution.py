#
# Time : O(M*N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks - Boolean Matrix
#
# Description:
#
# Given a boolean matrix of size RxC where each cell contains either 0 or 1,
# modify it such that if a matrix cell matrix[i][j] is 1 then all the cells
# in its ith row and jth column will become 1.
#
# Example 1:
#
# Input:
# R = 2, C = 2
# matrix[][] = {{1, 0},
#               {0, 0}}
# Output:
# 1 1
# 1 0
# Explanation:
# Only cell that has 1 is at (0,0) so all
# cells in row 0 are modified to 1 and all
# cells in column 0 are modified to 1.
#
# Example 2:
#
# Input:
# R = 4, C = 3
# matrix[][] = {{ 1, 0, 0},
#               { 1, 0, 0},
#               { 1, 0, 0},
#               { 0, 0, 0}}
# Output:
# 1 1 1
# 1 1 1
# 1 1 1
# 1 0 0
# Explanation:
# The position of cells that have 1 in
# the original matrix are (0,0), (1,0)
# and (2,0). Therefore, all cells in row
# 0,1,2 are and column 0 are modified to 1.
#
# Your Task:
# You dont need to read input or print anything. Complete the function booleanMatrix() that takes the matrix as input parameter and modifies it in-place.
#
#
# Expected Time Complexity: O(R * C)
# Expected Auxiliary Space: O(R + C)
#
#
# Constraints:
# 1 ≤ R, C ≤ 1000
# 0 ≤ matrix[i][j] ≤ 1
#
# **************************************************************************
# Source:
#   https://practice.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/1 (GeeksForGeeks - Boolean Matrix)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest


class Solution(object):

    # Solution 1: Use two temporary arrays
    #
    # TC: O(M*N)
    # SC: O(M+N)
    def booleanMatrix_solution_1(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        row = [0] * R
        col = [0] * C

        # Initialize all values of row[] as 0
        for i in range(0, R):
            row[i] = 0

        # Initialize all values of col[] as 0
        for i in range(0, C):
            col[i] = 0

        # Store the rows and columns to be marked
        # as 1 in row[] and col[] arrays respectively
        for i in range(0, R):

            for j in range(0, C):
                if matrix[i][j] == 1:
                    row[i] = 1
                    col[j] = 1

        # Modify the input matrix mat[] using the
        # above constructed row[] and col[] arrays
        for i in range(0, R):

            for j in range(0, C):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 1

    # Solution 2: Space optimized version of Solution 1
    #
    # TC: O(M*N)
    # SC: O(1)
    def booleanMatrix_solution_2(self, matrix: List[List[int]]) -> None:
        # r = len(matrix)
        # c = len(matrix[0])
        #
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == 1:
        #             for t in range(c):
        #                 if matrix[i][t] != 1:
        #                     matrix[i][t] = '1'
        #             for u in range(r):
        #                 if matrix[u][j] != 1:
        #                     matrix[u][j] = '1'
        #
        # for i in range(r):
        #     matrix[i] = list(map(int, matrix[i]))

        # variables to check if there are any 1
        # in first row and column
        row_flag = False
        col_flag = False

        # updating the first row and col
        # if 1 is encountered
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 and matrix[i][j] == 1:
                    row_flag = True

                if j == 0 and matrix[i][j] == 1:
                    col_flag = True

                if matrix[i][j] == 1:
                    matrix[0][j] = 1
                    matrix[i][0] = 1

        # Modify the input matrix mat[] using the
        # first row and first column of Matrix mat
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # print(f"{i} ; {j}")
                if matrix[0][j] == 1 or matrix[i][0] == 1:
                    matrix[i][j] = 1

        # modify first row if there was any 1
        if row_flag == True:
            for i in range(0, len(matrix)):
                matrix[0][i - 1] = 1

        # modify first col if there was any 1
        if col_flag == True:
            for i in range(0, len(matrix)):
                matrix[i][0] = 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_booleanMatrix(self) -> None:
        s = Solution()
        matrix, solution = [[1, 0], [0, 0]], [[1, 1], [1, 0]]
        s.booleanMatrix_solution_1(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = [[0, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 1, 1]]
        s.booleanMatrix_solution_1(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = (
            [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 0]],
        )
        s.booleanMatrix_solution_1(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = (
            [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]],
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1]],
        )
        s.booleanMatrix_solution_1(matrix)
        self.assertEqual(solution, matrix)

        matrix, solution = [[1, 0], [0, 0]], [[1, 1], [1, 0]]
        s.booleanMatrix_solution_2(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = [[0, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 1, 1]]
        s.booleanMatrix_solution_2(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = (
            [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 0, 0]],
        )
        s.booleanMatrix_solution_2(matrix)
        self.assertEqual(solution, matrix)
        matrix, solution = (
            [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]],
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1]],
        )
        s.booleanMatrix_solution_2(matrix)
        self.assertEqual(solution, matrix)


if __name__ == "__main__":
    unittest.main()
