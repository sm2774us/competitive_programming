## Geeks For Geeks : Longest Common Substring

Given two strings X and Y. The task is to find the length of the longest common substring.

##### Example 1:

```
Input: 
text1 = ABCDGH
text2 = ACDGHR

Output: 4
Explanation: CDGH is the longest substring present in both of the strings.
```

### Solution
Create a <ins>**D**</ins><ins>**P**</ins> (Dynamic Programming) table with `1+len(string)` for row and col. 
Your 0<sup>th</sup> row/col are initialized with 0. `dp[i][j]` tells you the length of your substring that 
is in common with both strings at `A[i-1]` and `B[j-1]`. 
We do -1 because our 0<sup>th</sup> row is an initialization row so we don't go out of bounds. 
If `A[i - 1] == B[j - 1]`, we look at the diagonal value and add 1. If it's not the same value, 
the longest substring ENDING at `A[i - 1]` and `B[j - 1]` is 0 because they are different letters so no substrings in common can end there.

We keep a `res` variable so we can know the longest substring at the end. 
Most other DP solutions look at a specific index (`dp[-1][-1]` or `dp[0][len(str)]`) but in this one 
our answer can be anywhere in the `dp`.

**Time Complexity:** O(MN)

**Space Complexity:** O(MN)

```python
class Solution(object):
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        res = 0
        R, C = len(text1), len(text2)
        dp = [[0] * (C + 1) for i in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res
```

We can improve the memory here to `O(min(M, N))` by switching the words if `len(B) > len(A)` and 
we can make our dp array 1D by just reusing the space each time we move to another row 
(versus in our orig 2D array). Note that we need to traverse each row backwards so that 
we do not erase the data from our previous row. If you don't traverse backwards, 
maybe you can keep a temp variable for the diagonal (the only one you would care about).

```python
class Solution(object):
    def longestCommonSubstringImproved(self, text1: str, text2: str) -> int:
        res = 0
        R, C = len(text1), len(text2)
        dp = [0] * (C + 1)
        for i in range(1, R + 1):
            for j in range(C, 0, -1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                res = max(res, dp[j])
            # print dp
        return res
```

If you need to find the word, remember the i and j index of your max substring length. Keep going diagnally (ie i -= 1, j -= 1) until the value is = 0 in the next ith and jth iteration.
