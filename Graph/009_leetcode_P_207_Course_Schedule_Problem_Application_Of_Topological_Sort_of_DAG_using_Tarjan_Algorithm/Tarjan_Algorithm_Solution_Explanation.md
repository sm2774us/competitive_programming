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
DFS with Tarjan Algorithm
> An alternative algorithm for topological sorting is based on [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search). The algorithm loops through each node of the graph, in an arbitrary order, initiating a depth-first search that terminates when it hits any node that has already been visited since the beginning of the topological sort or the node has no outgoing edges (i.e. a leaf node):
>

```
L ← Empty list that will contain the sorted nodes
while there are unmarked nodes do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop   (not a DAG)
    mark n temporarily
    for each node m with an edge from n to m do
        visit(m)
    mark n permanently
    add n to head of L
```

#### Implementation
Python implementation
```python
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype:bool
        """
        # base case 
        if numCourses == None or prerequisites == None:  return None

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
```

#### References: 
- [Tarjan Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)