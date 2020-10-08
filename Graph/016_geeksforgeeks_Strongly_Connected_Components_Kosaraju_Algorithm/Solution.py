#
# Time : O(V+E); Space: O(E)
# where, V = number of vertices
#        E = number of edges
# @tag : Graph ; Kosaraju's Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Strongly Connected Components (Kosaraju's Algo)
#
# Description:
#
# Given a graph with N nodes and M directed edges. Your task is to complete the function kosaraju() which returns an integer denoting the number of strongly connected components in the graph.
#
# Input:
# The first line of input contains an integer T. Then T test cases follow. Each test case contains two integers N and M. In the next line there are M space-separated values u,v denoting an edge from u to v.
#
# Output:
# For each test case in a new line output will an integer denoting the no of strongly connected components present in the graph.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function kosaraju() which takes the number of vertices V and adjacency list of the graph as inputs and returns an integer denoting the number of strongly connected components in the given graph.
#
# Expected Time Complexity: O(N + M).
# Expected Auxiliary Space: O(N).
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 5000
# 0 <= M <= (N*(N-1))
# 0 <= u, v <= N-1
# Sum of M over all testcases will not exceed 25*106
#
# Example:
# Input:
# 2
# 5 5
# 1 0 0 2 2 1 0 3 3 4
# 3 3
# 0 1 1 2 2 0
#
# Output:
# 3
# 1
#
# Explanation:
# Testcase 1:
# There is a connected subgraph that includes 0-1-2 which satisfy the condition of strongly connecting components i.e each node is reachable from every other nodes.
#
# Another subgraph includes individual nodes 4 and 3. That gives us a total of 3 subgraphs satisfying the condition of strongly connected components.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1 [GeeksForGeeks - Strongly Connected Components (Kosaraju's Algo)]
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#

# Python implementation of Kosaraju's algorithm to print all SCCs
from collections import defaultdict

import unittest


# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS

    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        # print(f"{v}", end=" ")
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

        # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

        # The main function that finds and prints all strongly

    # connected components
    def countSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)

        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by Stack
        ans = 0
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.DFSUtil(i, visited)
                ans += 1

        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countSCCs(self) -> None:
        g = Graph(5)
        g.addEdge(1, 0)
        g.addEdge(0, 2)
        g.addEdge(2, 1)
        g.addEdge(0, 3)
        g.addEdge(3, 4)
        self.assertEqual(3, g.countSCCs())
        g = Graph(3)
        g.addEdge(0, 1)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        self.assertEqual(1, g.countSCCs())


# main
if __name__ == "__main__":
    # # Create a graph given in the above diagram
    # g = Graph(5)
    # g.addEdge(1, 0)
    # g.addEdge(0, 2)
    # g.addEdge(2, 1)
    # g.addEdge(0, 3)
    # g.addEdge(3, 4)
    #
    # print("Following are strongly connected components " +
    #       "in given graph")
    # g.countSCCs()
    unittest.main()
