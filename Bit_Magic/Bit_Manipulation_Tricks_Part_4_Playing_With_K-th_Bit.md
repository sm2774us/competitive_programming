# Bit Manipulation - Tricks - Part 4

## Playing with K-th bit of a number

In this post we will discuss few related problems that operates on the k'th bit of a number.

Below problems are covered in this post -

1. [Problem 1. Turn off k’th bit in a number](#problem-1-turn-off-kth-bit-in-a-number)
1. [Problem 2. Turn on k’th bit in a number](#problem-2-turn-on-kth-bit-in-a-number)
1. [Problem 3. Check if k’th bit is set for a number](#problem 3-check-if-kth-bit-is-set-for-a-number)
1. [Problem 4. Toggle the k’th bit](#problem-4-toggle-the-kth-bit)

### Problem 1-Turn off kth bit in a number

The idea is to use bitwise `<<`, `&` and `~` operators. By using the expression `~ (1 << (k - 1))`,
we get a number which has all its bits set, except the `k'th` bit. If we do a bitwise `AND` of this expression
with `n`, i.e., `(n & ~(1 << (k - 1)))`, we get a number which has all its bits same as `n` except the
`k'th` bit which will be set to `0`.

For example, consider `n = 20` and `k = 3`.

```
00010100    &           (n = 20)
11111011                ~ (1 << (3-1))
~~~~~~~~
00010000
```

```python
# Function to turn off k'th bit in n
def turnOffKthBit(n, k):
    return n & ~(1 << (k - 1))
 
 
if __name__ == '__main__':
 
    n = 20
    k = 3
 
    print("{0} in binary is {1}".format(n, bin(n)))
    print("Turning k'th bit off..")
    n = turnOffKthBit(n, k)
    print("{0} in binary is {1}".format(n, bin(n)))
```
**Output:**
```
20 in binary is 0b10100
Turning k'th bit off..
16 in binary is 0b10000
```

### Problem 2-Turn on kth bit in a number

The idea is to use bitwise `<<` and `|` operators. By using the expression `(1 << (k - 1))`,
we get a number which has all its bits 0, except the `k'th` bit. If we do a bitwise `OR` of this expression
with `n`, i.e., `(n | (1 << (k - 1)))`, we get a number which has all its bits same as `n` except the
`k'th` bit which will be set to `1`.

For example, consider `n = 20` and `k = 4`.

```
00010100    |           (n = 20)
00001000                (1 << (4 - 1))
~~~~~~~~
00011100
```

```python
# Function to turn on k'th bit in n
def turnOnKthBit(n, k):
    return n | (1 << (k - 1))
 
 
if __name__ == '__main__':
 
    n = 20
    k = 4
 
    print("{0} in binary is {1}".format(n, bin(n)))
    print("Turning k'th bit on..")
    n = turnOnKthBit(n, k)
    print("{0} in binary is {1}".format(n, bin(n)))
```
**Output:**
```
20 in binary is 0b10100
Turning k'th bit off..
28 in binary is 0b11100
```

### Problem 3-Check if kth bit is set for a number

The idea is to use bitwise `<<` and `&` operators. By using the expression `(1 << (k - 1))`,
we get a number which has all its bits 0, except the `k'th` bit. If we do a bitwise `AND` of this expression
with `n`, i.e., `(n & (1 << (k - 1)))`, any non-zero value means that its k-th bit is set.

For example, consider `n = 20` and `k = 3`.

```
00010100    &           (n = 20)
00000100                (1 << (3-1))
~~~~~~~~
00000100                non-zero value
```

```python
# Function to check if k'th bit is set for n or not
def isKthBitset(n, k):
    return n & (1 << (k - 1))
 
 
if __name__ == '__main__':
 
    n = 20
    k = 3
 
    print("{0} in binary is {1}".format(n, bin(n)))
 
    if isKthBitset(n, k):
        print("k-th bit is set")
    else:
        print("k-th bit is not set")
```
**Output**
```
20 in binary is 0b10100
k-th bit is set
```

### Problem 4-Toggle the kth bit

The idea is to use bitwise '^' and `<<` operators. By using the expression `(1 << (k - 1))`,
we get a number which has all its bits 0, except the `k'th` bit. If we do a bitwise `XOR` of this expression
with `n`, i.e., `(n ^  (1 << k))`, we can easily toggle its `k-th` bit as `(0 ^ 1 = 1)` and `(1 ^ 1 = 0)`.

For example, consider `n = 20` and `k = 3`.

```
00010100    &           (n = 20)
00000100                (1 << (3-1))
~~~~~~~~
00000100                non-zero value
```

```python
# Function to toggle k'th bit of n
def toggleKthBit(n, k):
    return n ^ (1 << (k - 1))
 
 
if __name__ == '__main__':
 
    n = 20
    k = 3
 
    print("{0} in binary is {1}".format(n, bin(n)))
    print("Toggling k'th bit of n...")
    n = toggleKthBit(n, k)
 
    print("{0} in binary is {1}".format(n, bin(n)))
```
**Output**
```
20 in binary is 0b10100
Toggling k'th bit of n...
16 in binary is 0b10000
```
