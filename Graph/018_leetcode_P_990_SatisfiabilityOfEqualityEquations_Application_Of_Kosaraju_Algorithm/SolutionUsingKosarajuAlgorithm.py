#
# Time : O(V+E); Space: O(E)
# where, V = number of vertices
#        E = number of edges
# @tag : Graph ; Kosaraju's Algorithm
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
# Using Kosaraju's Algorithm (https://en.wikipedia.org/wiki/Kosaraju's_algorithm).
#
from typing import List
from collections import defaultdict

import unittest


def postorder_dfs(G):
    visited = set()
    postorder = []

    def helper(u):
        visited.add(u)

        for v in G[u]:
            if v not in visited:
                helper(v)

        postorder.append(u)

    for u in set(G):
        if u not in visited:
            helper(u)

    return postorder


def reverse_graph(G):
    rev = defaultdict(set)

    for u in G.keys():
        for v in G[u]:
            rev[v].add(u)

    return rev


def kosaraju_sharir(G):
    # First phase
    # -----------

    # vertices in postorder
    postorder = postorder_dfs(G)

    # Second phase
    # ------------

    G = reverse_graph(G)

    visited = set()
    count = 0

    def dfs(u, scc):
        visited.add(u)
        scc.add(u)

        for v in G[u]:
            if v not in visited:
                dfs(v, scc)

    sccs = defaultdict(set)

    for u in reversed(postorder):
        if u not in visited:
            dfs(u, sccs[count])
            count += 1

    return sccs.values()


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        G = defaultdict(set)

        vertices = set()

        for eq in equations:
            if "==" in eq:
                x, y = eq.split("==")
                vertices.add(x)
                vertices.add(y)
                G[x].add(y)
                G[y].add(x)

        # build strongly connected components of equal numbers
        sccs = kosaraju_sharir(G)

        for x, e, _, y in equations:
            if e == "!":
                if x == y:
                    return False
                for scc in sccs:
                    # if x and y in  the same component - return false
                    if x in scc and y in scc:
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
            [["a==b", "b!=a"], False],
            [["b==a", "a==b"], True],
            [["a==b", "b==c", "a==c"], True],
            [["a==b", "b!=c", "c==a"], False],
            [["c==c", "b==d", "x!=z"], True],
        ):
            self.assertEqual(
                solution,
                sol.equationsPossible(equations),
                "Should determine if it is possible to assign integers to variable names so as to satisfy all the given equations",
            )


# main
if __name__ == "__main__":
    unittest.main()
