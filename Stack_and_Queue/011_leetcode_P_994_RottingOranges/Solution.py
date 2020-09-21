#
# Time : O(N); Space: O(1)
# @tag : Stack and Queue - BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 994: Rotting Oranges
#
# Description:
#
# In a given grid, each cell can have one of three values:
#
#   * the value 0 representing an empty cell;
#   * the value 1 representing a fresh orange;
#   * the value 2 representing a rotten orange.
#   * Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible,
# return -1 instead.
#
# Examples:
# Refer to Problem_Description.md.
#
# **************************************************************************
# Source: https://leetcode.com/problems/rotting-oranges/ (Leetcode - Problem 994 - Rotting Oranges)
#         https://practice.geeksforgeeks.org/problems/rotten-oranges/0 (GeeksForGeeks - Rotten Oranges)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from typing import List
import itertools
from collections import deque

import unittest


class Solution:
    def orangesRottingConcise(self, grid: List[List[int]]) -> int:
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0

        # for i, j in itertools.product(range(m), range(n)):
        # where,
        # itertools.product is a cartesian product for-loop, i.e., a more concise way of saying :
        # for r in range(m):
        #     for c in range(n):

        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh += 1
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        levels = 0

        while queue:
            levels += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    if (
                        0 <= x + dx < m
                        and 0 <= y + dy < n
                        and grid[x + dx][y + dy] == 1
                    ):
                        fresh -= 1
                        grid[x + dx][y + dy] = 2
                        queue.append((x + dx, y + dy))

        return -1 if fresh != 0 else max(levels - 1, 0)

    # Time complexity: O(rows * cols) -> each cell is visited at least once
    # Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # number of rows
        rows = len(grid)
        if rows == 0:  # check if grid is empty
            return -1

        # number of columns
        cols = len(grid[0])

        # keep track of fresh oranges
        fresh_cnt = 0

        # queue with rotten oranges (for BFS)
        rotten = deque()

        # visit each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    # update fresh oranges count
                    fresh_cnt += 1

        # keep track of minutes passed.
        minutes_passed = 0

        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_cnt > 0:

            # update the number of minutes passed
            # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
            minutes_passed += 1

            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                # visit all the adjacent cells
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    # update the fresh oranges count
                    fresh_cnt -= 1

                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2

                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        # return the number of minutes taken to make all the fresh oranges to be rotten
        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_cnt == 0 else -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_orangesRotting(self) -> None:
        s = Solution()
        for grid, solution in (
            [[[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4],
            [[[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1],
            [[[0, 2]], 0],
        ):
            self.assertEqual(
                solution,
                s.orangesRotting(grid),
                "Should return the minimum number of minutes that must elapse until no cell has a fresh orange",
            )

    def test_orangesRottingConcise(self) -> None:
        s = Solution()
        for grid, solution in (
            [[[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4],
            [[[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1],
            [[[0, 2]], 0],
        ):
            self.assertEqual(
                solution,
                s.orangesRottingConcise(grid),
                "Should return the minimum number of minutes that must elapse until no cell has a fresh orange",
            )


if __name__ == "__main__":
    unittest.main()
