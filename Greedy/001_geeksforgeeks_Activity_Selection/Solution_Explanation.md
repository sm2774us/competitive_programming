## GeeksForGeeks - Activity Selection

Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. An optimization problem can be solved using Greedy if the problem has the following property: At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.
If a Greedy Algorithm can solve a problem, then it generally becomes the best method to solve that problem as the Greedy algorithms are in general more efficient than other techniques like Dynamic Programming. But Greedy algorithms cannot always be applied. For example, Fractional Knapsack problem (See [this](http://www.cs.binghamton.edu/~dima/cs333/knapsack.ppt)) can be solved using Greedy, but [0-1 Knapsack](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) cannot be solved using Greedy. 

Following are some standard algorithms that are Greedy algorithms.
1) **[Kruskal’s Minimum Spanning Tree (MST)](https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/)**: In Kruskal’s algorithm, we create a MST by picking edges one by one. The Greedy Choice is to pick the smallest weight edge that doesn’t cause a cycle in the MST constructed so far.
2) **[Prim’s Minimum Spanning Tree](https://www.geeksforgeeks.org/prims-algorithm-using-priority_queue-stl/)**: In Prim’s algorithm also, we create a MST by picking edges one by one. We maintain two sets: a set of the vertices already included in MST and the set of the vertices not yet included. The Greedy Choice is to pick the smallest weight edge that connects the two sets.
3) **[Dijkstra’s Shortest Path](https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/)**: The Dijkstra’s algorithm is very similar to Prim’s algorithm. The shortest path tree is built up, edge by edge. We maintain two sets: a set of the vertices already included in the tree and the set of the vertices not yet included. The Greedy Choice is to pick the edge that connects the two sets and is on the smallest weight path from source to the set that contains not yet included vertices.
4) **[Huffman Coding](https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/)**: Huffman Coding is a loss-less compression technique. It assigns variable-length bit codes to different characters. The Greedy Choice is to assign least bit length code to the most frequent character.

The greedy algorithms are sometimes also used to get an approximation for Hard optimization problems. For example, [Traveling Salesman Problem](https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/) is a NP-Hard problem. A Greedy choice for this problem is to pick the nearest unvisited city from the current city at every step. This solutions don’t always produce the best optimal solution but can be used to get an approximately optimal solution.

Let us consider the [Activity Selection problem](http://en.wikipedia.org/wiki/Activity_selection_problem) as our first example of Greedy algorithms. Following is the problem statement.

___You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.___

```
Example 1 : 
###################################
Consider the following 3 activities sorted by
by finish time.
     start[]  =  {10, 12, 20};
     finish[] =  {20, 25, 30};
A person can perform at most two activities. The 
maximum set of activities that can be executed 
is {0, 2} [ These are indexes in start[] and 
finish[] ]

Example 2 : 
###################################
Consider the following 6 activities 
sorted by by finish time.
     start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
A person can perform at most four activities. The 
maximum set of activities that can be executed 
is {0, 1, 3, 4} [ These are indexes in start[] and 
finish[] ]
```

The greedy choice is to always pick the next activity whose finish time is least among the remaining activities and the start time is more than or equal to the finish time of previously selected activity. We can sort the activities according to their finishing time so that we always consider the next activity as minimum finishing time activity.

1) Sort the activities according to their finishing time
2) Select the first activity from the sorted array and print it.
3) Do following for remaining activities in the sorted array.
…….a) If the start time of this activity is greater than or equal to the finish time of previously selected activity then select this activity and print it.

#### Implementation

In the following python implementation, it is assumed that the activities are already sorted according to their finish time.


```python
from typing import List

import unittest

# This class represents a undirected graph using adjacency list representation
class Solution:
    """The following implementation assumes that the activities
    are already sorted according to their finish time"""
    """Prints a maximum set of activities that can be done by a 
    single person, one at a time"""
    # a[]--> An array that contains start time of all activities
    # b[] --> An array that contains finish time of all activities
    def getMaxActivities(self, a: List[int], b: List[int]) -> int:
        pab = zip(a, b)
        c = 0
        curr = 0
        for x in sorted(pab, key=lambda x: x[1]):
            if curr <= x[0]:
                c += 1
                curr = x[1]
        #print(c)
        return c

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getMaxActivities(self) -> None:
        sol = Solution()
        a = [1, 3, 2, 5, 8, 5]
        b = [2, 4, 6, 7, 9, 9]
        self.assertEqual(4, sol.getMaxActivities(a, b))
        a = [1, 3, 2, 5]
        b = [2, 4, 3, 6]
        self.assertEqual(4, sol.getMaxActivities(a, b))


# main
if __name__ == "__main__":
    # sol = Solution()
    # # Driver program to test above function
    # a = [1, 3, 2, 5, 8, 5]
    # b = [2, 4, 6, 7, 9, 9]
    # sol.getMaxActivities(a, b)
    unittest.main()
```
____

#### Complexity Analysis:

- **Time Complexity:**
    
    Time Complexity : It takes O(n log n) time if input activities may not be sorted. It takes O(n) time when it is given that input activities are always sorted.