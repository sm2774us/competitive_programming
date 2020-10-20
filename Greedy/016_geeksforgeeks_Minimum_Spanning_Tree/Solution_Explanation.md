## GeeksForGeeks - Minimum Spanning Tree

#### Definition:
A **Spanning tree** is a subset of weighted Graph G with tree characteristics. For application, **Minimum Spanning Tree(MST)** is a spanning tree whose **sum of edge weights is as small as possible**.

#### Properties:
* Like general tree, it’s a graph with tree characteristics: acyclic and connected component with n nodes and n-1 edges.
* Graph may have several different minimum spanning tree(different structure but same weight). It’s not unique.
* In practice, Prim’s and Kruskal’s algorithms are both efficient [2]. However, With Union-Find structure, Kruskal’s algorithm runs in O(mlogm) time, which is faster than Prim’s for sparse graphs [1].

#### Application:
* network design problems
* traveling salesman

#### Implementation with an example:
* There’re mainly two algorithm to construct spanning tree given a weighted graph: Kruskal’s algorithm and Prim’s algorithm. (Please see my code in problem)

Summary:

|  | Usage | Assistance of Data Structure | Implementation | Time complexity |
| ------- | ----------- | ----- | -------- | -------- |
| Kruskal's Algorithm | Construct MST | Need 1 data structure: | Greedy Strategy: | O(mlogm) |
| | | 1) Union-Find Data Structure | Step1: | |
| | | | sort the edge by weight in an increasing order. | |
| | | | Step2: | |
| | | | We iterate sorted edge, at each step, we try | |
| | | | to merge node a and node b together and | |
| | | | calculate weight at same time if they're not | |
| | | | connected. | |
| Prim's Algorithm | Construct MST | Need 2 data structures: | Greedy Strategy: | O(m+mlogm) |
| | | 1) visited array | Step1: we can choose any arbitrary node as | |
| | | 2) priority queue | starting node with zero edge. | |
| | | | Step 2: | |
| | | | At each step, simply select the minimum | |
| | | | weighted edge and add a new node to the | |
| | | | current component until we make all the | |
| | | | nodes in the graph included in the | |
| | | | component. | |

* Both are greedy algorithm.

The below problems are related to spanning tree:
* [1135 - Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

#### Reference:
* [1]. Chapter 6, The algorithm design manual, 2nd edition

* [https://github.com/aforarup/interview/blob/master/Data%20Structures%20and%20Algorithm/Algorithm%20Books/The%20Algorithm%20Design%20Manual%20by%20Steven%20S.%20Skiena.pdf](https://github.com/aforarup/interview/blob/master/Data%20Structures%20and%20Algorithm/Algorithm%20Books/The%20Algorithm%20Design%20Manual%20by%20Steven%20S.%20Skiena.pdf)

* [2]. [Chapter 15, Competitive programmer handbook](https://github.com/abhishekgahlot/competitive-programmer-handbook-python)