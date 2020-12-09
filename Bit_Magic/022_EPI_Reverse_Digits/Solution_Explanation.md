## EPI - Reverse Digits

#### **Solution:**

The brute-force approach is to convert the input to a string, and then
compute the reverse from the string by traversing it from back to front. 
For example, (1100)<sub>2</sub> is the decimal number 12, 
and the answer for (1100)<sub>2</sub> can be computed by
traversing the string "12" in reverse order.

Closer analysis shows that we can avoid having to form a string. Consider the
input 1132. The first digit of the result is 2, which we can obtain by taking the input
modulo 10. The remaining digits of the result are the reverse of `1132/10 = 113`.
Generalizing, let the input be `k`. If `k > 0`, then `k mod 10` is the **most significant digit**
of the result and the subsequent digits are the reverse of `k/10`. 
Continuing with the example, we iteratively update the result and the input as `2` and `113`, 
then `23` and `11`, then `231` and `1`, then `2311`.

For general `k`, we record its sign, solve the problem for `|k|`, 
and apply the sign to the result.

```python
import unittest

class Solution(object):

    def reverse(self, x: int) -> int:
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        return -result if x < 0 else result

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverse(self) -> None:
        sol = Solution()
        for x, solution in (
            [1683683571, 1753863861],
            [1799113645, 5463119971],
            [2138559785, 5879558312],
            [-1856396381, -1836936581],
            [1296932912, 2192396921],
            [-778610391, -193016877],
            [-1203840386, -6830483021],
            [1963072368, 8632703691],
            [-363773848, -848377363],
            [-1299988089, -9808899921],
            [388359, 953883],
            [-388359, -953883]
        ):
            self.assertEqual(solution, sol.reverse(x))


# main
if __name__ == "__main__":
    unittest.main()
```

##### **Time Complexity:** O(n)

The time complexity is `O(n)`, where `n` is the number of digits in `k`.