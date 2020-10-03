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