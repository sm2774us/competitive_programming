# Shortest Path Algorithms Development Inspirations

This is a summary of how people discovered the following algorithms related to shortest path problem, both for single source and for all pairs of nodes in the graph.
We could see how algorithms are developed on foundations of previous algorithm.
This post is to help me to remember all algorthms much easier. Not by brute force, but by truly understand how people discovered them and follow their thinking patterns.

Prerequisite: you already understand all the algorithms listed here.
____

#### 1) Bellman-Ford

Video Tutorial: https://www.youtube.com/watch?v=-mOEd_3gTK0&t=785s

Intuition: If we don't know any algorithms, it's very easy for a beginner algorithm student to just come up with an idea, why don't we just do inifite rounds of relaxation of all edges until shorted distance table don't change. After this student experiment with different graph examples, several rounds of experiments, he discovered, hey, at most we'll just need V - 1 rounds of all edges relaxation to making distance table stable ( if there is no negative loop)

Why its V-1 rounds? Answer: https://www.youtube.com/watch?v=-mOEd_3gTK0&t=785s

Pros: will allow negative edge, could detect negative cycle (in which case there is no shortest path)
____

#### 2) SPFA (Shortest Past Faster Algorithm)

Now people started to think, hmm, we don't have any order of picking the next edge to relax in bellman ford. And we should enforce some orders to reduce the rounds of all edges relaxation. Heuristic is that we should start from source, relax layer by layer just like BFS, while in BFS, once node removed from queue we don't visit it again. But here in spfa, if we find a shorter path to v which has already been removed from queue, we'll add it back. Coz from it. we might have more chances to relax downstream nodes along the path.

**References:**
- https://www.geeksforgeeks.org/shortest-path-faster-algorithm/
- https://blog.csdn.net/qq_21120027/article/details/47978937 (chinese website)

#### 3) Dijkstra:

Video Tutorial: https://www.youtube.com/watch?v=uzHJXbToiIU

Then Dijkstra started to think on top of SPFA, we should select the "best" node popped from queue, with SPFA, the definition of "best" is lowest level. But with Dijskstar algorithm the "best" is defined to be the node with shortest distance from source.

cons: no negative edge in the graph

[![Dijkstra Algorithm Explanation - Youtube Video](https://img.youtube.com/vi/uzHJXbToiIU/0.jpg)](https://www.youtube.com/watch?v=uzHJXbToiIU)
____

#### 4) Floyd-Warshall Algorithm:

Video Tutorial: https://www.youtube.com/watch?v=oNI0rf2P9gE&t=99s

This is a classic dynamic programming

- Round k=0: in all the pathes where node 0 is the largest label, all min paths are found and relaxed
- Round k=1: in all the pathes where node 1 is the largest label, all min paths are found and relaxed
- Round k=2: in all the pathes where node 2 is the largest label, all min paths are found and relaxed
- ....
- Round k=n -1: in all the pathes where node n-1 is the largest label, all min paths are found and relaxed

[![Floyd-Warshal Algorithm Explanation - Youtube Video](https://img.youtube.com/vi/oNI0rf2P9gE/0.jpg)](https://www.youtube.com/watch?v=oNI0rf2P9gE)
