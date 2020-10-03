#
# Time : O(V + E); Space: O(V)
# @tag : Graph
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
# Kahn's Algorithm - Solution Explanation
# **************************************************************************
# Refer to Kahns_Algorithm_Solution_Explanation.md.
# **************************************************************************
#
from typing import List
from collections import defaultdict

import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype:bool
        """
        if not prerequisites:
            return True

        L = []

        in_degrees = defaultdict(int)
        graph = defaultdict(list)
        # Construct the graph
        for u, v in prerequisites:
            graph[v].append(u)
            in_degrees[u] += 1

        Q = [u for u in graph if in_degrees[u] == 0]

        while Q:  # while Q is not empty
            start = Q.pop()  # remove a node from Q
            L.append(start)  # add n to tail of L
            for v in graph[start]:  # for each node v with a edge e
                in_degrees[v] -= 1  # remove edge
                if in_degrees[v] == 0:
                    Q.append(v)
        # check there exist a cycle
        for u in in_degrees:  # if graph has edge
            if in_degrees[u]:
                return False
                # print(f"L: {L}")
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
