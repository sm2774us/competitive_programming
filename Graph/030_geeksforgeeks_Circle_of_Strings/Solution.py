#
# Time  : O(N*M)
# Space : O(N*M)
# @tag : Graph ; Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Minimum Cost Path
#
# Description:
#
# Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum. You can move in 4 directions : up, down, left an right.
#
# Note : It is assumed that negative cost cycles do not exist in input matrix.
#
# Input:
# The first line of input will contain number of testcases T. Then T test cases follow. Each test case contains 2 lines. The first line of each test case contains an integer N denoting the size of the grid. Next line of each test contains a single line containing N*N space separated integers depicting the cost of respective cell from (0,0) to (N,N).
#
# Output:
# For each test case output a single integer depecting the minimum cost to reach the destination.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 100
# 1 <= grid[i][j] <= 104
#
# Example:
# Input:
# 2
# 5
# 31 100 65 12 18 10 13 47 157 6 100 113 174 11 33 88 124 41 20 140 99 32 111 41 20
# 2
# 42 93 7 14
#
# Output:
# 327
# 63
#
# Explanation:
# Testcase 1:
# Grid is:
# 31, 100, 65, 12, 18,
# 10, 13, 47, 157, 6,
# 100. 113, 174, 11, 33,
# 88, 124, 41, 20, 140,
# 99, 32, 111, 41, 20
# A cost grid is given in below diagram, minimum
# cost to reach bottom right from top left
# is 327 (31 + 10 + 13 + 47 + 65 + 12 + 18 + 6 + 33 + 11 + 20 + 41 + 20)
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-cost-path/0 (GeeksForGeeks - Minimum Cost Path)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List

import unittest

# Python program to check if a given directed graph is Eulerian or not
CHARS = 26


# A class that represents an undirected graph
class Graph(object):
    def __init__(self, V):
        self.V = V  # No. of vertices
        self.adj = [[] for x in range(V)]  # a dynamic array
        self.inp = [0] * V

        # function to add an edge to graph

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.inp[w] += 1

    # Method to check if this graph is Eulerian or not
    def isSC(self):
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * self.V

        # Find the first vertex with non-zero degree
        n = 0
        for n in range(self.V):
            if len(self.adj[n]) > 0:
                break

        # Do DFS traversal starting from first non zero degree vertex.
        self.DFSUtil(n, visited)

        # If DFS traversal doesn't visit all vertices, then return false.
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        for i in range(self.V):
            visited[i] = False

        # Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.DFSUtil(n, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        for i in range(self.V):
            if len(self.adj[i]) > 0 and visited[i] == False:
                return False

        return True

    # This function returns true if the directed graph has an eulerian
    # cycle, otherwise returns false
    def isEulerianCycle(self):

        # Check if all non-zero degree vertices are connected
        if self.isSC() == False:
            return False

        # Check if in degree and out degree of every vertex is same
        for i in range(self.V):
            if len(self.adj[i]) != self.inp[i]:
                return False

        return True

    # A recursive function to do DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in range(len(self.adj[v])):
            if not visited[self.adj[v][i]]:
                self.DFSUtil(self.adj[v][i], visited)

                # Function that returns reverse (or transpose) of this graph

    # This function is needed in isSC()
    def getTranspose(self):
        g = Graph(self.V)
        for v in range(self.V):
            # Recur for all the vertices adjacent to this vertex
            for i in range(len(self.adj[v])):
                g.adj[self.adj[v][i]].append(v)
                g.inp[v] += 1
        return g

    # This function takes an of strings and returns true


class Solution:
    # if the given array of strings can be chained to
    # form cycle
    def canBeChained(self, arr: List[str], n: int) -> bool:
        # Create a graph with 'aplha' edges
        g = Graph(CHARS)

        # Create an edge from first character to last character
        # of every string
        for i in range(n):
            s = arr[i]
            g.addEdge(ord(s[0]) - ord("a"), ord(s[len(s) - 1]) - ord("a"))

        # The given array of strings can be chained if there
        # is an eulerian cycle in the created graph
        return g.isEulerianCycle()


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canBeChained(self) -> None:
        sol = Solution()
        for arr, n, solution in (
            [["for", "geek", "rig", "kaf"], 4, True],
            [["aab", "abb"], 2, False],
        ):
            self.assertEqual(
                solution,
                sol.canBeChained(arr, n),
                "Should determine if the strings can be chained together to form a circle",
            )


# main
if __name__ == "__main__":
    # Driver program
    sol = Solution()
    arr1 = ["for", "geek", "rig", "kaf"]
    n1 = len(arr1)
    if sol.canBeChained(arr1, n1):
        print("Can be chained")
    else:
        print("Cant be chained")

    arr2 = ["aab", "abb"]
    n2 = len(arr2)
    if sol.canBeChained(arr2, n2):
        print("Can be chained")
    else:
        print("Can't be chained")
    unittest.main()
