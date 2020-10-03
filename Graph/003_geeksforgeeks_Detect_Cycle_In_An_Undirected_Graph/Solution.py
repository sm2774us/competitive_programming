#
# Time : O(V + E); Space: O(V)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Detect cycle in an undirected graph
#
# Description:
#
# Given a Undirected Graph. Check whether it contains a cycle or not.
#
# Input:
# The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' testcases follow. Each testcase consists of two lines. Description of testcases are as follows: The First line of each testcase contains two integers 'N' and 'M' which denotes the no of vertices and no of edges respectively. The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is a bidirectional  edge from u to v .
#
# Output:
# The method should return 1 if there is a cycle else it should return 0.
#
# User task:
# You don't need to read input or print anything. Your task is to complete the function isCyclic which takes the Graph and the number of vertices as inputs and returns true if the given undirected graph contains any cycle. Else, it returns false.
#
# Expected Time Complexity: O(V + E).
# Expected Auxiliary Space: O(V).
#
# Constraints:
# 1 <= T <= 100
# 2 <= N <= 104
# 1 <= M <= (N*(N-1))/2
# 0 <= u, v <=  N-1
# Graph doesn't contain multiple edges and self loops.
#
# Example:
# Input:
# 3
# 2 1
# 0 1
# 4 3
# 0 1 1 2 2 3
# 5 4
# 0 1 2 3 3 4 4 2
#
# Output:
# 0
# 0
# 1
#
# Explanation:
# Testcase 1: There is a graph with 2 vertices and 1 edge from 0 to 1. So there is no cycle.
# Testcase 2: There is a graph with 3 vertices and 3 edges from 0 to 1, 1 to 2 and 2 to 3.
# Testcase 3: There is a cycle in the given graph formed by vertices 2, 3 and 4.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1/ (GeeksForGeeks - Detect cycle in an undirected graph)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List
from collections import defaultdict

import unittest

# This class represents a undirected graph using adjacency list representation
class Graph:
    def __init__(self, vertices: int) -> None:
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, v: int, w: int) -> None:
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v: int, visited: List[bool], parent: List[bool]) -> bool:

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    # Returns true if the graph contains a cycle, else false.
    def isCyclic(self) -> bool:
        # Mark all the vertices as not visited
        visited = [False] * (self.V)
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(self.V):
            if not visited[i]:  # Don't recur for u if it is already visited
                if self.isCyclicUtil(i, visited, -1):
                    return True

        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isUndirectedGraphCyclic(self) -> None:
        g = Graph(5)
        g.addEdge(1, 0)
        g.addEdge(0, 2)
        g.addEdge(2, 0)
        g.addEdge(0, 3)
        g.addEdge(3, 4)
        self.assertEqual(True, g.isCyclic())

        g = Graph(3)
        g.addEdge(0, 1)
        g.addEdge(1, 2)
        self.assertEqual(False, g.isCyclic())


# main
if __name__ == "__main__":
    unittest.main()
