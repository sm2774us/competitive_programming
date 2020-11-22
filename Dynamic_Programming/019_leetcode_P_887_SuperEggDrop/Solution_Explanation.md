## LeetCode - Problem 887 - Super Egg Drop

You are given `K` eggs, and you have access to a building with N floors from `1` to `N`. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor `F` with `0 <= F <= N` such that any egg dropped 
at a floor higher than `F` will break, and any egg dropped at or below floor `F` 
will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from 
any floor `X` (with `1 <= X <= N`). 

Your goal is to know **with certainty** what the value of `F` is.

What is the minimum number of moves that you need to know 
with certainty what `F` is, regardless of the initial value of `F` ?

#### Examples

**Example 1:**

```
Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
```

**Example 2:**

```
Input: K = 2, N = 6
Output: 3
Example 3:
```

**Example 3:**

```
Input: K = 3, N = 14
Output: 4
```

**Note:**

* `1 <= K <= 100`
* `1 <= N <= 10000`


#### Basic idea

First of all, we can see to get the answer of larger floors and eggs, 
results of smaller cases are useful for analysis, which leads to 
dynamic programming.

Next, how to define a state for each drop of getting the optimal floor ? 
Here we have two variables:

* The number of eggs left to throw `i`, (0 <= i <= K)
* The number of floors left to test `j`, (1 <= j <= N)

The answer (smallest times to get the optimal floor) can be the value 
of each dp state.

Therefore, we define `dp[i][j]` as smallest number of drop to get the 
optimal floor with `i` eggs and `j` floors left.

#### DP formula
For the implementation of dp, we need two information:
* base case
* recursive relation

Base case is rather intuitive to come up with. 
Think of cases with smaller eggs and floors:

```
dp[1][j] = j, j = 1...N # one egg, check each floor from 1 to j
dp[i][0] = 0, i = 1...K # no floor, no drop needed to get the optimal floor
dp[i][1] = 1, i = 1...K # one floor, only check once
```

To get recursive relation, let's consider a test case: 3 eggs and 100 floors.
For the next drop, I can choose floor from 1 to 100, say I choose 25.
There are 2 possible results for this drop:
* the egg breaks, I now have 2 eggs, and the floor to choose becomes 1~24.
* the egg remains safe, I still have 3 eggs, and the floor to choose becomes 26~100.

Think of the worst case senerio and use the dp definition above, 
we can describe the situation of getting the optical floor with choosing floor 25 
for the next drop as:
`dp[3][100] = 1 + max(dp[2][24], dp[3][75])`

Besides floor 25, in term of next drop, we can also choose floor from 1 to 100. 
Each drop would be similar to the case of 25 above. The final result 
would be the minimum of all possible choices of next floors to drop:

`dp[3][100] = min(..., 1 + max(dp[2][23], dp[3][76]), 1 + max(dp[2][24], dp[3][75]), 1 + max(dp[2][25], dp[3][74]), ...)` (take floor 24, 25, 26 as example)

To generalize the above example, the dp formula would be:
`dp[i][j] = min(1 + max(dp[i-1][k-1], dp[i][j-k])), k = 1,2,...j`

##### The brute force solution

With dp formula above, the brute force solution would be O(kn^2) as below:

```python
class Solution(object):
    def superEggDrop(self, K: int, N: int) -> int:
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
        
        for i in range(2, K+1):
            for j in range(2, N+1):
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[K][N]
```

##### Optimization1: choosing k for each dp[i][j]

The brute force solution gets TLE. To optimize, we should check for the unnecessary iteration 
in the for-loops. More specifically, to get the `k` that best fits each drop, we don't need to 
go over all floors from `1` to `j`. As for a fixed `k`, `dp[i][k]` goes up as `k` increases. 
This means `dp[i-1][k-1]` will increase and `dp[i][j-k]` will decrease as `k` goes from `1` to `j`. 
The optimal value of `k` will be the middle point where the two meet. 
So to get the optimal `k` value for `dp[i][j]`, we can do a binary search for `k` 
from `1` to `j`.

This will save the third for-loop of `k` from `O(n)` to `O(logn)`. 
Total complexity is `O(knlogn)`. 
Using binary search, we can only do top down dp, as shown below:

```python
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def dfs(i, j):
            if i==1:
                return j
            if j==0:
                return 0
            if j==1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            while lo < hi:
                mid = (lo+hi)/2
                left, right = dfs(i-1, mid-1), dfs(i, j-mid)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            res = 1 + max(dfs(i-1, lo-1), dfs(i, j-lo))
            d[i, j]=res
            return res
        
        d={}
        return dfs(K, N)
```

##### Optimization2: choosing k_1...k_N for each dp[i][1...N]

To go one step further, till now, we are still finding the optimal floor `k` from `1` to `j` 
for each `dp[i][j]`. But is this really the smallest range we can narrow? 
In fact, we can see that the optimal floor `k` for each `dp[i][j]` 
increases as `j` increases. This means that once we get the optimal `k` for `dp[i][j]`, 
we can save current `k` value and start the next round of for-loop directly, 
instead of initiating `k` from `0` again. In this way, in the third for-loop, `k` will 
go from `1` to `N` only once as `j` in the second for-loop goes from `1` to `N`. 
The total time complexity will be `O(kn)`. The code is shown below:

```python
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
            
        for i in range(2, K+1):
            k = 1
            for j in range(2, N+1):
                while k < j+1 and dp[i][j-k] > dp[i-1][k-1]:
                    k += 1
                dp[i][j] = 1 + dp[i-1][k-1]
        return dp[K][N]
```

##### Optimization3: space complexity

Usually, we can save space complexity by one dimension if the recursive relation of 
dp is based the constant length of previous states. Here, the current line `dp[i]` 
is getting updated based on the current line and previous line, so we can only record 
those two lines and update them in the iteration process to 
save the space complexity by one dimension. 
Final time complexity `O(kn)`, space complexity `O(n)`. The code is shown below: 

```python
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """ 
        dp = range(N+1)
        for i in range(2, K+1):
            k = 1
            ndp = [0, 1] + [float('inf')]*(N-1)
            for j in range(2, N+1):
                while k < j+1 and ndp[j-k] > dp[k-1]:
                    k += 1
                ndp[j] = 1 + dp[k-1]
            dp = ndp
        return dp[N]
```

#### Summary
Personally, I'd recommend thinking this problem through the following logic:

1. Why dp? Under what circumstances should we use dp to solve a problem?
1. What's the base case and recursive relation to describe a state in the problem?
1. What's the dp formula based on the above analysis?
1. Implement the brute force solution.
1. Optimization: find the pattern of dp array, what iteration is unneccessary and can be saved?
1. What's the time and space complexity? Any way to save the space complexity by one dimension?