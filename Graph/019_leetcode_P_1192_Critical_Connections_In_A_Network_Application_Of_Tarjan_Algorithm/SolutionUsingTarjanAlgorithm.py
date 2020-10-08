#
# Time : O(V+E); Space: O(E)
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
# Solution Explanation ( Using Tarjan's Algorithm )
# **************************************************************************
# Refer to Solution_Explanation_Using_Tarjan_Algorithm.md.
#
# **************************************************************************
# References:
# **************************************************************************
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/382526/Tarjan-Algorithm-(DFS)-Python-Solution-with-explanation/344457/#:~:text=In%20tarjan%20algorithm%2C%20we%20keep,neighbor%20except%20its%20direct%20parent.&text=After%20DFS%2C%20we%20find%20edge,and%20get%20the%20final%20answers.
#
#
from typing import List
import collections

import unittest


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        N = len(connections)
        lev = [None] * N
        low = [None] * N

        def dfs(node, par, level):
            # already visited
            if lev[node] is not None:
                return

            lev[node] = low[node] = level
            for nei in graph[node]:
                if not lev[nei]:
                    dfs(nei, node, level + 1)

            # minimal level in the neignbors, exclude the parent
            cur = min([level] + [low[nei] for nei in graph[node] if nei != par])
            low[node] = cur
            # print(low, lev)

        dfs(0, None, 0)

        ans = []
        for u, v in connections:
            if low[u] > lev[v] or low[v] > lev[u]:
                ans.append([u, v])
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_criticalConnections(self) -> None:
        sol = Solution()
        self.assertEqual(
            [[1, 3]], sol.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
        )


# main
if __name__ == "__main__":
    unittest.main()
