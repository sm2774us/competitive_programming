#
# Time : O(V+E); Space: O(E)
# using Kosaraju's Algorithm
# where, V = number of vertices
# @tag : Graph ; Dikstra
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 990: Satisfiability of Equality Equations
#
# Description:
#
# Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
#
# Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.
#
#
#
# Example 1:
#
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
# Example 2:
#
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# Example 3:
#
# Input: ["a==b","b==c","a==c"]
# Output: true
# Example 4:
#
# Input: ["a==b","b!=c","c==a"]
# Output: false
# Example 5:
#
# Input: ["c==c","b==d","x!=z"]
# Output: true
#
# Note:
#
#   1. 1 <= equations.length <= 500
#   2. equations[i].length == 4
#   3. equations[i][0] and equations[i][3] are lowercase letters
#   4. equations[i][1] is either '=' or '!'
#   5. equations[i][2] is '='
#
# **************************************************************************
# Source: https://leetcode.com/problems/satisfiability-of-equality-equations/ (LeetCode - Problem 990 - Satisfiability of Equality Equations)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Method 3: Union Find
#
# - for each equation,
#       + if it is an inquality,
#           [] then add it to 'check' (a list that we use to check the validility of the input later)
#       + else:
#           [] union the two expression
#
# After we find all connnected components, we can simply check if the lhs and rhs of each inequality in 'check' is in the same connected components.
#
# If they are, then they must be equal and therefore the inequality should not hold, so we return 'False'.
#
# **************************************************************************
# Complexity Analysis
# **************************************************************************
#   - Time  : O(N) where is the length of the input
#   - Space : O(1) since we only store 26 characters in the parent dictionary.
#
from typing import List
import collections
import string

import unittest


class Solution:
    # Method 1: DFS (coloring connect components)
    #
    # complexity analysis:
    #   - Time  : DFS is O(N^2). We do dfs number of inequalities times. In worest case, they are N inequalities ( N is length of input). The overall complexity is O(N^3).
    #   - Space : O(N).
    def equationsPossibleUsingDFSColoringConnectComponents(self, equations: List[str]) -> bool:
        graph = collections.defaultdict(set)
        for eq in equations:
            if eq[1] == "=":
                graph[eq[0]].add(eq[3])
                graph[eq[3]].add(eq[0])

        colored = {}
        def dfs(node, color):
            if node not in colored:
                colored[node] = color
                for nei in graph[node]:
                    dfs(nei, color)

        color = 0
        for node in graph:
            if node not in colored:
                dfs(node, color)
                color += 1

        for eq in equations:
            if eq[1] == "!":
                if eq[0] == eq[3]: return False
                if colored.get(eq[0], eq[0]) == colored.get(eq[3], eq[3]): return False
        return True

    # Method 2: BFS
    #
    # complexity analysis:
    #   - Time  : bfs is O(N^2). We do number of inequalities times bfs. In worst case, they are N inequalities ( N is length of input). The overall complexity is O(N^3).
    #   - Space : O(N).
    def equationsPossibleUsingBFS(self, equations: List[str]) -> bool:
        graph = collections.defaultdict(set)
        check = []
        '''
        def dfs(u, target, visited):
            if u == target: return True
            visited.add(u)
            for v in graph[u]:
                if v in visited: continue
                return dfs(v, target, visited):
        '''
        def bfs(u, target):
            Q = collections.deque([u])
            visited = set([u])
            while Q:
                u = Q.popleft()
                if u == target: return True
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        Q.append(v)
            return False

        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq.split('!=')
                check.append((a, b))
                continue
            u, v = eq.split('==')
            graph[u].add(v)
            graph[v].add(u)

        for u, v in check:
            if bfs(u, v):
                return False
        return True

    # Method 3: Union Find
    #
    # - for each equation,
    #       + if it is an inquality,
    #           [] then add it to 'check' (a list that we use to check the validility of the input later)
    #       + else:
    #           [] union the two expression
    #
    # After we find all connnected components, we can simply check if the lhs and rhs of each inequality in 'check' is in the same connected components.
    #
    # If they are, then they must be equal and therefore the inequality should not hold, so we return 'False'.
    #
    # complexity analysis:
    #   - Time  : O(N) where is the length of the input
    #   - Space : O(1) since we only store 26 characters in the parent dictionary.
    def equationsPossibleUsingUnionFind(self, equations: List[str]) -> bool:
        if not equations: return True
        parent = {i: i for i in string.ascii_lowercase}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        checks = []
        for eq in equations:
            if eq[1] == '!':
                checks.append(eq)
                continue
            union(eq[0], eq[3])

        for chk in checks:
            if find(chk[0]) == find(chk[3]):
                return False
        return True

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_equationsPossible(self) -> None:
        sol = Solution()
        for equations, solution in (
            [["a==b","b!=a"], False ],
            [["b==a","a==b"], True],
            [["a==b","b==c","a==c"], True],
            [["a==b","b!=c","c==a"], False],
            [["c==c","b==d","x!=z"], True]
        ):
            self.assertEqual(
                solution,
                sol.equationsPossibleUsingDFSColoringConnectComponents(equations),
                "Should determine if it is possible to assign integers to variable names so as to satisfy all the given equations"
            )
            self.assertEqual(
                solution,
                sol.equationsPossibleUsingBFS(equations),
                "Should determine if it is possible to assign integers to variable names so as to satisfy all the given equations"
            )
            self.assertEqual(
                solution,
                sol.equationsPossibleUsingUnionFind(equations),
                "Should determine if it is possible to assign integers to variable names so as to satisfy all the given equations"
            )


# main
if __name__ == "__main__":
    unittest.main()
