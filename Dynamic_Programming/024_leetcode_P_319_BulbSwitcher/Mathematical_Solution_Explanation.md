Firstly, the solution is a one-liner:

```python
import math

def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
```

But here is why this works:

A lightbulb is switched everytime a number divides it. Thus a lightbulb is switched on exactly if its number of divisors (that is the count of numbers that divide it) is odd.

Each number can be decomposed in its prime factors like so:

![equation](http://latex.codecogs.com/svg.latex?n%20=%20p_%7B1%7D%5E%7Bv1%7Dp_%7B2%7D%5E%7Bv2%7D...p_%7Bk%7D%5E%7Bvk%7D)

Then the number of divisors is exactly:

![equation](http://latex.codecogs.com/svg.latex?d%28n%29%20=%20%28v_%7B1%7D&plus;1%29%28v_%7B2%7D&plus;1%29...%28v%7Bk%7D&plus;1%29,)

This is because for each prime factor we can use it up to \nu times or not use it at all (thus the +1).

Therefore, the only way that a number can have an odd number of divisors is if all of its prime factor powers are even (which means they are divisible by two) and thus it can only happen if n is a square number. Thus, only square number lightbulbs are turned on and all others are turned off.