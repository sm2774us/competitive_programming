## Geeks For Geeks : Rightmost different bit

#### **[Problem Statement](https://practice.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1) of Rightmost different bit problem.**

> Given two numbers **M** and **N**. The task is to find the position 
> of the **rightmost different** bit in the binary representation of numbers.
>
> **Example 1:**
> ----
> **Input:**
>
> `M = 11, N = 9`
>
> **Output:**
> 
> `2`
>
> **Explanation:**
>
> ```
> Binary representation of the given 
> numbers are: 1011 and 1001, 
> 2nd bit from right is different.
> ```
> ----
> **Example 2:**
> ----
> **Input:**
>
> `M = 52, N = 4`
>
> **Output:**
> 
> `5`
>
> **Explanation:**
>
> ```
> Binary representation of the given 
> numbers are: 110100 and 0100, 
> 5th-bit from right is different.
> ```
> ---
> **User Task:**
>
> The task is to complete the function **posOfRightMostDiffBit()** 
> which **takes two arguments m and n** and **returns** 
> the **position of first different bits in m and n**. 
> If both `m` and `n` are the same then return `-1` in this case.
>
> **Expected Time Complexity:** `O(max(log m, log n))`.
>
> **Expected Auxiliary Space:** `O(1)`.
>
> **Constraints:**
> * 1 <= M <= 103
> * 1 <= N <= 103

#### Solution

```
(n ^ m) & -(n ^ m)
```

#### Explanation

Let’s take n = 11 and m = 13 for example.

**11<sub>10</sub> = 1011<sub>2</sub>**

**13<sub>10</sub> = 1101<sub>2</sub>**


If we do **XOR** operation with `n` and `m`, 
we have 1 in every position that differs between the two.

**11<sub>10</sub> XOR 13<sub>10</sub> = 1011<sub>2</sub> ^ 1101<sub>2</sub> = 0110<sub>2</sub>**

Since we have a bit representation of the positions that differ, we need to find the rightmost `1`.

There is a trick to this. Given a number, `x`,
`x & -x` gives the rightmost 1 :

**x = 6 = 0110<sub>2</sub>**

**-x = -6 = 1010<sub>2</sub>**

**x & -x = 0110<sub>2</sub> & 1010<sub>2</sub> = 0010<sub>2</sub>**

So, `(n^m) & -(n^m)` is our answer.

```python
from math import log2

import unittest

class Solution(object):

    # Function to find the position of
    # rightmost set bit in 'n'
    def getRightMostSetBit(self, n: int) -> int:
        if (n == 0):
            return 0

        return int(log2(n & -n)) + 1


    # Function to find the position of
    # rightmost different bit in the
    # binary representations of 'm' and 'n'
    def posOfRightMostDiffBit(self, m: int, n: int) -> int:
        # position of rightmost different
        # bit
        return self.getRightMostSetBit(m ^ n)

    # Function to find the position of
    # rightmost different bit in the
    # binary representations of 'm' and 'n'
    # and return its value
    def valOfRightMostDiffBit(self, m: int, n: int) -> int:
        return (m^n) & -(m^n)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_posOfRightMostDiffBit(self) -> None:
        sol = Solution()
        for m, n, solution in (
            [11, 9, 2],
            [52, 4, 5]
        ):
            self.assertEqual(solution, sol.posOfRightMostDiffBit(m, n))

    def test_valOfRightMostDiffBit(self) -> None:
        sol = Solution()
        for m, n, solution in (
            [13, 11, 2],
            [23, 7, 16]
        ):
            self.assertEqual(solution, sol.valOfRightMostDiffBit(m, n))


# main
if __name__ == "__main__":
    unittest.main()
```