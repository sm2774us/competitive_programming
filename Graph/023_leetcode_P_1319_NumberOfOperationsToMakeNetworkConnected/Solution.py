#
# Time  : O(connections)
# Space : O(n)
#
# @tag : Graph ; DFS ; SCC (Strongly Connected Components) ; Union Find
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1319: Number of Operations to Make Network Connected
#
# Description:
#
# There are n computers numbered from 0 to n-1 connected by ethernet cables connections
# forming a network where connections[i] = [a, b] represents a connection
# between computers a and b. Any computer can reach any other computer directly
# or indirectly through the network.
#
# Given an initial computer network connections. You can extract certain cables
# between two directly connected computers, and place them between any pair of
# disconnected computers to make them directly connected.
# Return the minimum number of times you need to do this in order to make all the
# computers connected. If it's not possible, return -1.
#
# **************************************************************************
# Examples
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# Constraints:
#
#   * 1 <= n <= 10^5
#   * 1 <= connections.length <= min(n*(n-1)/2, 10^5)
#   * connections[i].length == 2
#   * 0 <= connections[i][0], connections[i][1] < n
#   * connections[i][0] != connections[i][1]
#   * There are no repeated connections.
#   * No two computers are connected by more than one cable.
#
# **************************************************************************
# Source: https://leetcode.com/problems/number-of-operations-to-make-network-connected/ (LeetCode - Problem 1319 - Number of Operations to Make Network Connected)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List
import collections

import unittest


class DisjointSetUnion(object):
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [i for i in range(size)]

    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        rank_u = self.rank[root_u]
        rank_v = self.rank[root_v]

        if rank_u == rank_v:
            rank_u += 1
            self.parent[root_v] = root_u
        elif rank_u > rank_v:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v


class Solution:

    # Method 1 : Using DFS
    #
    # Explanation
    # ==========================================
    # We need at least n - 1 cables to connect all nodes (like a tree).
    # If connections.size() < n - 1, we can directly return -1.
    #
    # One trick is that, if we have enough cables,
    # we don't need to worry about where we can get the cable from.
    #
    # We only need to count the number of connected networks.
    # To connect two unconnected networks, we need to set one cable.
    #
    # The number of operations we need = the number of connected networks - 1
    #
    #
    # Complexity
    # ==========================================
    # Time  : O(connections)
    # Space : O(n)
    #
    def makeConnectedUsingDFS(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        G = [set() for i in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n

        def dfs(i):
            if seen[i]:
                return 0
            seen[i] = 1
            for j in G[i]:
                dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1

    # Method 2 : Using SCC (Strongly Connected Component) algorithm
    def makeConnectedUsingSCC(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj_list = collections.defaultdict(list)
        for u, v in connections:
            adj_list[v].append(u)
            adj_list[u].append(v)

        num_connected_components = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                stack = [node]
                num_connected_components += 1
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        visited.add(curr)
                        for child in adj_list[curr]:
                            stack.append(child)

        return num_connected_components - 1

    # Method 3 : Using Union Find algorithm
    def makeConnectedUsingUnionFind(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        dsu = DisjointSetUnion(n)
        for connection in connections:
            u, v = connection
            dsu.union(u, v)

        # count number of connected components by counting distinct val
        connected_components = set()
        for node in range(n):
            component = dsu.find(node)  # find the set number it belones to
            connected_components.add(component)

        return len(connected_components) - 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_makeConnected(self) -> None:
        sol = Solution()
        for n, connections, solution in (
            [4, [[0, 1], [0, 2], [1, 2]], 1],
            [6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]], 2],
            [6, [[0, 1], [0, 2], [0, 3], [1, 2]], -1],
            [5, [[0, 1], [0, 2], [3, 4], [2, 3]], 0],
        ):
            self.assertEqual(
                solution,
                sol.makeConnectedUsingDFS(n, connections),
                "Should determine the minimum number of times you need to do this in order to make all the computers connected",
            )
            self.assertEqual(
                solution,
                sol.makeConnectedUsingSCC(n, connections),
                "Should determine the minimum number of times you need to do this in order to make all the computers connected",
            )
            self.assertEqual(
                solution,
                sol.makeConnectedUsingUnionFind(n, connections),
                "Should determine the minimum number of times you need to do this in order to make all the computers connected",
            )


# main
if __name__ == "__main__":
    unittest.main()
