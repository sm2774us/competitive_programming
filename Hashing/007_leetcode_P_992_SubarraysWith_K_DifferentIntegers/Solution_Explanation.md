## LeetCode - Problem 992 - Subarrays with K Different Integers
## GeeksForGeeks - Count distinct elements in every window

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, `[1,2,3,1,2]` has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Examples:

```
Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```
_____

```
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
```

> Python solution 
> ______________________
>
> Time Complexity   : O(N) for two passes.
>
> Space Complexity  : O(K) at most K elements in the counter
>
> Improvements      : You can merge 2 for loops into one

#### Intuition:
First you may have feeling of using sliding window.
Then this idea get stuck in the middle.

This problem will be a very typical sliding window,
if it asks the number of subarrays with at most K distinct elements.

Just need one more step to reach the folloing equation:
`exactly(K) = atMost(K) - atMost(K-1)`

#### Explanation
1. Write/copy a helper function of sliding window, to get the number of subarrays with at most K distinct elements.
1. Done.

#### Complexity
Time O(N) for two passes.
Space O(K) at most K elements in the counter

Of course, you can merge 2 for loops into one, if you like.

#### Implementation 
Below is the implementation of the above approach:

```python
from typing import List

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)
    
        def subarraysWithAtMostKDistinct(self, A, K):
            import collections
            d = collections.defaultdict(int)
            left = right = 0
            no_dts = 0 # number of distinct integers
            res = 0

            while right < len(A):
                if d[A[right]] == 0:
                    no_dts += 1
                d[A[right]] += 1

                while no_dts == K+1:
                    if d[A[left]] == 1:
                        no_dts -= 1
                    d[A[left]] -= 1
                    left += 1

                if no_dts <= K:
                    # right-left+1 is the current number of at most K distinct substrings 
                    # in A[left:right+1] and ending with A[right]
                    res += right - left + 1 
                right += 1
            return res
```

#### Time Complexity :-
- If arrays are sorted : O(n + m)
- If arrays are not sorted : O(nlog(n) + mlog(m))

#### Similar LeetCode Problems involving Sliding Window Approach
- [LeetCode - Problem 1358 - Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC++Python-Easy-and-Concise)
- [LeetCode - Problem 1248 - Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- [LeetCode - Problem 1234 - Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/javacpython-sliding-window/367697)
- [LeetCode - Problem 1004 - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/javacpython-sliding-window/379427?page=3)
- [LeetCode - Problem 930 - Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/)
- [LeetCode - Problem 992 - Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/234482/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- [LeetCode - Problem 904 - Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/discuss/170740/Sliding-Window-for-K-Elements)
- [LeetCode - Problem 862 - Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque)
- [LeetCode - Problem 209 - Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123/JavaC++Python-Sliding-Window)