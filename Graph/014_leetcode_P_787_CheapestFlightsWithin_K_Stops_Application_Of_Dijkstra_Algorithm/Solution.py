#
# Time : O(|E| log |V|); Space: O(|E|)
# using Dijkstra Algorithm
# where, V = number of vertices
# @tag : Graph ; Dikstra
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 787: Cheapest Flights Within K Stops
#
# Description:
#
# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to
# find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
# **************************************************************************
# Examples
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# Constraints:
#
#   * The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
#   * The size of flights will be in range [0, n * (n - 1) / 2].
#   * The format of each flight will be (src, dst, price).
#   * The price of each flight will be in the range [1, 10000].
#   * k is in the range of [0, n - 1].
#   * There will not be any duplicated flights or self cycles.
#
# **************************************************************************
# Source: https://leetcode.com/problems/cheapest-flights-within-k-stops/ (LeetCode - Problem 787 - Cheapest Flights Within K Stops)
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
    # In an interview - always choose Dijkstra since it is the fastest algorithm of the various Shortest Path Algorithms

    # Method 1  : DFS with pruning | Rt: 1244ms |
    # Reference : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/128217/Three-C%2B%2B-solutions-BFS-DFS-and-BF
    # | O(T): O() | O(S): O() | Rt: 1244ms |
    def findCheapestPriceUsingDFS(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        def dfs(route, k, st, end, cost, rst):
            if st == end:
                rst[0] = min(rst[0], cost)
                return
            if k < 0:
                return
            for node, price in route[st]:
                # prune
                if cost + price >= rst[0]:
                    continue
                dfs(route, k - 1, node, end, cost + price, rst)

        route = [[] for _ in range(n)]
        for i, j, k in flights:
            route[i].append((j, k))
        rst = [math.inf]
        dfs(route, K, src, dst, 0, rst)
        if rst[0] == math.inf:
            return -1
        return rst[0]

    # Method 2  : BFS | Rt: 108ms |
    # Reference : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/128217/Three-C%2B%2B-solutions-BFS-DFS-and-BF
    # | O(T): O(|E|^|V|) | O(S): O(|E|) | Rt: 108ms |
    # where - E : # of flights ( argument - flights )
    #         V : # of cities  ( argument - n )
    def findCheapestPriceUsingBFS(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        route = [[] for _ in range(n)]
        for i, j, k in flights:
            route[i].append((j, k))
        rst, q = math.inf, collections.deque([(src, 0)])
        # we need one more k time to check last round deposit
        while q and K >= -1:
            size, K = len(q), K - 1
            for _ in range(size):
                i, cost = q.popleft()
                if i == dst:
                    rst = min(rst, cost)
                    continue
                for j, price in route[i]:
                    if cost + price >= rst:
                        continue
                    q.append((j, cost + price))

        if rst == math.inf:
            return -1
        return rst

    # Method 3  : Dijkstra with Heap: Shortest Path | Rt: 88ms |
    # Reference : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
    # | O(T): O(|E| log |V|) | O(S): O(|E|) | Rt: 88ms |
    # where - E : # of flights ( argument - flights )
    #         V : # of cities  ( argument - n )
    def findCheapestPriceUsingDijkstraAlgorithm(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        """
        Depth-limied Dijkstra's Algorithm
        """
        route = [[] for _ in range(n)]
        for i, j, k in flights:
            route[i].append((j, k))

        # dijkstra's
        heap = [(0, src, K)]
        while heap:
            cost, i, k = heapq.heappop(heap)
            if i == dst:
                return cost
            if k < 0:
                continue
            for j, price in route[i]:
                heapq.heappush(heap, (cost + price, j, k - 1))
        return -1

    # Method 3  : Bellman-Ford | Rt: 152ms |
    # Reference : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115596/c%2B%2B-8-line-bellman-ford
    # | O(T): O(|E| * |V|) | O(S): O(|E|) | Rt: 152ms |
    # where - E : # of flights ( argument - flights )
    #         V : # of cities  ( argument - n )
    def findCheapestPriceUsingBellmanFordAlgorithm(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        cost = [math.inf] * n
        cost[src] = 0
        # at most travel through K edges
        for _ in range(K + 1):
            copy = cost[:]
            for i, j, p in flights:
                copy[j] = min(copy[j], cost[i] + p)
            cost = copy
        if cost[dst] == math.inf:
            return -1
        return cost[dst]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTheCity(self) -> None:
        sol = Solution()
        for n, flights, src, dst, K, solution in (
            [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200],
            [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500],
        ):
            self.assertEqual(
                solution,
                sol.findCheapestPriceUsingDFS(n, flights, src, dst, K),
                "Should return the cheapest price from src to dst with up to K stops",
            )
            self.assertEqual(
                solution,
                sol.findCheapestPriceUsingBFS(n, flights, src, dst, K),
                "Should return the cheapest price from src to dst with up to K stops",
            )
            self.assertEqual(
                solution,
                sol.findCheapestPriceUsingDijkstraAlgorithm(n, flights, src, dst, K),
                "Should return the cheapest price from src to dst with up to K stops",
            )
            self.assertEqual(
                solution,
                sol.findCheapestPriceUsingBellmanFordAlgorithm(n, flights, src, dst, K),
                "Should return the cheapest price from src to dst with up to K stops",
            )


# main
if __name__ == "__main__":
    unittest.main()
