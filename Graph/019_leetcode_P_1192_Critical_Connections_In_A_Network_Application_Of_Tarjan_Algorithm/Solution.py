#
# Time : O(E); Space: O(E)
# using Kosaraju's Algorithm
# where, V = number of vertices
# @tag : Graph ; Dikstra
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1192: Critical Connections in a Network
#
# Description:
#
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
#
# Return all critical connections in the network in any order.
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
#   * n-1 <= connections.length <= 10^5
#   * connections[i][0] != connections[i][1]
#   * There are no repeated connections.
#
# **************************************************************************
# Source: https://leetcode.com/problems/critical-connections-in-a-network/ (LeetCode - Problem 1192 - Critical Connections in a Network)
#
# **************************************************************************
# Solution Explanation ( Using DFS )
# **************************************************************************
# Refer to Solution_Explanation_Using_DFS.md.
#
# **************************************************************************
# References:
# **************************************************************************
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
#
from typing import List
import collections

import unittest


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-1] * n

        def dfs(node, depth, parent):
            if rank[node] >= 0: return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if neighbor == parent: continue
                back_depth = dfs(neighbor, depth + 1, node)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
        dfs(0, 0, -1)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_criticalConnections(self) -> None:
        sol = Solution()
        self.assertEqual([(1,3)], sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
        # Convert sol.criticalConnections(...) list of tuples to list of lists and then perform equality check
        self.assertEqual([[1,3]], [list(elem) for elem in sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])])

# main
if __name__ == "__main__":
    unittest.main()
