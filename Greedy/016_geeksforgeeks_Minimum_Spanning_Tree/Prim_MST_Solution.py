#
# Time  : O(N log N)
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Minimum Spanning Tree
#
# Description:
#
# Given a weighted, undirected and connected graph. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
#
# Input:
# The first line of input contains an integer T denoting the number of testcases. Then T test cases follow. The first line of each testcase contains two integers V (starting from 1), E denoting the number of nodes and number of edges. Then in the next line are 3*E space separated values a b w where a, b denotes an edge from a to b and w is the weight of the edge.
#
# Output:
# For each test case in a new line print the sum of weights of  the edges of the Minimum Spanning Tree formed of the graph.
#
# User task:
# Since this is a functional problem you don't have to worry about input, you just have to complete the function  spanningTree() which takes number of vertices V and the number of edges E and a graph graph as inputs and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree.
# Note: Please note that input of graph is 1-based but the adjacency matrix is 0-based.
#
# Expected Time Complexity: O(V2).
# Expected Auxiliary Space: O(V).
#
# Constraints:
# 1 <= T <= 100
# 2 <= V <= 1000
# V-1 <= E <= (V*(V-1))/2
# 1 <= a, b <= N
# 1 <= w <= 1000
# Graph is connected and doesn't contain self loops & multiple edges.
#
# Example:
# Input:
# 2
# 3 3
# 1 2 5 2 3 3 1 3 1
# 2 1
# 1 2 5
#
# Output:
# 4
# 5
#
# Example:
# Testcase 1:  Sum of weights of edges in the minimum spanning tree is 4.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1 (GeeksForGeeks - Minimum Spanning Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# 1) Kruskal's Minimum Spanning Tree Algorithm - Refer to Solution_Explanation.md
# 2) Prim's Minimum Spanning Tree Algorithm - Refer to Solution_Explanation.md
#
# **************************************************************************
# Reference:
# **************************************************************************
# https://yunrui-li.medium.com/leetcode-spanning-tree-32e9a87164e4
#
from typing import List
import collections
import heapq
import unittest


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        """
        Problem formulation:
            We could formulate this problem into minimum spanning tree problem. So, our goal turn to if it's possble to construct minimum spanning tree given an undirected graph. If yes, return weight. Otherwise, return -1.
        Thought process:
            We use Prim's algorithm
                Step 0: build the graph adjacency list.
                Step 1: we can choos any arbitrary node as starting node with zero edge. Put the pair into the priority queue. (Here, we take first node as starting node)
                Step 2: It's a greedy aglrithm. At each step, simply selects the minimum weight edge that adds a new node to the current component(tree) until we make all the nodes in the graph included in the the component. In order to do that, we need help of priority queue and visited array. One is efficiently contain nodes that can be connected to current component in a increasing order of edge's weight and another is to record if the node has be processed or not.
                    Step2-1: We add weight we selected to cost if it has not been processed.
                Step3: If there's only one connected components, return weight. Otherwise, reuturn -1.

        Time complexity analysis:
            At most, we have m times operation of insertion and extract elelemt from pq. Each node has been processed once as well as. So, time complexity is O(n + m log m)
        Note:
            1. Prim's algorithm is greedy algorithm.

        T:O(n + mlogm)
        S:O(m+n) because we use adjacency list represent graph data strucutre.
        """
        graph = collections.defaultdict(list)
        for a, b, w in connections:
            graph[a - 1].append((b - 1, w))
            graph[b - 1].append((a - 1, w))

        pq = [(0, 0)]  # (zero weight, node 0)
        visited = [False for _ in range(N)]
        cost = 0  # weight
        while len(pq) != 0:
            cur_cost, cur_node = heapq.heappop(pq)
            if visited[cur_node]:
                continue
            cost += cur_cost
            visited[cur_node] = True
            for nei_node, w in graph[cur_node]:
                if not visited[nei_node]:
                    heapq.heappush(pq, (w, nei_node))
        return -1 if sum(visited) != N else cost


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minimumCost(self) -> None:
        sol = Solution()
        for N, connections, solution in (
            [3, [[1, 2, 5], [2, 3, 3], [1, 3, 1]], 4],
            [2, [[1, 2, 5]], 5],
        ):
            self.assertEqual(solution, sol.minimumCost(N, connections))


# main
if __name__ == "__main__":
    unittest.main()
