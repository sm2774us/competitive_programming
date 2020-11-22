## LeetCode - Problem 416 - Partition Equal Subset Sum

Given a **non-empty** array `nums` containing only **positive integers**, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

#### Examples

**Example 1:**

`
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
`

**Example 2:**

`
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
`

**Constraints:**

* 1 <= nums.length <= 200
* 1 <= nums[i] <= 100

#### Solution_1 : Dynamic Programming 0-1 Knapsack based Solution
One way is to treat problem as **0-1 knapsack** that we need to pick some of the elements that 
sum up to `target = sum(nums) / 2`. Suppose `dp[i][j]` is a boolean that indicates whether 
we can pick some of the elements from `nums[:i+1]` to sum up to a specific value `s`. 
Thus, if `dp[i][j]` is `True`, either `dp[i-1][s]` is already `True` 
(some elements from `nums[:i]` can already sum up to `s`), or `dp[i-1][s-nums[i]]` is `True` 
(some elements from `nums[:i]` plus `nums[i]` equals to `s`).

Therefore, we can have recurrence equation as:

```
dp[i][j] = dp[i-1][s] or (s >= nums[i] and dp[i-1][s-nums[i]])
```

The base case `dp[0][0]` is True and we can always pick none of elements to sum up to `0`.
And we can use rolling dp arrays to reduce dp size from `len(nums) * sum(nums)/2` to `sum(nums)/2` 
since `dp[i]` depends on `dp[i-1]` alone.

The time complexity is `O(len(nums) * sum(nums))` and Python 3 runs `~700ms`.

```python
from typing import List

import unittest


class Solution(object):

    # Solution_1 : Dynamic Programming 0-1 Knapsack based Solution
    def canPartition_DP_ZeroOneKnapsack(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1:
            return False
        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[s] or (s >= x and dp[s - x]) for s in range(target + 1)]
            if dp[target]:
                return True
        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canPartition(self) -> None:
        sol = Solution()
        for nums, solution in ([[1, 5, 11, 5], True], [[1, 2, 3, 5], False]):
            self.assertEqual(solution, sol.canPartition_DP_ZeroOneKnapsack(nums))


# main
if __name__ == "__main__":
    unittest.main()
```

#### Solution_2 : DFS + Memoization
Another solution is **DFS + Memoization**. We keep trying to reduce `nums[j]` 
from target value and see whether target value can be reduced to exactly `0`. 
And with memoization, time complexity can be limited within `O(len(nums) * sum(nums))`.
Besides we can iterate from large to small values to prune our DFS (sort takes `O(NlogN)`). 
Actually time will be much less since we can avoid checking most of `{1,..., sum(nums)}`. 
Python 3 runs `~ 50ms`.

```python
from typing import List

import unittest


class Solution(object):

    # Solution_2 : DFS + Memoization
    def canPartition_DP_Memoization(self, nums: List[int]) -> bool:
        def dfs(nums, target, cache):
            if target < 0:
                return False
            if target == 0:
                return True
            if target in cache:
                return False
            cache.add(target)
            for i, n in enumerate(nums):
                if dfs(nums[i + 1 :], target - n, cache):
                    return True
            return False

        s = sum(nums)
        if s % 2 != 0:
            return False
        return dfs(nums, s // 2, set())


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canPartition(self) -> None:
        sol = Solution()
        for nums, solution in ([[1, 5, 11, 5], True], [[1, 2, 3, 5], False]):
            self.assertEqual(solution, sol.canPartition_DP_Memoization(nums))


# main
if __name__ == "__main__":
    unittest.main()
```