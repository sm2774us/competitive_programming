Space and Runtime analysis:
-------------------------------

* Example 1:

![Example 1](Example_1.png)

```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

* Example 2:

```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

* Example 3:

```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```
