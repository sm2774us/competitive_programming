## EPI - Generate Uniform Random Numbers

This problem is motivated by the following scenario. Six friends have to select
a designated driver using a single unbiased coin. The process should be fair to
everyone.

How would you implement a random number generator that generates a random
integer `i` between `a` and `b`, inclusive, given a random number generator 
that produces zero or one with equal probability ? 
All values in `[a, b]` should be equally likely.

___Hint: How would you mimic a three-sided coin with a two-sided coin ?___

#### **Solution:**

Note that it is easy to produce a random integer between `0` and ![equation](http://latex.codecogs.com/svg.latex?2%5E%7Bi%7D-1),
inclusive: concatenate `i` bits produced by the random number generator. 
For example, two calls to the random number generator will produce one of
![equation](http://latex.codecogs.com/svg.latex?(00)_2,(01)_2,(10)_2,(11)_2).
These four possible outcomes encode the four integers `0,1,2,3`, and all of them are
equally likely.

For the general case, first note that it is equivalent to produce a random integer
between `0` and `b - a`, inclusive, since we can simply add `a` to the result. 
If `b - a` is equal to ![equation](http://latex.codecogs.com/svg.latex?2%5E%7Bi%7D-1), 
for some `i`, then we can use the approach in the previous paragraph

If `b - a` is not of the form ![equation](http://latex.codecogs.com/svg.latex?2%5E%7Bi%7D-1), 
we find the smallest number of the form ![equation](http://latex.codecogs.com/svg.latex?2%5E%7Bi%7D-1) that
is greater than `b - a`. We generate an `i-bit` number as before. This `i-bit` number may or
may not lie between `0` and `b - a`, inclusive. If it is within the range, we return it — all
such numbers are equally likely. If it is not within the range, we try again with `i` new random bits. 
We keep trying until we get a number within the range.

For example, to generate a random number corresponding to a dice roll,
i.e., a number between `1` and `6`, we begin by making three calls to the ran¬
dom number generator (since ![equation](http://latex.codecogs.com/svg.latex?2%5E2%20-%201%20%3C%20(6%20-%201)%20%5Cleq%202%5E3%20-%201)).
If this yields one of ![equation](http://latex.codecogs.com/svg.latex?(000)_2,(001)_2,(010)_2,(011)_2,(100)_2,(101)_2),
we return 1 plus the corresponding value.
Observe that all six values between 1 and 6, inclusive, are equally likely to be re¬
turned. If the three calls yields one of ![equation](http://latex.codecogs.com/svg.latex?(110)_2,(111)_2),
we make three more calls. Note that the probability of having to try again is `2/8`, 
which is less than half. Since successive calls are independent, the probability that 
we require many attempts diminishes very rapidly, e.g., the probability of not getting 
a result in 10 attempts is ![equation](http://latex.codecogs.com/svg.latex?(2/8)%5E%7B10%7D) 
which is less than one-in-a-million.

```python
import random
import unittest

class Solution(object):

    def zero_one_random(self):
        return random.randrange(2)

    def uniform_random(self, lower_bound: int, upper_bound: int) -> int:

        number_of_outcomes = upper_bound - lower_bound + 1
        while True:
            result, i = 0, 0
            while (1 << i) < number_of_outcomes:
                # zero_one_random() is the provided random number generator.
                result = (result << 1) | self.zero_one_random()
                i += 1
            if result < number_of_outcomes:
                break
        return result + lower_bound

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_uniform_random(self) -> None:
        sol = Solution()
        for lower_bound, upper_bound in (
            [0, 10],
            [10, 25],
            [1, 100],
            [0, 999],
            [0, 9999],
            [999, 1000],
            [0, 1]
        ):
            self.assertTrue(lower_bound <= sol.uniform_random(lower_bound, upper_bound) <= upper_bound)


# main
if __name__ == "__main__":
    unittest.main()
```

##### **Time Complexity:** ![equation](http://latex.codecogs.com/svg.latex?O(log(b-a&plus;1)))

To analyze the time complexity, let `t = b — a + 1`. 
The probability that we succeed in the first try is ![equation](http://latex.codecogs.com/svg.latex?t/2%5E%7Bi%7D). 
Since ![equation](http://latex.codecogs.com/svg.latex?2%5E%7Bi%7D) is the smallest power of `2` 
greater than or equal to `t`, it must be less than `2t`. 
(An easy way to see this is to consider the binary representation of `t` and `2t`.) 
This implies that ![equation](http://latex.codecogs.com/svg.latex?t/2%5E%7Bi%7D%20%3E%20t/2t%20=%20(1/2)%20). 
Hence the probability that we do not succeed on the first try is ![equation](http://latex.codecogs.com/svg.latex?1%20-%20t/2%5E%7Bi%7D%20%3C%201/2). 
Since successive tries are independent, the probability that more than `k` tries 
are needed is less than or equal to ![equation](http://latex.codecogs.com/svg.latex?1/2%5E%7Bk%7D). 
Hence, the expected number of tries is not more than ![equation](http://latex.codecogs.com/svg.latex?1%20&plus;%202(1/2)%5E%7B1%7D%20&plus;%203(1/2)%5E%7B2%7D%20&plus;%20...). 
The series converges, so the number of tries is `O(1)`. 
Each try makes ![equation](http://latex.codecogs.com/svg.latex?%5Cleft%20%5Clceil%20log(b%20-%20a%20&plus;%201)%20%5Cright%20%5Crceil) 
calls to the 0/1-valued random number generator. 
Assuming the 0/1-valued random number generator takes `O(1)` time, 
the time complexity is ![equation](http://latex.codecogs.com/svg.latex?O(log(b-a&plus;1))).
 