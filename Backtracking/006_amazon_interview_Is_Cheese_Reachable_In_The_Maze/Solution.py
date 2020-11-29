#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Amazon Interview - Is cheese reachable in the maze?
#
# Description:
#
# Refer to LeetCode_Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/algorithms/124715/amazon-is-cheese-reachable-in-the-maze (Amazon Interview - Is cheese reachable in the maze?)
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):
    # Solution: DFS with memoization
    def isPath(self, maze):
        def find_if_possible(memo_grid, visited, grid, row_no, col_no):
            if (
                row_no == -1
                or row_no == len(grid)
                or col_no == len(grid[0])
                or col_no == -1
                or visited[row_no][col_no]
                or grid[row_no][col_no] == 0
            ):
                return False

            if grid[row_no][col_no] == 9:
                return True

            if memo_grid[row_no][col_no] is not None:
                return memo_grid[row_no][col_no]

            visited[row_no][col_no] = True

            can_find_cheese = False

            can_find_cheese = (
                find_if_possible(memo_grid, visited, grid, row_no - 1, col_no)
                or can_find_cheese
            )
            can_find_cheese = (
                find_if_possible(memo_grid, visited, grid, row_no + 1, col_no)
                or can_find_cheese
            )
            can_find_cheese = (
                find_if_possible(memo_grid, visited, grid, row_no, col_no + 1)
                or can_find_cheese
            )
            can_find_cheese = (
                find_if_possible(memo_grid, visited, grid, row_no, col_no - 1)
                or can_find_cheese
            )

            visited[row_no][col_no] = False
            memo_grid[row_no][col_no] = can_find_cheese
            return can_find_cheese

        visited = [[False] * len(maze[0]) for row in range(len(maze))]
        memo_grid = [[None] * len(maze[0]) for row in range(len(maze))]
        row_no = 0
        col_no = 0
        return find_if_possible(memo_grid, visited, maze, row_no, col_no)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isPath(self) -> None:
        sol = Solution()
        maze = [
            [1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 9, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(True, sol.isPath(maze))


# main
if __name__ == "__main__":
    unittest.main()
