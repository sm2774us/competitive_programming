## LeetCode - Problem 207 - Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Examples:

```
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

```
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

#### Algorithm
BFS with Kahn's algorithms
> One of these algorithms, first described by [Kahn (1962)](https://en.wikipedia.org/wiki/Topological_sorting#CITEREFKahn1962), works by choosing vertices in the same order as the eventual topological sort. First, find a list of "start nodes" which have no incoming edges and insert them into a set S; at least one such node must exist in a non-empty acyclic graph. Then:
>

```
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge
while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
```

#### Implementation
Python implementation
```python
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype:bool
        """
        if not prerequisites: return True

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
                #print(f"L: {L}")
        return True
```

#### References: 
- [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting#CITEREFKahn1962)