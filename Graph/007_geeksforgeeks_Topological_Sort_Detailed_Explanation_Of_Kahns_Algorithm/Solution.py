#
# Time : O(V + E)
# The outer for loop will be executed V number of times and the inner for loop will be executed E number of times.
#
# Space: O(V)
# The queue needs to store all the vertices of the graph. So the space required is O(V)
#
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Topological sort
#
# Description:
#
# Given a Directed Graph. Find any Topological Sorting of that Graph.
#
# Input:
# The first line of input takes the number of test cases then T test cases follow . Each test case contains two lines. The first  line of each test case  contains two integers E and V representing no of edges and the number of vertices. Then in the next line are E  pairs of integers u, v representing an edge from u to v in the graph.
#
# Output:
# For each test case output will be 1 if the topological sort is done correctly else it will be 0.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function topoSort() which takes the adjacency list of the Graph and the number of vertices (N) as inputs are returns an array consisting of a the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them.
#
# Expected Time Complexity: O(V + E).
# Expected Auxiliary Space: O(V).
#
# Constraints:
# 1 <= T <= 100
# 2 <= V <= 104
# 1 <= E <= (N*(N-1))/2
# 0 <= u, v <= N-1
# Graph doesn't contain multiple edges, self loops and cycles.
# Graph may be disconnected.
#
# Example:
# Input
# 2
# 6 6
# 5 0 5 2 2 3 4 0 4 1 1 3
# 3 4
# 3 0 1 0 2 0
#
# Output:
# 1
# 1
#
# Explanation:
# Testcase 1: The output 1 denotes that the order is valid.  So, if you have implemented your function correctly, then output would be 1 for all test cases.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/topological-sort/1 (GeeksForGeeks - Topological sort)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
# A Python program to print topological sorting of a graph
# using indegrees
from typing import List
from collections import deque

import unittest

# class to represent a graph object:
class Graph:

    # stores indegree of a vertex
    indegree = None

    # Constructor
    def __init__(self, edges: List[int], N: int) -> None:
        # Set the list of graph edges
        self.edges = edges
        # Set number of vertices in the graph
        self.N = N
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(self.N)]

        # initialize indegree of each vertex by 0
        self.indegree = [0] * self.N

        # add edges to the undirected graph
        for (src, dest) in self.edges:
            # add an edge from source to destination
            self.adjList[src].append(dest)

            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1

    # performs Topological Sort on a given DAG
    def doTopologicalSort(self) -> List[int]:
        # list to store the sorted elements
        L = []

        # get in-degree information of the graph
        indegree = self.indegree

        # Set of all nodes with no incoming edges
        S = deque([i for i in range(self.N) if indegree[i] == 0])

        while S:

            # remove a node n from S
            n = S.pop()

            # add n to tail of L
            L.append(n)

            for m in self.adjList[n]:

                # remove edge from n to m from the graph
                indegree[m] = indegree[m] - 1

                # if m has no other incoming edges then
                # insert m into S
                if indegree[m] == 0:
                    S.append(m)

        # if graph has edges then graph has at least one cycle
        for i in range(self.N):
            if indegree[i]:
                return None

        return L


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_topologicalSortOfDirectedGraph(self) -> None:
        # List of graph edges as per above diagram
        edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

        # Set number of vertices in the graph
        N = 8

        # create a graph from edges
        graph = Graph(edges, N)

        # Perform Topological Sort
        L = graph.doTopologicalSort()
        # if L:
        #     print(L)  # print topological order
        # else:
        #     print("Graph has at least one cycle. Topological sorting is not possible.")
        self.assertEqual([7, 5, 1, 2, 3, 4, 0, 6], L)


# main
if __name__ == "__main__":
    unittest.main()
