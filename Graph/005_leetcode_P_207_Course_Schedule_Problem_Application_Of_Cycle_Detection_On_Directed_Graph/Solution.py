#
# Time : O(V + E); Space: O(V)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 207: Course Schedule
#
# Description:
#
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
#
# Constraints:
#
#   * The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#   * You may assume that there are no duplicate edges in the input prerequisites.
#   * 1 <= numCourses <= 10^5
#
# **************************************************************************
# Source: https://leetcode.com/problems/course-schedule/ (LeetCode - Problem 207 - Course Schedule)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List
from collections import defaultdict

import unittest


class Graph:
    def __init__(self, vertices: int) -> None:
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u: int, v: int) -> None:
        self.graph[u].append(v)

    def isCyclicUtil(self, v: int, visited: List[bool], recStack: List[bool]) -> bool:

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self) -> bool:
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses)
        for i in prerequisites:
            u = i[0]
            v = i[1]
            g.addEdge(u, v)
        if g.isCyclic():
            return False
        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canFinishAllCourses(self) -> None:
        sol = Solution()
        for numCourses, prerequisites, solution in (
            [2, [[1, 0]], True],
            [2, [[1, 0], [0, 1]], False],
        ):
            self.assertEqual(
                solution,
                sol.canFinish(numCourses, prerequisites),
                "Should return if it is possible to finish all the courses",
            )


# main
if __name__ == "__main__":
    unittest.main()
