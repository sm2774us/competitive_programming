#
# Time  : O(N*M)
# Space : O(N*M)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Find whether path exist
#
# Description:
#
# Given a N X N matrix (M) filled with 1, 0, 2, 3.
# The task is to find whether there is a path possible from source to destination,
# while traversing through blank cells only. You can traverse up, down, right and left.
#
# A value of cell 1 means Source.
# A value of cell 2 means Destination.
# A value of cell 3 means Blank cell.
# A value of cell 0 means Blank Wall.
# Note: there is only single source and single destination.
#
#
#
# Input:
# The first line of input is an integer T denoting the no of testcases.
# Then T test cases follow. Each test case consists of 2 lines.
# The first line of each test case contains an integer N denoting the size of the square matrix.
# Then in the next line are N*N space separated values of the matrix (M).
#
# Output:
# For each test case in a new line print 1 if the path exist from source to destination else print 0.
#
# Constraints:
# 1 <= T <= 20
# 1 <= N <= 20
#
# Example:
# Input:
# 2
# 4
# 3 0 0 0 0 3 3 0 0 1 0 3 0 2 3 3
# 3
# 0 3 2 3 0 0 1 0 0
#
# Output:
# 1
# 0
#
# Explanation:
# Testcase 1: The matrix for the above given input is:
# 3 0 0 0
# 0 3 3 0
# 0 1 0 3
# 0 2 3 3
# From the matrix we can see that there exists a path from to reach destination 2 from source 1.
# Testcase 2: The matrix for the above given input is:
# 0 3 2
# 3 0 0
# 1 0 0
# From the matrix we can see that there does not exists any path to reach destination 2 from source 1.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/find-whether-path-exist/0 (GeeksForGeeks - Find whether path exist)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#

# Python3 program to find path between two
# cell in matrix
from collections import defaultdict

import unittest


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

        # add edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # BFS function to find path from source to sink
    def BFS(self, s, d):

        # Base case
        if s == d:
            return True

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph) + 1)

        # Create a queue for BFS
        queue = []
        queue.append(s)

        # Mark the current node as visited and
        # enqueue it
        visited[s] = True
        while queue:

            # Dequeue a vertex from queue
            s = queue.pop(0)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent has
            # not been visited, then mark it visited
            # and enqueue it
            for i in self.graph[s]:

                # If this adjacent node is the destination
                # node, then return true
                if i == d:
                    return True

                # Else, continue to do BFS
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        # If BFS is complete without visiting d
        return False


class Solution:
    def isSafe(self, i, j, matrix):
        if i >= 0 and i <= len(matrix) and j >= 0 and j <= len(matrix[0]):
            return True
        else:
            return False

    # Returns true if there is a path from a source (a
    # cell with value 1) to a destination (a cell with
    # value 2)
    def doesPathExist(self, M):
        s, d = None, None  # source and destination
        N = len(M)
        g = Graph()

        # create graph with n * n node
        # each cell consider as node
        k = 1  # Number of current vertex
        for i in range(N):
            for j in range(N):
                if M[i][j] != 0:

                    # connect all 4 adjacent cell to
                    # current cell
                    if self.isSafe(i, j + 1, M):
                        g.addEdge(k, k + 1)
                    if self.isSafe(i, j - 1, M):
                        g.addEdge(k, k - 1)
                    if self.isSafe(i + 1, j, M):
                        g.addEdge(k, k + N)
                    if self.isSafe(i - 1, j, M):
                        g.addEdge(k, k - N)

                if M[i][j] == 1:
                    s = k

                    # destination index
                if M[i][j] == 2:
                    d = k
                k += 1

        # find path Using BFS
        return g.BFS(s, d)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_doesPathExist(self) -> None:
        sol = Solution()
        M = [[0, 3, 0, 1], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]]
        self.assertEqual(True, sol.doesPathExist(M))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # M = [[0, 3, 0, 1], [3, 0, 3, 3], [2, 3, 3, 3], [0, 3, 3, 3]]
    # if sol.findPath(M):
    #     print("Yes")
    # else:
    #     print("No")
    unittest.main()
