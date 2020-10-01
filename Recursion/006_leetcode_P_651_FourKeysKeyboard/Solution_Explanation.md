## Leetcode - Problem 651 - 4 Keys Keyboard

### Main idea:
______

There are four operations:

Key 1: (A): Print'A' on the screen

Key 2: (Ctrl-A): select all

Key 3: (Ctrl-C): Copy the selected content to the buffer

Key 4: (Ctrl-V): Paste the contents of the buffer on the screen

Given the number of operations N, find the maximum number of characters that can be printed.
______

### Problem-solving ideas:

Dynamic Programming (Dynamic Programming)

`dp[z][y]` represents the maximum number of characters printed on the screen when the number of characters in the buffer is `y` using `z` operations

Initial `dp[0][0] = 0`

State transition equation:

```
When the character A is pressed:

dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)

When pressing Ctrl-V:

dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)

When pressing Ctrl-A + Ctrl-C:

dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
```
______

### Implementation

```python
import collections

class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = collections.defaultdict(lambda : collections.defaultdict(int))
        dp[0][0] = 0 #step, buffer
        for z in range(N):
            for y in dp[z]:
                #Key 1: (A):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)
                #Key 4: (Ctrl-V):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)
                #Key 2: (Ctrl-A): + Key 3: (Ctrl-C):
                dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
        return max(dp[N].values())
```