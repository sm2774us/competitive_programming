#
# Time : O(V + E); Space: O(V)
# @tag : Hashing ; HashMap
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
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from collections import defaultdict

import unittest


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isCyclic(self) -> None:
        g = Graph(4)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)
        self.assertEqual(True, g.isCyclic())


# main
if __name__ == "__main__":
    unittest.main()
