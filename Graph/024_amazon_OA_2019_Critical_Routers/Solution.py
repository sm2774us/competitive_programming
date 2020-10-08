# Amazon | OA 2019 / 2020 | Critical Routers
#
# Time : O(N); Space: O(N)
# @tag : Graph ; DFS
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Amazon | OA 2019 / 2020 | Critical Routers
#
# Description:
#
# You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.
#
# Input:
# The input to the function/method consists of three arguments:
#
# numNodes, an integer representing the number of nodes in the graph.
# numEdges, an integer representing the number of edges in the graph.
# edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
#
# Output:
# Return a list of integers representing the critical nodes.
#
# Example:
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# **************************************************************************
# Related problems:
# **************************************************************************
# - Critical Connections [ https://leetcode.com/discuss/interview-question/372581 ]
# - Articualtion Points or Cut Vertices in a graph [ https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/ ]
# - Cut Points [ https://cp-algorithms.com/graph/cutpoints.html ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/network-delay-time/ (LeetCode - Problem 743 - Network Delay Time)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List
import collections

import unittest


class Solution:
    # Method 1 : Using DFS
    def critical_routers_using_DFS(self, numNodes, numEdges, edges):
        """
        :type numNodes: int
        :type numEdges: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        self.value_graph = collections.defaultdict(list)
        value_list = [-1] * numNodes
        self.res = []

        for i in range(numEdges):
            a, b = edges[i]
            self.value_graph[a].append(b)
            self.value_graph[b].append(a)

        self.dfs(-1, 0, 0, value_list)

        return self.res

    def dfs(self, a, b, count, value_list):
        value_list[b] = count + 1

        for node in self.value_graph[b]:
            if node == a:
                continue
            elif value_list[node] == -1:
                temp_value = self.dfs(b, node, count + 1, value_list)
                value_list[b] = min(value_list[b], temp_value)
            else:
                value_list[b] = min(value_list[b], value_list[node])

        if value_list[b] == count + 1 and b != 0:
            self.res.append(a)
        return value_list[b]

    # Method 2 : Using Biconnected Component
    # Linear Time Solution
    # Reference: https: // en.wikipedia.org / wiki / Biconnected_component
    def get_adj_list(self, edges: List[int], num_nodes: int) -> List[List[int]]:
        adj = [[] for _ in range(num_nodes)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    """
    O(V+E) time because of DFS
    O(V+E) space because of the adjacency list and call stack
    """

    def critical_routers_using_Biconnected_Component(
        self, num_nodes: int, num_edges: int, edges: List[List[int]]
    ) -> List[int]:
        adj = self.get_adj_list(edges, num_nodes)
        n = num_nodes
        visited = [False for _ in range(n)]
        depth = [-1 for _ in range(n)]
        low = [-1 for _ in range(n)]
        parent = [None for _ in range(n)]
        art_points = []  # articulation points

        """
        Run DFS while maintaining the following:
        * The depth of each vertex in the DFS tree (once it gets visited)
        * the lowpoint for each vertex v, i.e. the lowest depth of neighbors of all 
        descendants of v (including v itself) in the DFS tree.
        """

        def get_art_points(node: int, d: int) -> None:
            visited[node] = True
            depth[node] = d
            low[node] = d
            child_count = 0
            articulation = False  # for input node

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    get_art_points(neighbor, d + 1)
                    child_count += 1
                    if low[neighbor] >= depth[node]:
                        articulation = True
                    low[node] = min(low[node], low[neighbor])
                elif neighbor != parent[node]:
                    low[node] = min(low[node], low[neighbor])
            if (parent[node] and articulation) or (
                not parent[node] and child_count > 1
            ):
                art_points.append(node)

        get_art_points(0, 0)
        return art_points


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_critical_routers(self) -> None:
        sol = Solution()
        numNodes = 7
        numEdges = 7
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        self.assertEqual(
            [5, 2, 3], sol.critical_routers_using_DFS(numNodes, numEdges, edges)
        )
        self.assertEqual(
            [5, 2, 3],
            sol.critical_routers_using_Biconnected_Component(numNodes, numEdges, edges),
        )


# main
if __name__ == "__main__":
    unittest.main()
