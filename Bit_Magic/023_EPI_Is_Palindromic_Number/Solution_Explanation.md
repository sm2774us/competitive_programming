## EPI - Check If A Decimal Integer is a Palindrome

A palindromic string is one which reads the same forwards and backwards, e.g.,
**"redivider"**. In this problem, you are to write a program which determines if the
decimal representation of an integer is a palindromic string. For example, your
program should return true for the inputs `0,1,7,11,121,333, and 2147447412`, 
and `false` for the inputs - `1,12,100, and 2147483647`.

Write a program that takes an integer and determines 
if that integer's representation as a decimal string is a palindrome.

Hint: It's easy to come up with a simple expression that extracts the least significant digit. 
Can you find a simple expression for the most significant digit?

#### **Solution:**

First note that if the input is negative, then its representation as a decimal
string cannot be palindromic, since it begins with a `-`.

A brute-force approach would be to convert the input to a string and then iterate
through the string, pairwise comparing digits starting from the least significant digit
and the most significant digit, and working inwards, stopping if there is a mismatch.

The time and space complexity are `O(n)`, where `n` is the number of digits in the input.

We can avoid the `O(n)` space complexity used by the string representation by
directly extracting the digits from the input. The number of digits, `n`, 
in the input's string representation is the log (base 10) of the input value, `x`. 
To be precise, ![equation](http://latex.codecogs.com/svg.latex?n%20=%20%5Cleft%20%5Clfloor%20log_1_0(x)%20%5Cright%20%5Crfloor%20&plus;%201). 
Therefore, the least significant digit is `x mod 10`, and the most significant
digit is ![equation](http://latex.codecogs.com/svg.latex?(x/10)%5E%7Bn-1%7D). 
In the program below, we iteratively compare the most and least
significant digits, and then remove them from the input. For example, if the input is
`151751`, we would compare the leading and trailing digits, `1` and `1`. 
Since these are equal, we update the value to `5175`. The leading and trailing digits are equal, 
so we update to `17`. Now the leading and trailing are unequal, so we return `false`. 
If instead the number was `157751`, the final compare would be of `7` with `7`, 
so we would return `true`.

```python
import math
import unittest

class Solution(object):

    def is_palindrome_number(self, x: int) -> bool:
        if x <= 0:
            return x == 0

        num_digits = math.floor(math.log10(x)) + 1
        msd_mask = 10 ** (num_digits - 1)
        for i in range(num_digits // 2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask  # Remove the most significant digit of x.
            x //= 10  # Remove the least significant digit of x.
            msd_mask //= 100
        return True

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_is_palindrome_number(self) -> None:
        sol = Solution()
        for x, solution in (
            [7915, False],
            [-7915, False],
            [20692, False],
            [-20692, False],
            [904196, False],
            [-904196, False],
            [14, False],
            [-14, False],
            [30, False],
            [-30, False],
            [2982623, False],
            [-2982623, False],
            [496146024, False],
            [-496146024, False],
            [413, False],
            [-413, False],
            [230, False],
            [-230, False],
            [1941, False],
            [-1941, False],
            [9, True]
        ):
            self.assertEqual(solution, sol.reverse(x))


# main
if __name__ == "__main__":
    unittest.main()
```

##### **Time Complexity:** O(n)
##### **Space Complexity:** O(1)

The time complexity is `O(n)`, and the space complexity is `O(1)`. 