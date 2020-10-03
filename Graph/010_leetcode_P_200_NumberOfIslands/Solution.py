#
# Time : O(V + E); Space: O(V)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 200: Number of Islands
#
# Description:
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# **************************************************************************
# Source: https://leetcode.com/problems/number-of-islands/ (LeetCode - Problem 200 - Number of Islands)
#         https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1 (GeeksForGeeks - Find the number of islands)
#
from typing import List
from collections import defaultdict

import unittest


class Solution:
    def numIslandsIterativeUsingBFS(self, grid):
        # BFS
        if not grid:
            return 0
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    stack = [(i, j)]
                    for ii, jj in stack:
                        if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == "1":
                            grid[ii][jj] = "2"
                            stack.extend(
                                [(ii + 1, jj), (ii - 1, jj), (ii, jj - 1), (ii, jj + 1)]
                            )
        return count

    # Approach : Sink and count the islands.
    # NOTE: Uses Recursive DFS approach.
    #       The recursive dfs calls on the stack we could express space complexity as O(max(m, n)).
    def numIslandsRecursiveConciseSolutionUsingSinkingApproach(
        self, grid: List[List[str]]
    ) -> int:
        def sink(i, j):
            # if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and int(grid[i][j]):
                grid[i][j] = "0"
                # list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))  # map in python3 return iterator
                for i, j in zip((i, i + 1, i, i - 1), (j + 1, j, j - 1, j)):
                    sink(i, j)
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numIslands(self) -> None:
        sol = Solution()
        for grid, solution in (
            [
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ],
                1,
            ],
            [
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ],
                3,
            ],
        ):
            self.assertEqual(
                solution,
                sol.numIslandsIterativeUsingBFS(grid),
                "Should determine the number of islands",
            )
            self.assertEqual(
                solution,
                sol.numIslandsRecursiveConciseSolutionUsingSinkingApproach(grid),
                "Should determine the number of islands",
            )


# main
if __name__ == "__main__":
    unittest.main()
