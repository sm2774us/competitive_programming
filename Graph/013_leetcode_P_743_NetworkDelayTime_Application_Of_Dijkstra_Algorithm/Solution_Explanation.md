## LeetCode - Problem 743 - Network Delay Time

There are `N` network nodes, labelled `1` to `N`.

Given `times`, a list of travel times as directed edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `K`. How long will it take for all nodes to receive the signal? If it is impossible, return `-1`.

Examples:

#### Example 1:
____
> ![Example - 1](Example_1.png)
>
____

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
```
____

Good video to visualize what's happening in Dijkstra with minimal fuss https://www.youtube.com/watch?v=pVfj6mxhdMw

[![Dijkstra Algorithm Explanation - Youtube Video](https://img.youtube.com/vi/pVfj6mxhdMw/0.jpg)](https://www.youtube.com/watch?v=pVfj6mxhdMw)

Python implementation details:

Construct adjacency list representation of a directional graph using a defaultdict of dicts
Track visited vertices in a set
Track known distances from K to all other vertices in a dict. Initialize this with a 0 to K.
Use a min_dist heapq to maintain minheap of (distance, vertex) tuples. Initialize with (0,K).
Main algorithm:

While the min_dist is not empty, pop vertices in the order of minimal cur_dist , skip visited
Visit the current vertex and check if any of its unvisited neighbors' known distances can be improved. This is the case if this_dist is less than distances[neighbor].
Update the known distances and add new shorter distances onto the min_dist min heap if above is true.
If we have not visited all of the nodes in the graph, we need to return -1 per problem statement
Our answer is the largest known distance to any node from K
There is no efficient find method in a min heap. Whenever a new shorter distance to a vertex becomes known, we push onto the min_dist heap. This will result in duplicate vertices being on the min queue. Use visited set to skip duplicates in constant time.

This approach is not very space efficient for dense graphs because we will have O(|E|) items on the min_dist queue. However, this will allow for log |E| = 2 log |V| lookups of the next minimum distance edge to process.

Time complexity: O(|E| log |E| ) = O(|E| 2 log |V|) = O(|E| log |V|)

```python

```
