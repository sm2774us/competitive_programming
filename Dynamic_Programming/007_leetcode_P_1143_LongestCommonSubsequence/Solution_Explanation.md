## LeetCode - Problem 1143 - Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
___

### Q & A:

Q1: What is the difference between `[[0] * m * n]` and `[[0] * m for _ in range(n)]`?  Why does the former update all the rows of that column when I try to update one particular cell ?

A1: `[[0] * m * n]` creates `n` references to the exactly same list object: `[0] * m`; In contrast: `[[0] * m for _ in range(n)]` creates `n` different list objects that have same value of `[0] * m`.

### End of Q & A
___

### Examples

##### Example 1:

```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```

##### Example 2:

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

##### Example 3:

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

### Why might we want to solve the longest common subsequence problem?

> File comparison. The Unix program "diff" is used to compare two different versions of the same file, to determine what changes have been made to the file. It works by finding a longest common subsequence of the lines of the two files; any line in the subsequence has not been changed, so what it displays is the remaining set of lines that have changed. In this instance of the problem we should think of each line of a file as being a single complicated character in a string.

### Solution

##### 1. Recursive Solution
```python
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        return self.helper(s1, s2, 0, 0)
        
    def helper(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0
        if s1[i] == s2[j]:
            return 1 + self.helper(s1, s2, i + 1, j + 1)
        else:
            return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j + 1))
```

If the two strings have no matching characters, so the last line always gets executed, the the time bounds are binomial coefficients, which (if m=n) are close to 2^n.
```
                            lcs("AXYT", "AYZX")
                           /              \
             lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
             /        \                      /              \ 
    lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")
```

##### 2. Recursive solution with Memoization

```python
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )
        return memo[i][j]
```
Time analysis: each call to subproblem takes constant time. We call it once from the main routine, and at most twice every time we fill in an entry of array L. There are (m+1)(n+1) entries, so the total number of calls is at most 2(m+1)(n+1)+1 and the time is O(mn).

As usual, this is a worst case analysis. The time might sometimes better, if not all array entries get filled out. For instance if the two strings match exactly, we'll only fill in diagonal entries and the algorithm will be fast.

##### 3. Bottom up dynamic programming

We can view the code above as just being a slightly smarter way of doing the original recursive algorithm, saving work by not repeating subproblem computations. But it can also be thought of as a way of computing the entries in the array L. The recursive algorithm controls what order we fill them in, but we'd get the same results if we filled them in in some other order. We might as well use something simpler, like a nested loop, that visits the array systematically. The only thing we have to worry about is that when we fill in a cell L[i,j], we need to already know the values it depends on, namely in this case L[i+1,j], L[i,j+1], and L[i+1,j+1]. For this reason we'll traverse the array backwards, from the last row working up to the first and from the last column working up to the first.

```python
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if s1[row - 1] == s2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        return memo[m][n]
```

Advantages of this method include the fact that iteration is usually faster than recursion, we save three if statements per iteration since we don't need to test whether L[i,j], L[i+1,j], and L[i,j+1] have already been computed (we know in advance that the answers will be no, yes, and yes). One disadvantage over memoizing is that this fills in the entire array even when it might be possible to solve the problem by looking at only a fraction of the array's cells.

Time complexity: O(mn) and Space complexity: O(mn)

##### 4. DP with Reduced space complexity

One disadvantage of the dynamic programming methods we've described, compared to the original recursion, is that they use a lot of space: O(mn) for the array L (the recursion only uses O(n+m)). But the iterative version can be easily modified to use less space -- the observation is that once we've computed row i of array L, we no longer need the values in row i+1.
This takes roughly the same amount of time as before, O(mn) -- it uses a little more time to copy X into Y but this only increases the time by a constant (and can be avoided with some more care). The space is either O(m) or O(n), whichever is smaller (switch the two strings if necessary so there are more rows than columns). Unfortunately, this solution does not leave you with enough information to find the subsequence itself, just its length.

```python
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        if m < n:
            return self.longestCommonSubsequence(s2, s1)
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]
    
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
                else:
                    memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])
    
        return memo[m % 2][n]
```

Time complexity: O(mn) ans Space comlexity: O(min(m, n))

### References

[ICS 161: Design and Analysis of Algorithms - Lecture notes for February 29, 1996](https://www.ics.uci.edu/~eppstein/161/960229.html)
