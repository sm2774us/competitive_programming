#
# Time  : Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply find-union algorithm.
#         The find and union operations can take atmost O(LogV) time. So overall complexity is O(ELogE + ELogV) time. The value of E can be atmost O(V2), so O(LogV) are O(LogE) same.
#         Therefore, overall time complexity is O(ElogE) or O(ElogV)
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
import unittest


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n)]
        self._ranks = [1 for _ in range(n)]

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True

        if self._ranks[root_u] < self._ranks[root_v]:
            self._parents[root_u] = root_v
        elif self._ranks[root_v] < self._ranks[root_u]:
            self._parents[root_v] = root_u
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1

        return False


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        """
        Problem formulation:
            We could formulate this problem into minimum spanning tree problem. So, our goal turn to if it's possble to construct minimum spanning tree given an undirected graph. If yes, return weight. Otherwise, return -1.

        Thought process:
            We use Kruskal's algorithm
            Step1: sorted the edges by their weight in an increasing order
            Step2: It's a greedy algorithm. We iterate the soreted edge, at each step we connected them together, and keep calculated the cost from node a node b, if they're not connected before.
            Step3: We make sure if there's only one group of connected components by checking if all the root nodes of nodes in the union-find set is the same root node. Otherwise, return -1.

        Time complexity analysis:
            For step1, because we sort the edge by their weight, it's O(mlogm)
            For step2, merge and find take O(log * n) =~O(1)
            So, toally, it should be O(mlogm)

        Note:
            1.Kruskal's algorithm is implemented using Union-Find Data Structure practically.
            2.It's greedy algorithm and proves more efficient on sparse graphs compared to Prim's algorithm

        T:O(mlogm)
        S:O(n) because we need maiting array tree when implement union-find
        """
        connections = sorted(connections, key=lambda x: x[2])
        unionfind = UnionFindSet(N)
        cost = 0
        for a, b, w in connections:
            if not unionfind.union(a - 1, b - 1):
                cost += w
        return -1 if len(set([unionfind.find(n) for n in range(N)])) != 1 else cost


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
