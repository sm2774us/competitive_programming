## LeetCode - Problem 1497 - Check If Array Pairs Are Divisible by k
## GeeksForGeeks - Array Pair Sum Divisibility Problem

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.

Examples:

```
Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
```
_____

```
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
```
_____

```
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
```
_____

```
Example 4:

Input: arr = [-10,10], k = 2
Output: true
```
_____

```
Example 5:

Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true
```
_____

> Python solution 
> ______________________
>
> Time Complexity   : O(N)
>
> Space Complexity  : O(K)

#### Approach
Count positive remainder and cancel the other whenever locate a pair.

#### Explanation
1. Loop through input array;
1. Compute the positive remainder against `mod k`, cancel the other whenever find a pair; Otherwise, count it in;
   
   **Note:** the elements in arr can be negative, therefore in Java the remainder may be negative too;
   
   In order to get positive remainder for any element `a`, use `(a % k + k) % k;`
1. At the end , check if all elements in `cnt` are `0`.

#### Complexity
Time O(N)
Space O(K)

#### Implementation 
Below is the implementation of the above approach:

```python
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for a in arr:
            a %= k
            theOther = (k - a) % k
            if cnt[theOther] > 0:
                cnt[theOther] -= 1
            else:
                cnt[a] += 1
        return all(c == 0 for c in cnt)
```

```java
import java.util.Arrays;

public boolean canArrange(int[] arr, int k) {
    int[] cnt = new int[k];
    for (int a : arr) {
        a = (a % k + k) % k;
        int theOther = (k - a) % k;
        if (cnt[theOther] > 0) {
            --cnt[theOther];
        } else {
            ++cnt[a];
        }
    }
    return Arrays.stream(cnt).allMatch(i -> i == 0);
}
```

#### Time Complexity :-
- If arrays are sorted : O(n + m)
- If arrays are not sorted : O(nlog(n) + mlog(m))

#### Similar LeetCode Problems involving the same approach - i.e., - [ Count positive remainder and cancel the other whenever locate a pair. ]
- [LeetCode - Problem 1 - Two Sum](https://leetcode.com/problems/two-sum)
- [LeetCode - Problem 325 - Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k)
- [LeetCode - Problem 525 - Contiguous Array](https://leetcode.com/problems/contiguous-array)
- [LeetCode - Problem 1010 - Pairs of Songs With Total Durations Divisible by 60](Count positive remainder and cancel the other whenever locate a pair.)
- [LeetCode - Problem 1497 - Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/)
