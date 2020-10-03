## LeetCode - Problem 787 - Cheapest Flights Within K Stops

There are `n` cities connected by `m` flights. Each flight starts from city `u` and arrives at `v` with a price `w`.

Now given all the cities and flights, together with starting city `src` and the destination `dst`, your task is to find the cheapest price from `src` to `dst` with up to `k` stops. If there is no such route, output -1.

### Examples:

#### Example 1:
____
```
Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:
```

> ![Example - 1](Example_1.png)
>

```
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, 
as marked red in the picture.
```
____
#### Example 2:
____
```
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:
```

> ![Example - 2](Example_2.png)
>

```
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, 
as marked blue in the picture.
```
____

### Algorithm:

**Explanation:**

Apparently, It is based on Dijkstra's algorithm. However, since we have an **extra depth constraint**, we are going to **keep the paths** in the queue and **skip using a hashtable** such that we can consider all other possible paths.

**The Trickiest Part 1**

Why the first item found to the destination has the least cost???

Consider an example,

```
n=4
flights = [[0,1,10],[0,2,20],[1,3,100],[2,3,1]]
src = 0
dst = 3
K = 1
```

**You may worry that the result will be 110**, but actually it doesn't, let's see the reason.

Let's go through the iterations of `for pq.Len() > 0`,

```
after 1st iteration: pq will have [10, 20], 10 is 0->1, 20 is 0->2
after 2nd iteration: pq will have [20, 110], 20 is 0->2, 110 is 0->1->3(arrived destination but it is not prioritized due to its high cost)
after 3rd iteration: pq will have [21, 110], 21 is 0->2->3, 110 is 0->1->3
after 4th iteration: since 21 has arrived the destination, we return it as a result
```

**The Trickiest Part 2**

**Why dont we use a hastable** to avoid visiting a node again, like the original Dijkstra's Algorithm?

Let's consider a test case

```
n=4
flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src = 0
dst = 3
K = 1
```

According to the original Dijkstra's Algorithm, if we use a hashtable to fix the point as a route member and never visit again, **we will end up missing other paths which have less steps to the destination**.

Let's go through the iterations,

```
after 1st iteration: pq will have [1, 5], 1 is 0->1, 5 is 0->2
after 2nd iteration: pq will have [2, 5], 2 is 0->1->2, 5 is 0->2 (u see, here we have 2 paths to point2. if we set the 2(0->1->2) in the hashtable and never visit 2 again, we will miss the 5(0->2) which later reaches to the destination)
after 3rd iteration: pq will have [5], 5 is 0->2, we popped 2 and do nothing because its steps-1 == K
after 4th iteration: pq will have [6], 6 is 0->2->3, since 6 has arrived the destination, we return it as a result
```

### Algorithm:

Python implementation details:

Give my explanation above. In python, **I want to show you the nuance** how the original Dijkstra's Algorithm can be modified for this question. **I deliberately leave the commented-out lines** which we usually do in the traditional Dijkstra's Algorithm.

Time complexity : O(|E| log |V|)
Space complexity: O(|E|)

where: 
 - E : # of flights ( argument - flights )
 - V : # of cities  ( argument - n )

```python
from typing import List
import heapq

class Solution:
    def findCheapestPriceUsingDijkstraAlgorithm(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """
        Depth-limied Dijkstra's Algorithm
        """
        route = [[] for _ in range(n)]
        for i, j, k in flights: route[i].append((j, k))

        # dijkstra's
        heap = [(0, src, K)]
        # seen = {}
        while heap:
            cost, i, k = heapq.heappop(heap)
        
            # if i in seen and cost <= seen[i]:
            #     continue
            # seen[i] = cost

            if i == dst: return cost
            if k < 0: continue
            for j, price in route[i]:
                # if j not in seen:
                heapq.heappush(heap, (cost+price, j, k-1))
        # if dst in seen:
        #     return seen[dst]
        return -1

```
