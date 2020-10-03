#
# Time : O(V^3); Space: O(V^2)
# where, V = number of vertices
# @tag : Graph ; Dikstra ; Floyd-Warshall
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1334: Find the City With the Smallest Number of Neighbors at a Threshold Distance
#
# Description:
#
# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a
# bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
#
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at
# most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
#
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
#
# **************************************************************************
# Examples
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# Constraints:
#
#   * 2 <= n <= 100
#   * 1 <= edges.length <= n * (n - 1) / 2
#   * edges[i].length == 3
#   * 0 <= fromi < toi < n
#   * 1 <= weighti, distanceThreshold <= 10^4
#   * All pairs (fromi, toi) are distinct.
#
# **************************************************************************
# Source: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/ (LeetCode - Problem 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance)
#
#
from typing import List
import collections
import heapq
import math

import unittest

class Solution:
    def findTheCityUsingDijkstraAlgorithm(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def getNumberOfNeighbors(city):
            heap = [(0, city)]
            dist = {}

            while heap:
                currW, u = heapq.heappop(heap)
                if u in dist:
                    continue
                if u != city:
                    dist[u] = currW
                for v, w in graph[u]:
                    if v in dist:
                        continue
                    if currW + w <= distanceThreshold:
                        heapq.heappush(heap, (currW + w, v))
            return len(dist)

        return max([(getNumberOfNeighbors(city), city) for city in range(n)], key=lambda x: (-x[0], x[1]))[-1]

    def findTheCityUsingFloydWarshallAlgorithm(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """Floyd-Warshall algorithm"""
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for i, j, w in edges: dist[i][j] = dist[j][i] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = {sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return ans[min(ans)]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTheCity(self) -> None:
        sol = Solution()
        for n, edges, distanceThreshold, solution in (
            [4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4, 3],
            [5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2, 0]
        ):
            self.assertEqual(
                solution,
                sol.findTheCityUsingDijkstraAlgorithm(n, edges, distanceThreshold),
                "Should return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold"
            )
            self.assertEqual(
                solution,
                sol.findTheCityUsingFloydWarshallAlgorithm(n, edges, distanceThreshold),
                "Should return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold"
            )


# main
if __name__ == "__main__":
    unittest.main()
