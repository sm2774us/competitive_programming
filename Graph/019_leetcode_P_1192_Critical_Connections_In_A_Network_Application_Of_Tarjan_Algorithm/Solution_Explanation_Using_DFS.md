## LeetCode - Problem 1192 - Critical Connections in a Network

There are `n` servers numbered from `0` to `n-1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a, b]` represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A ___critical connection___ is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

### Examples:

#### Example 1:

![Example - 1](Example_1.png)
```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```
____

### Algorithm:

**First thought**

Thinking for a little while, you will easily find out this theorem on a connected graph:

- An edge is a critical connection, if and only if it is not in a cycle.

So, if we know how to find cycles, and discard all edges in the cycles, then the remaining connections are a complete collection of critical connections.
____

**How to find edges in cycles, and remove them?**

We will use DFS algorithm to find cycles and decide whether or not an edge is in a cycle.

Define **rank** of a node: The depth of a node during a DFS. The starting node has a ___rank___ 0.

Only the nodes on the current DFS path have non-special ranks. In other words, only the nodes that we've started visiting, but haven't finished visiting, have ranks. So `0 <= rank < n`.

(For coding purpose, if a node is not visited yet, it has a special rank `-2`; if we've fully completed the visit of a node, it has a special rank `n`.)

**How can "rank" help us with removing cycles?** Imagine you have a current path of length `k` during a DFS. The nodes on the path has increasing ranks from `0` to `k` and incrementing by `1`. Surprisingly, your next visit finds a node that has a rank of `p` where `0 <= p < k`. Why does it happen? Aha! You found a node that is on the current search path! That means, congratulations, you found a cycle!

But only the current level of search knows it finds a cycle. How does the upper level of search knows, if you backtrack? Let's make use of the return value of DFS: **`dfs`** **function returns the minimum rank it finds**. During a step of search from node `u` to its neighbor `v`, **if** **`dfs(v)`** **returns something smaller than or equal to** **`rank(u)`**, then `u` knows its neighbor `v` helped it to find a cycle back to `u` or `u`'s ancestor. So u knows it should discard the edge `(u, v)` which is in a cycle.

After doing dfs on all nodes, all edges in cycles are discarded. So the remaining edges are critical connections.

### Implementation:

```python
from typing import List
import collections

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)      
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-1] * n

        def dfs(node, depth, parent):
            if rank[node] >= 0: return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if neighbor == parent: continue
                back_depth = dfs(neighbor, depth + 1, node)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth
        dfs(0, 0, -1)  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)

```
____
#### Notes:

If anyone was confused about what this does:

```
connections = set(map(tuple, (map(sorted, connections))))
```

this is the translation for normal humans:

```
def sortConnections(self, connections):
    sortedConnections = set()
        
    for conn in connections:
        conn.sort()
        sortedConnections.add((conn[0], conn[1]))
        
    return sortedConnections
```

- So from this: `[[0, 1], [1, 2], [2, 0], [1, 3]]` we get: `{(0, 1), (0, 2), (1, 2), (1, 3)}` which is the set of all the connections in the graph. 
- We use this in our answer since we only return one single connection per node.
- It's sorted so we can delete the tuple from the set easily, given a node and neighbor.

____
#### Complexity analysis { TC : O(|E|) ; SC : O(|E|) } :

DFS time complexity is `O(|E| + |V|)`, attempting to visit each edge at most twice. (the second attempt will immediately return.)
As the graph is always a connected graph, `|E| >= |V|`.

So, time complexity = `O(|E|)`.

Space complexity = `O(graph) + O(rank) + O(connections)` = `3 * O(|E| + |V|)` = `O(|E|)`.
____
#### FAQ: Are you reinventing Tarjan?
Honestly, I didn't know Tarjan beforehand. The idea of using rank is inspired by preordering which is a basic concept of DFS. Now I realize they are similar, but there are still major differences between them.

- This solution uses only one array rank. While Tarjan uses two arrays: dfn and low.
- This solution's min_back_depth is similar to Tarjan's low, but rank is very different than dfn. max(dfn) is always n-1, while max(rank) could be smaller than n-1.
- This solution constructs the result by removing non-critical edges during the dfs, while Tarjan constructs the result by collecting non-critical edges after the dfs.
- In this solution, only nodes actively in the current search path have 0<=rank[node]<n; while in Tarjan, nodes not actively in the current search path may still have 0<=dfn[node]<=low[node]<n.
____
#### Brain teaser
Thanks [@migfulcrum](https://leetcode.com/migfulcrum) for [pointing out](https://leetcode.com/discuss/comment/359567) that `rank[node] = n` is not necessary. He is totally right. I'll leave this as a brain teaser for you: why is it not necessary?

(Hint: after we've finished visiting a node, is it possible to have another search path attempting to visit this node again?)