## EPI - Compute **___x<sup>y</sup>___**

#### **Solution:**

First, assume y is nonnegative. The brute-force algorithm is to form
![equation](http://latex.codecogs.com/svg.latex?x%5E%7B2%7D%20=%20x%20*%20x), 
then ![equation](http://latex.codecogs.com/svg.latex?x%5E%7B3%7D%20=%20x%5E%7B2%7D%20*%20x), and so on. 
This approach takes `y - 1` multiplications, which is ![equation](http://latex.codecogs.com/svg.latex?O(2%5E%7Bn%7D)),
where `n` is number of bits in the integer type.

The key to efficiency is to try and get more work done with each multiplication,
thereby using fewer multiplications to accomplish the same result. 
For example, to compute ![equation](http://latex.codecogs.com/svg.latex?1.1%5E%7B21%7D), 
instead of starting with `1.1` and multiplying by `1.1 20 times`, 
we could multiply `1.1` by ![equation](http://latex.codecogs.com/svg.latex?1.1%5E%7B2%7D%20=%201.21) 
`10` times for a total of `11` multiplications (one to compute ___1.1<sup>2</sup>___, 
and `10` additional multiplications by `1.21`). 
We can do still better by computing ___1.1<sup>3</sup>___, ___1.1<sup>4</sup>___, etc.

When y is a power of 2, the approach that uses fewest multiplications is iterated
squaring, i.e., forming ![equation](http://latex.codecogs.com/svg.latex?x,x%5E%7B2%7D,(x%5E%7B2%7D)%5E%7B2%7D%20=%20x%5E%7B4%7D,(x%5E%7B4%7D)%5E%7B2%7D%20=%20x%5E%7B8%7D,...)
To develop an algorithm that works for general `y`, it is instructive to look at the binary representation of `y`, 
as well as properties of exponentiation, specifically 
![equation](http://latex.codecogs.com/svg.latex?x%5E%7By_0&plus;y_1%7D%20=%20x%5E%7By_0%7D.x%5E%7By_1%7D).

We begin with some small concrete instances, first assuming that `y` is non-negative.
For example, ![equation](http://latex.codecogs.com/svg.latex?x%5E%7B(1010)_2%7D%20=%20x%5E%7B(101)_2&plus;(101)_2%7D%20=%20x%5E%7B(101)_2%7D*x%5E%7B(101)_2%7D).
Similarly, ![equation](http://latex.codecogs.com/svg.latex?x%5E%7B(101)_2%7D%20=%20x%5E%7B(100)_2&plus;(1)_2%7D%20=%20x%5E%7B(100)_2%7D*x%20=%20x%5E%7B(10)_2%7D*x%5E%7B(10)_2%7D*x).

Generalizing, if the least significant bit of `y` is `0`, the result is ![equation](http://latex.codecogs.com/svg.latex?(x%5E%7By/2%7D)%5E%7B2%7D); 
otherwise, it is ![equation](http://latex.codecogs.com/svg.latex?x*(x%5E%7By/2%7D)%5E%7B2%7D). 
This gives us a recursive algorithmfor computing **___x<sup>y</sup>___** when **___y___** is non-negative.

The only change when `y` is negative is replacing `x` by `1/x` and `y` by `-y`. 
In the implementation below we replace the recursion with a while loop 
to avoid the overhead of function calls.

```python
import unittest

class Solution(object):

    def power(self, x: float, y: int) -> float:
        result, power = 1.0, y
        if y < 0:
            power, x = -power, 1.0 / x
        while power:
            if power & 1:
                result *= x
            x, power = x * x, power >> 1
        return result

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_power(self) -> None:
        sol = Solution()
        for x, y, solution in (
            [1.4434757236195281, 12, 81.830237516844],
            [-1.0006612108596369, -2217, -0.23098094677379155],
            [1.0002834272148748, 9522, 14.85611487317237],
            [12.742204083907403, -32, 4.287204382781865e-36],
            [-1.0000900945810876, 11333, -2.7759579506143144],
            [1.0009527767684638, 2713, 13.245432102894338],
            [-33.39859347898841, -15, -1.3934049046693264e-23],
            [-0.9995431471379314, 16560, 0.0005171321645226984],
            [1.0008047242601628, -19097, 2.130712791834006e-07],
            [26.009670142825087, -38, 1.678324406851151e-54],
            [-1.0004147889224355, 267, -1.1170884251055078],
            [0.9993534485152967, 5181, 0.035053962717426244]
        ):
            self.assertEqual(solution, sol.power(x, y))


# main
if __name__ == "__main__":
    unittest.main()
```

##### **Time Complexity:** O(n)

The number of multiplications is at most twice the index of `y's` MSB, 
implying an `O(n)` time complexity.
