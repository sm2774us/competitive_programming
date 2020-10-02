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
# Solution Hint: https://leetcode.com/problems/course-schedule/discuss/267234/python-solutions-with-Kahn's-algorithms-and-Tarjan-Algorithms
# **************************************************************************
# **************************************************************************
# Tarjan Algorithm - Solution Explanation
# **************************************************************************
# Refer to Tarjan_Algorithm_Solution_Explanation.md.
#
from typing import List

import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype:bool
        """
        # base case
        if numCourses == None or prerequisites == None:
            return None

        # Construct a directed graph from `prerequisites`.
        # initiate the graph, The nodes are `0` to `n-1`(nodes are origins)
        graph = [[] for _ in range(numCourses)]
        # there is an edge from `i` to `j` if `i` is the prerequisite of `j`.
        for x, y in prerequisites:
            graph[x].append(y)
            # hold the paint status
        # we initiate nodes which have not been visited, paint them as 0
        paint = [0 for _ in range(numCourses)]

        # if node is being visiting, paint it as -1, if we find a node painted as -1 in dfs,then there is a ring
        # if node has been visited, paint it as 1

        def dfs(i):
            # base cases
            if paint[i] == -1:  # a ring
                return False
            if paint[i] == 1:  # visited
                return True
            paint[i] = -1  # paint it as being visiting.
            for j in graph[i]:  # traverse i's neighbors
                if not dfs(j):  # if there exist a ring.
                    return False
            paint[i] = 1  # paint as visited and jump to the next.
            return True

        for i in range(numCourses):
            if not dfs(i):  # if there exist a ring.
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
