# Bit Manipulation - Tricks - Part 3

## Playing with rightmost set bit of a number

In this post we will discuss few related problems that are related to
unsetting the rightmost bit of a number.

### How to unset the rightmost set bit of a number?

The expression `(n & (n - 1))` will turn off the rightmost set bit (**LSB**)
of a given number. `(n - 1)` will have all the bits flipped after the rightmost
set bit of `n` (including the rightmost set bit). So `(n & (n - 1))` will result
in last bit flipped of `n`.

Consider

```
00010100    &               (n = 20)
00010011                    (n-1 = 19)
~~~~~~~~
00010000

00...00000000       &       (n = 0, no rightmost bit - i.e., no LSB)
11...11111111               (n-1 = -1)
~~~~~~~~~~~~~
00...00000000
```

Below problems can be solved by unsetting the rightmost set bit (LSB) of a number -

1. [Problem 1. Check if given positive integer is a power of 2 without using any branching or loop.](#problem-1-check-if-given-positive-integer-is-a-power-of-2-without-using-any-branching-or-loop)

1. [Problem 2. Find position of the rightmost set bit](#problem-2-find-position-of-the-rightmost-set-bit)

1. [Problem 3. Find position of the only set bit in a number](#problem-3-find-position-of-the-only-set-bit-in-a-number)

1. [Problem 4. Computing parity of a number (Naive solution)](#problem-4-computing-parity-of-a-number-naive-solution)

#### Problem 1-Check if given positive integer is a power of 2 without using any branching or loop

As discussed above, the expression `(n & (n - 1))` will unset the rightmost set bit of a number.
If the number is power of `2`, it has only one bit set and `(n & (n - 1))` will unset the only set bit.
So we can say that `(n & (n - 1))` returns `0` if `n` is power of `2` else it is not a power of `2`.

For example:

```
00010000    &           (n = 16, only one set bit)
00001111                (n-1 = 15)
~~~~~~~~
00000000
```

```python
# returns position of the rightmost set bit of n
def isPowerOfTwo(n: int) -> bool:
    if (n == 0): return False
    return (n & (n - 1)) == 0 
  
if __name__ == '__main__':
    n = 16
    print("Is {0} a power of 2? {1}".format(n, isPowerOfTwo(n)))
    n = 0
    print("Is {0} a power of 2? {1}".format(n, isPowerOfTwo(n)))
    n = 1
    print("Is {0} a power of 2? {1}".format(n, isPowerOfTwo(n)))
``` 

#### Problem-2-Find position of the rightmost set bit

The idea to unset the rightmost bit of a number `n` and `XOR` the result with `n`.
Then the position of the rightmost set bit in `n` will be the **position of the only set bit** in the result.
Note that if `n` is odd, we can directly return `1` as first bit is always set
for odd numbers.

For example, number `20` in binary is `00010100` and position of the rightmost set bit is `3`.

```
00010100    &               (n = 20)
00010011                    (n-1 = 19)
~~~~~~~~
00010000    ^               (XOR resulting number with n)
00010100
~~~~~~~~
00000100      - rightmost set bit will tell us the position 
```

```python
# returns position of the rightmost set bit of n
def rightmostSetBitPos(n):
 
    # if number is odd, return 1
    if n & 1:
        return 1
 
    # unset rightmost bit and xor with number itself
    n = n ^ (n & (n - 1))
 
    # find the position of the only set bit in the result
    # we can directly return log2(n) + 1 from the function
    pos = 0
    while n:
        n = n >> 1
        pos = pos + 1
 
    return pos
 
 
if __name__ == '__main__':
 
    n = 20
 
    print(f"{n} in binary is", bin(n))
    print("Position of the rightmost set bit is", rightmostSetBitPos(n))
```
**Output:**
```
20 in binary is 0b10100
Position of the rightmost set bit is 3
```
---
**Alternate Solution -**

The idea is to negate `n` and perform bitwise AND operation with itself, i.e., `(n & -n)`.
Then the position of the rightmost bit in `n` will be the **position of the only set bit**
in the result. We can also use this hack for [Problem 1](problem-1-check-if-given-positive-integer-is-a-power-of-2-without-using-any-branching-or-loop).
If `(n & -n) == n`, then given positive integer is a power of 2.

For example,

```
00...0010100    &               (n = 20)
11...1101100                    (-n = -20)
~~~~~~~~~~~~
00...0000100
```

```python
from math import log2
  
# returns position of the rightmost set bit of n
def rightmostSetBitPos(n):
    if (n == 0):
        return 0

    # if number is odd, return 1
    if n & 1:
        return 1
 
    return int(log2(n & -n)) + 1
 
 
if __name__ == '__main__':
 
    n = 20
    print("Position of the rightmost set bit is", rightmostSetBitPos(n))
```
**Output:**
```
Position of the rightmost set bit is 3
```

#### Problem 3-Find position of the only set bit in a number

The idea is to unset the rightmost bit of a number `n` and check if it becomes `0` or not.
If it is non-zero, we know that there is another set bit present and we have an invalid input.
If it becomes `0`, then the position of the only set bit can be found by processing every bit 
of `n` one by one or we can directly use ___**log<sub>2</sub>(n)+1**___.

For example, number `16` in binary is `00010000` and position of the rightmost set bit is `5`.

```
00010000        &               (n = 16)
00001111                        (n-1 = 15)
~~~~~~~~
00000000

log2(16) + 1 = 5 
```

```python
from math import log2

# returns position of the only set bit of n
def setBitPos(n):

    # unset rightmost bit and check if the number is non-zero
    if (n & (n - 1)) == 1:
        print("Wrong input")
        return 1

    return int(log2(n)) + 1

if __name__ == '__main__':
 
    n = 16
 
    print(n, "in binary is", bin(n))
    print("Position of the only set bit is", setBitPos(n))
```
**Output:**
```
16 in binary is 10000
Position of the rightmost set bit is 5
```

#### Problem 4-Computing parity of a number-Naive-solution

**"Parity"** refers to the number of 1s in a given binary number. 
Odd parity(1) means there are an odd number of 1s and even parity(0)
means that there are an even number of 1s. Parity bits are often used
as a crude means of error detection as digital data is transmitted and received.

Naive solution would be to calculate parity by checking each bit of `n`
one by one. The time taken is proportional to the number of bits in the number.

```python
# find parity of number n
def findParity(n):
 
    parity = False
 
    # run till n is zero
    while n:
        # invert the parity flag
        if n & 1:
            parity = not parity
 
        # right shift n by 1 (divide by 2)
        n = n >> 1
 
    return parity
 
 
if __name__ == '__main__':
 
    n = 31
 
    print(n, "in binary is", bin(n))
 
    if findParity(n):
        print(f"Parity of {n} is odd")
    else:
        print("Parity of {n} is even")
```
**Output:**
```
31 in binary is 11111
Parity of 31 is odd
```

We can perform better by turning off the rightmost set bit of the number
one by one and count the parity. The below code uses an approach
like [Brian Kernigan's](https://www.techiedelight.com/brian-kernighans-algorithm-count-set-bits-integer/)
bit counting. The time it takes is proportional to the number of bits set.

```python
def findParity(n):
 
    parity = False
 
    # run till n is zero
    while n:
        # invert the parity flag
        parity = not parity
 
        # turn off rightmost set bit
        n = n & (n - 1)
 
    return parity
 
 
if __name__ == '__main__':
 
    n = 31
 
    print("{0} in binary is {1}".format(n, bin(n)))
 
    if findParity(n):
        print(f"Parity of {n} is odd")
    else:
        print(f"Parity of {n} is even")
```
**Output:**
```
31 in binary is 0b11111
Parity of 31 is odd
```

