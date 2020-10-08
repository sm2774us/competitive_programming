# Facebook | Phone Interview Question | Given a directed graph remove return minimum of edges to keep all paths
#
# @tag : Graph ; Transitive Reduction
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Facebook | Phone Interview Question | Given a directed graph remove return minimum of edges to keep all paths
#
# Description:
#
# Question 1:
# Given a directed graph remove return minimum of edges to keep all paths.
#
# Example:
#
# Input: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
# Output: 3
# Explanation: Minimum number of edges is 3 (1 2, 2 3, 3 4)
#
# **************************************************************************
# Refer to Examples.md.
# **************************************************************************
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/630806/facebook-phone-transitive-reduction-factorial-trailing-zeroes (Facebook | Phone Interview Question | Given a directed graph remove return minimum of edges to keep all paths)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Steps:
#
#   - Create a directed graph which captures followee -> follower relationship
#   - Now create the topological sort for the entire graph
#   - For each unvisited node in the topological sort result, add it to the final result and then visit all the nodes in that tree
#   - The reason this works is, in the topological sort order the node that appears first is the left most node in the given connected component. So you would use that to traverse the curr node and all its children node.
#
# **************************************************************************
# References:
# **************************************************************************
# Similar Problem       : https://www.youtube.com/watch?v=qz9tKlF431k
# Transitive Reduction  : https://www.wikiwand.com/en/Transitive_reduction
#
import unittest


class Solution:
    def dfs(self, adj_map, x, start, visited, edges, redundant_edges):
        visited.add(x)

        if x in adj_map:
            for y in adj_map[x]:
                if y not in visited:
                    if start != x and (start, y) in edges:
                        redundant_edges.add((start, y))

                    a = self.dfs(
                        adj_map, y, start, set(visited), edges, redundant_edges
                    )
                    redundant_edges.update(a)

        return redundant_edges

    def transitive_reduction(self, edges):
        if len(edges) == 0:
            return 0

        edges = set([(x, y) for x, y in edges])

        adj_map = {}
        for x, y in edges:
            if x not in adj_map:
                adj_map[x] = []
            adj_map[x].append(y)

        redundant_edges = set()

        for x in adj_map:
            redundant_edges = self.dfs(adj_map, x, x, set(), edges, redundant_edges)

        return len(edges) - len(redundant_edges)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_transitive_reduction(self) -> None:
        sol = Solution()
        edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        self.assertEqual(3, sol.transitive_reduction(edges))


# main
if __name__ == "__main__":
    unittest.main()
