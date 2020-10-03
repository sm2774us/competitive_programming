#
# Time : O(V + E); Space: O(V)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Detect cycle in a directed graph
#
# Description:
#
# Given a Directed Graph. Check whether it contains any cycle or not.
#
# Input: The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of two lines. Description of testcases is as follows: The First line of each test case contains two integers 'N' and 'M'  which denotes the no of vertices and no of edges respectively. The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is an uni-directed  edge from u to v .
#
# Output:
# The method should return 1 if there is a cycle else it should return 0.
#
# User task:
# You don't need to read input or print anything. Your task is to complete the function isCyclic which takes the Graph and the number of vertices and inputs and returns true if the given directed graph contains a cycle. Else, it returns false.
#
# Expected Time Complexity: O(V + E).
# Expected Auxiliary Space: O(V).
#
# Constraints:
# 1 <= T <= 1000
# 1<= N,M <= 1000
# 0 <= u,v <= N-1
#
# Example:
# Input:
# 3
# 2 2
# 0 1 0 0
# 4 3
# 0 1 1 2 2 3
# 4 3
# 0 1 2 3 3 2
# Output:
# 1
# 0
# 1
#
# Explanation:
# Testcase 1: In the above graph there are 2 vertices. The edges are as such among the vertices.
#
#   _____
# /       \
# \ _____ /
#  /     \
# +       +
# +   0   +
#  \     / \
#   -----   \
#            \
#             \  _____
#              +/     \
#              +       +
#              +   1   +
#               \     /
#                -----
#
# From graph it is clear that it contains cycle.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1 (GeeksForGeeks - Detect cycle in a directed graph)
#
# Youtube Video Explanation: https://youtu.be/ba4YGd7S-TY
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
from typing import List
import sys

import unittest

INT_MAX = sys.maxsize


class Graph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist: List[int]) -> None:
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(f"{node}\t{dist[node]}")

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist: List[int], sptSet: List[bool]) -> int:
        # Initilaize minimum distance for next node
        min = INT_MAX

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v

        return min_index

        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src: int) -> List[int]:

        dist = [INT_MAX] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not sptSet[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        # self.printSolution(dist)
        return dist


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_dijkstra(self) -> None:
        g = Graph(9)
        g.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0],
        ]
        self.assertEqual([0, 4, 12, 19, 21, 11, 9, 8, 14], g.dijkstra(0))


# main
if __name__ == "__main__":
    unittest.main()
