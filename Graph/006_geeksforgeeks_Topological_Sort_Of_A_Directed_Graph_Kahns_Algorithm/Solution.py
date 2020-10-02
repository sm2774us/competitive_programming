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
from collections import defaultdict

import unittest


class Graph:
    def __init__(self, vertices: int) -> None:
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].append(v)

    # The function to do Topological Sort.
    def topologicalSort(self) -> List[int]:

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # # Check if there was a cycle
        # if cnt != self.V:
        #     print("There exists a cycle in the graph")
        # else:
        #     # Print topological order
        #     print(top_order)
        return top_order


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_topologicalSortOfDirectedGraph(self) -> None:
        g = Graph(6)
        g.addEdge(5, 2)
        g.addEdge(5, 0)
        g.addEdge(4, 0)
        g.addEdge(4, 1)
        g.addEdge(2, 3)
        g.addEdge(3, 1)
        self.assertEqual([4, 5, 2, 0, 3, 1], g.topologicalSort())


# main
if __name__ == "__main__":
    unittest.main()
