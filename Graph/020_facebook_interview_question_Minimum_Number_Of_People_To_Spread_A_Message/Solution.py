# Facebook | Interview Question | Minimum number of people to spread a message
#
# @tag : Graph ; Topological Sort
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Facebook | Interview Question | Minimum number of people to spread a message
#
# Description:
#
# Considering that I'ld would like to spread a promotion message across all people in twitter.
# Assuming the ideal case, if a person tweets a message, then every follower will re-tweet the message.
#
# You need to find the minimum number of people to reach out (for example, who doesn't follow anyone etc)
# so that your promotion message is spread out across entire network in twitter.
#
# Also, we need to consider loops like, if A follows B, B follows C, C follows D, D follows A (A -> B -> C -> D -> A)
# then reaching only one of them is sufficient to spread your message.
#
# Input: A 2x2 matrix like below. In this case, a follows b, b follows c, c follows a.
#
#     a b c
# a  1 1 0
# b  0 1 1
# c  1 0 1
# Output: List of people to be reached to spread out message across everyone in the network.
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/124827/Find-minimum-number-of-people-to-reach-to-spread-a-message-across-all-people-in-twitter/ (Facebook | Interview Question | Minimum number of people to spread a message)
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
# Similar Problem: https://www.youtube.com/watch?v=qz9tKlF431k
#
import collections

import unittest


class Solution:

    #     2
    #     |       4
    #     0       |
    #    / \      5
    #   1   3
    #
    # In this example 0 follows 2. so if we reach 2 then we will reach 0 and all its descendents as well.
    # So the final result will be [2,4]
    #

    def minPeopleToSpreadAMessage(self, num_people, follows):
        # in this graph we will store
        # followee -> follower relation
        graph = collections.defaultdict(set)

        # a follows b
        for a, b in follows:
            graph[b].add(a)

        def topo(node, graph, visited, result):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    topo(nei, graph, visited, result)
            result.append(node)

        visited = set([])
        result = []
        for i in range(num_people):
            if i not in visited:
                topo(i, graph, visited, result)
        result = list(reversed(result))

        def visit(node, visited, graph):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    visit(nei, visited, graph)

        visited = set([])
        start_with = []
        for r in result:
            if r not in visited:
                start_with.append(r)
                visit(r, visited, graph)

        return start_with


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minPeopleToSpreadAMessage(self) -> None:
        sol = Solution()
        follows = [(0, 2), (1, 0), (3, 0), (5, 4)]
        self.assertEqual([4, 2], sol.minPeopleToSpreadAMessage(6, follows))


# main
if __name__ == "__main__":
    unittest.main()
