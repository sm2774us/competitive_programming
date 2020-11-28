#
# Time  :
# Space :
#
# @tag : Divide And Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Rat in a Maze Problem - I
#
# Description:
#
# Consider a rat placed at (0, 0) in a square matrix of order N*N. It has to reach the destination at (N-1, N-1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and cannot be crossed while value 1 at a cell in the matrix represents that it can be traveled through.
#
# Example 1:
#
# Input: N = 4, m[][] = {{1, 0, 0, 0},
#                        {1, 1, 0, 1},
#                        {1, 1, 0, 0},
#                        {0, 1, 1, 1}}
# Output: DDRDRR DRDDRR
# Explanation: The rat can reach the
# destination at (3, 3) from (0, 0) by two
# paths ie DRDDRR and DDRDRR when printed
# in sorted order we get DDRDRR DRDDRR.
# Example 2:
# Input: N = 2, m[][] = {{1, 0},
#                        {1, 0}}
# Output: -1
# Explanation: No path exits
#
# Your Task:
# You don't need to read input or print anything. Complete the function printPath() which takes N and 2d array m[][] as input parameters and returns a sorted list of paths.
#
# Note:  In case of no path, return an empty list. The driver will output -1 automatically.
#
# Expected Time Complexity: O((N2)4).
# Expected Auxiliary Space: O(L*X), L = length of the path, X = number of paths.
#
# Constraints:
# 2 ≤ N ≤ 5
# 0 ≤ m[i][j] ≤ 1
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1 (GeeksForGeeks - Rat in a Maze Problem - I)
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
    def isSafe(self, n, x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        return True

    def dfs(self, arr, n, x, y, visited, path):
        visited[str(x) + " " + str(y)] = True
        if x == n - 1 and y == n - 1:
            ans.append("".join(path))
        rx = [1, 0, 0, -1]
        ry = [0, 1, -1, 0]

        for i in range(4):
            nx = x + rx[i]
            ny = y + ry[i]
            if self.isSafe(n, nx, ny) and arr[nx][ny] == 1:
                if not visited[str(nx) + " " + str(ny)]:
                    if ny > y:
                        self.dfs(arr, n, nx, ny, visited, path + ["R"])
                    elif nx > x:
                        self.dfs(arr, n, nx, ny, visited, path + ["D"])
                    elif nx < x:
                        self.dfs(arr, n, nx, ny, visited, path + ["U"])
                    elif ny < y:
                        self.dfs(arr, n, nx, ny, visited, path + ["L"])
        visited[str(x) + " " + str(y)] = False

    # Solution 1:
    #
    # Your task is to complete this function
    # Function should return a sorted string
    # String should contains required paths
    # string should contain space separated paths
    def findPath(self, arr: List[int], n: int) -> str:
        global ans
        ans = []
        """
        :type arr: List[int]
        :type n: int
        :rtype: str
        """
        visited = {}
        for i in range(n):
            for j in range(n):
                visited[str(i) + " " + str(j)] = False
        self.dfs(arr, n, 0, 0, visited, [])
        ans.sort()
        return " ".join(ans)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findPath(self) -> None:
        sol = Solution()
        for arr, n, solution in (
            [
                [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]],
                4,
                "DDRDRR DRDDRR",
            ],
            [[[1, 0], [1, 0]], 2, ""],
        ):
            self.assertEqual(solution, sol.findPath(arr, n))


# main
if __name__ == "__main__":
    unittest.main()
