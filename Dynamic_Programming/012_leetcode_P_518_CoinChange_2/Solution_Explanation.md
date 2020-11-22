## LeetCode - Problem 518 - Coin Change 2

You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

##### Example 1:

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```
##### Example 2:

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

##### Example 3:

```
Input: amount = 10, coins = [10] 
Output: 1
```

Let `dp_sum[i][j]` be a number of ways to represent amount `i` such that we use only first `j` coins. 
We initialize the first column of this table with 1, because we can say there is one way to get `amount = 0`, using first `j` coins: do not take any coins.
To find `dp_sum[i][j]` we need to look at the last coin taken, it consists of two terms:

1. `dp_sum[i][j-1]`, number of options, where we take only first `j-1` coins
1. `dp_sum[i-coins[j]][j]`, number of options, where we removed coin number `j` 
and we need to find number of options for the rest amount.

**Example:** let us consider `coins = [1,2,5]` and `amount = 5`. Then table `dp_sum` will be equal to

|             | 0 | 1 | 2 | 3 | 4 | 5 |
| ----------- | --- | --- | --- | --- | --- | --- |
| coin #0 (1) | 1 | 1 | 1 | 1 | 1 | 1 |
| coin #1 (2) | 1 | 1 | 2 | 2 | 3 | 3 |
| coin #2 (5) | 1 | 1 | 2 | 2 | 3 | 4 |

**Complexity:** 
Time and space is `O(amount * N)`, where `N` is number of different coins, because we need only `O(1)` to update each cell.

In the code I use index `i+1` instead of `i`, because we start from 1<sup>st</sup> column, not 0<sup>th</sup>.

```python
from typing import List

# Cartesian product of input iterables.
# Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
from itertools import product
import unittest


class Solution(object):

    # Dynamic Programming - Knapsack - Solution ( Using 2D Array )
    #
    # TC: O(amount*N)
    # SC: O(amount*N)
    #
    def change(
        self, amount: int, coins: List[int]
    ) -> int:
        # Using 2D array.
        N = len(coins)
        if N == 0:
            return int(N == amount)

        dp_sum = [[0] * N for _ in range(amount + 1)]
        for i in range(N):
            dp_sum[0][i] = 1

        for i, j in product(range(amount), range(N)):
        #or
        #for i in range(amount):
        #    for j in range(N):
            dp_sum[i + 1][j] = dp_sum[i + 1][j - 1]
            if i + 1 - coins[j] >= 0:
                dp_sum[i + 1][j] += dp_sum[i + 1 - coins[j]][j]

        return dp_sum[-1][-1]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_change(self) -> None:
        sol = Solution()
        for amount, coins, solution in (
            [5, [1, 2, 5], 4],
            [3, [2], 0],
            [4, [1, 2, 3], 4],
            [10, [2, 5, 3, 6], 5],
        ):
            self.assertEqual(
                solution, sol.change(amount, coins)
            )


# main
if __name__ == "__main__":
    unittest.main()
```

**Update** Space complexity can be reduced to `O(amount)`, because for every `j` we look at most one row back.

```python
from typing import List

import unittest


class Solution(object):

    # Dynamic Programming - Knapsack - Solution ( Using 1D Array )
    #
    # TC: O(amount*N)
    # SC: O(amount)
    #
    def change(
        self, amount: int, coins: List[int]
    ) -> int:
        # Using 1D array.
        N = len(coins)
        if N == 0:
            return int(N == amount)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(N):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] = dp[j] + dp[j - coins[i]]

        return dp[-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_change(self) -> None:
        sol = Solution()
        for amount, coins, solution in (
            [5, [1, 2, 5], 4],
            [3, [2], 0],
            [4, [1, 2, 3], 4],
            [10, [2, 5, 3, 6], 5],
        ):
            self.assertEqual(
                solution, sol.change(amount, coins)
            )


# main
if __name__ == "__main__":
    unittest.main()
```