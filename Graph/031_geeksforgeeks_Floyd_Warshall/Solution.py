#
# Time : O(V^3)
# @tag : Graph ; Floyd Warshall
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Floyd Warshall
#
# Description:
#
# The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. The Graph is represented as Adjancency Matrix, and the Matrix denotes the weight of the edegs (if it exists) else INF (1e7).
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer V denoting the size of the adjacency matrix. The next V lines contain V space separated values of the matrix (graph). All input will be integer type.
#
# Output:
# For each test case output will be V*V space separated integers where the i-jth integer denote the shortest distance of ith vertex from jth vertex. For INT_MAX integers output INF.
#
# Constraints:
# 1 <= T <= 20
# 1 <= V <= 100
# 1 <= graph[][] <= 500
#
# Example:
# Input
# 2
# 2
# 0 25
# INF 0
# 3
# 0 1 43
# 1 0 6
# INF INF 0
#
# Output
# 0 25
# INF 0
# 0 1 7
# 1 0 6
# INF INF 0
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall/0 (GeeksForGeeks - Floyd Warshall)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
#
from typing import List

import unittest

# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF = 99999


class Solution:
    # Solves all pair shortest path via Floyd Warshall Algorithm
    def floydWarshall(self, graph):
        """ dist[][] will be the output matrix that will finally
            have the shortest distances between every pair of vertices """
        """ initializing the solution matrix same as input graph matrix 
        OR we can say that the initial values of shortest distances 
        are based on shortest paths considering no  
        intermediate vertices """
        # dist = list(map(lambda i: map(lambda j: j, i), graph))
        dist_tuples = list(map(tuple, graph))
        dist = [list(ele) for ele in dist_tuples]

        """ Add all vertices one by one to the set of intermediate 
         vertices. 
         ---> Before start of an iteration, we have shortest distances 
         between all pairs of vertices such that the shortest 
         distances consider only the vertices in the set  
        {0, 1, 2, .. k-1} as intermediate vertices. 
          ----> After the end of a iteration, vertex no. k is 
         added to the set of intermediate vertices and the  
        set becomes {0, 1, 2, .. k} 
        """
        for k in range(V):

            # pick all vertices as source one by one
            for i in range(V):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(V):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        self.printSolution(dist)
        return dist

    # A utility function to print the solution
    def printSolution(self, dist):
        print(
            "Following matrix shows the shortest distances between every pair of vertices"
        )
        for i in range(V):
            for j in range(V):
                if dist[i][j] == INF:
                    print("{0}".format("INF"))
                else:
                    print("{0}\t".format(dist[i][j]))
                if j == V - 1:
                    print("")


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_floydWarshall(self) -> None:
        sol = Solution()
        graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0],
        ]
        self.assertEqual(
            [[0, 5, 8, 9], [INF, 0, 3, 4], [INF, INF, 0, 1], [INF, INF, INF, 0]],
            sol.floydWarshall(graph),
        )


# main
if __name__ == "__main__":
    # Driver program to test the above program
    # Let us create the following weighted graph
    sol = Solution()
    """ 
                10 
           (0)------->(3) 
            |         /|\ 
          5 |          | 
            |          | 1 
           \|/         | 
           (1)------->(2) 
                3           
    """
    graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
    # Print the solution
    sol.floydWarshall(graph)
    unittest.main()
