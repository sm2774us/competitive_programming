#
# Time : O(|E| log |V|); Space: O(|E|)
# using Dijkstra Algorithm
# where, V = number of vertices
# @tag : Graph ; Dikstra
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 743: Network Delay Time
#
# Description:
#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
# v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
# If it is impossible, return -1.
#
# **************************************************************************
# Examples
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# Note:
#
#   1. N will be in the range [1, 100].
#   2. K will be in the range [1, N].
#   3. The length of times will be in the range [1, 6000].
#   4. All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
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
import heapq
import math

import unittest


class Solution:
    # In an interview - always choose Dijkstra since it is the faster algorithm of the two Shortest Path Algorithms [ i.e., Bellmand Ford and Dikstra ]

    def networkDelayTimeUsingDijkstraAlgorithm(
        self, times: List[List[int]], N: int, K: int
    ) -> int:
        graph = collections.defaultdict(dict)

        for frm, to, cost in times:
            graph[frm][to] = cost

        distances = {i: math.inf for i in range(1, N + 1)}
        distances[K] = 0
        min_dist = [(0, K)]
        visited = set()

        while min_dist:

            cur_dist, cur = heapq.heappop(min_dist)
            if cur in visited:
                continue
            visited.add(cur)

            for neighbor in graph[cur]:
                if neighbor in visited:
                    continue
                this_dist = cur_dist + graph[cur][neighbor]
                if this_dist < distances[neighbor]:
                    distances[neighbor] = this_dist
                    heapq.heappush(min_dist, (this_dist, neighbor))

        if len(visited) != len(distances):
            return -1
        return distances[max(distances, key=distances.get)]

    #  Time Complexity: O(VE)
    def networkDelayTimeUsingBellmanFordAlgorithm(
        self, times: List[List[int]], N: int, K: int
    ) -> int:
        """Bellman Ford algorithm"""
        dp = [0] + [math.inf] * N
        dp[K] = 0
        for _ in range(N):
            for u, v, w in times:
                if dp[u] != float("inf") and dp[u] + w < dp[v]:
                    dp[v] = dp[u] + w
        res = max(dp or [0])
        return -1 if res == float("inf") else res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTheCity(self) -> None:
        sol = Solution()
        self.assertEqual(
            2,
            sol.networkDelayTimeUsingDijkstraAlgorithm(
                [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
            ),
        )
        self.assertEqual(
            2,
            sol.networkDelayTimeUsingBellmanFordAlgorithm(
                [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
            ),
        )


# main
if __name__ == "__main__":
    unittest.main()
