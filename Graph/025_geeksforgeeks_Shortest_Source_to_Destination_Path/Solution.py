#
# Time : O(MN) for an MxN matrix
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Shortest Source to Destination Path
#
# Description:
#
# Given a boolean 2D matrix (0-based index), find whether there is path from (0,0) to (x,y) and if there is one path,
# print the minimum no of steps needed to reach it, else print -1 if the destination is not reachable.
# You may move in only four direction ie up, down, left and right. The path can only be created out of a cell
# if its value is 1.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines . The first line of each test case contains two integers n and m denoting the size of the matrix. Then in the next line are n*m space separated values of the matrix. The following line after it contains two integers x and y denoting the index of the destination.
#
# Output:
# For each test case print in a new line the min no of steps needed to reach the destination.
#
# Constraints:
# 1<=T<=100
# 1<=n,m<=20
#
# Example:
# Input:
# 2
# 3 4
# 1 0 0 0 1 1 0 1 0 1 1 1
# 2 3
# 3 4
# 1 1 1 1 0 0 0 1 0 0 0 1
# 0 3
# Output:
# 5
# 3
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/shortest-source-to-destination-path/0 (GeeksForGeeks - Shortest Source to Destination Path)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#

# Python program to find the shortest
# path between a given source cell
# to a destination cell.

from collections import deque

import unittest

ROW = 9
COL = 10

# To store matrix cell cordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # A data structure for queue used in BFS


class QueueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source


class Solution:
    # Check whether given cell(row,col)
    # is a valid cell or not
    def isValid(self, row: int, col: int):
        return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

    # Function to find the shortest path between ( uses BFS )
    # a given source cell to a destination cell.
    def shortestPath(self, mat, src: Point, dest: Point):
        # These arrays are used to get row and column
        # numbers of 4 neighbours of a given cell
        rowNum = [-1, 0, 0, 1]
        colNum = [0, -1, 1, 0]

        # check source and destination cell
        # of the matrix have value 1
        if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
            return -1

        visited = [[False for i in range(COL)] for j in range(ROW)]

        # Mark the source cell as visited
        visited[src.x][src.y] = True

        # Create a queue for BFS
        q = deque()

        # Distance of source cell is 0
        s = QueueNode(src, 0)
        q.append(s)  # Enqueue source cell

        # Do a BFS starting from source cell
        while q:

            curr = q.popleft()  # Dequeue the front cell

            # If we have reached the destination cell,
            # we are done
            pt = curr.pt
            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

                # Otherwise enqueue its adjacent cells
            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]

                # if adjacent cell is valid, has path
                # and not visited yet, enqueue it.
                if (
                    self.isValid(row, col)
                    and mat[row][col] == 1
                    and not visited[row][col]
                ):
                    visited[row][col] = True
                    Adjcell = QueueNode(Point(row, col), curr.dist + 1)
                    q.append(Adjcell)

        # Return -1 if destination cannot be reached
        return -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_shortestPath(self) -> None:
        sol = Solution()
        mat = [
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        ]
        source = Point(0, 0)
        dest = Point(3, 4)
        self.assertEqual(11, sol.shortestPath(mat, source, dest))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    #        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    #        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    #        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    #        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    #        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    #        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    #        [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    # source = Point(0, 0)
    # dest = Point(3, 4)
    #
    # dist = sol.shortestPath(mat, source, dest)
    #
    # if dist != -1:
    #     print("Shortest Path is", dist)
    # else:
    #     print("Shortest Path doesn't exist")
    unittest.main()
