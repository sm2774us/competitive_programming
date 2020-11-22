#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 392: Longest Increasing Path in a Matrix
#
# Description:
#
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
#
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ (LeetCode - Problem 329 - Longest Increasing Path in a Matrix)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):

    # Solution_1 : Bottom-up Dynamic Programming based Solution
    def longestIncreasingPath_BottomUp_DP(self, matrix: List[List[int]]) -> int:
        def length(z):
            if z not in memo:
                memo[z] = 1 + max(
                    [
                        length(Z)
                        for Z in [z + 1, z - 1, z + 1j, z - 1j]
                        if Z in matrix and matrix[z] > matrix[Z]
                    ]
                    or [0]
                )
            return memo[z]

        memo = {}
        matrix = {
            i + j * 1j: val for i, row in enumerate(matrix) for j, val in enumerate(row)
        }
        return max(map(length, matrix), default=0)

    # Solution_2 : Top-down Dynamic Programming based Solution
    def longestIncreasingPath_TopDown_DP(self, matrix: List[List[int]]) -> int:
        matrix = {
            i + j * 1j: val for i, row in enumerate(matrix) for j, val in enumerate(row)
        }
        length = {}
        for z in sorted(matrix, key=matrix.get):
            length[z] = 1 + max(
                [
                    length[Z]
                    for Z in (z + 1, z - 1, z + 1j, z - 1j)
                    if Z in matrix and matrix[z] > matrix[Z]
                ]
                or [0]
            )
        return max(length.values(), default=0)

    # Solution_3 : Bottom-up Dynamic Programming based Solution
    def longestIncreasingPath_TopologicalSortingOnDAG(
        self, matrix: List[List[int]]
    ) -> int:
        # Step 1: build a directed acyclic graph
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                for x, y in neighbors:
                    if (
                        0 <= x < len(matrix)
                        and 0 <= y < len(matrix[0])
                        and matrix[i][j] < matrix[x][y]
                    ):
                        graph[(i, j)].append((x, y))
                        indegree[(x, y)] += 1

        # Step 2: Topological sorting with Kahn's algorithm
        queue = collections.deque(
            [
                (i, j)
                for i in range(len(matrix))
                for j in range(len(matrix[0]))
                if (i, j) not in indegree
            ]
        )
        max_path_len = 0
        while queue:
            max_path_len += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
        return max_path_len


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestIncreasingPath(self) -> None:
        sol = Solution()
        for matrix, solution in (
            [[[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4],
            [[[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4],
        ):
            self.assertEqual(solution, sol.longestIncreasingPath_BottomUp_DP(matrix))
            self.assertEqual(solution, sol.longestIncreasingPath_TopDown_DP(matrix))
            self.assertEqual(
                solution, sol.longestIncreasingPath_TopologicalSortingOnDAG(matrix)
            )


# main
if __name__ == "__main__":
    unittest.main()
