# LeetCode - Problem 371 - Sum of Two Integers

## Problem Description:

Calculate the sum of two integers ___a___ and ___b___, but you are **not allowed** to use the operator `+` and `-`.

#### **Example 1:**

> **Input:** `a = 1, b = 2`
>
> **Output:** `3`
>

#### **Example 2:**

> **Input:** `a = -2, b = 3`
>
> **Output:** `1`

#### **Basics**

Since a lot of people say they don't get how the solution is derived, 
here's an explanation.

When faced with a "perform arithmetic operation without using the operator" question, 
the chances are you will have to use bit manipulation.

The key insight is to realize that basic mathematical rules still work when using binary. 
So to solve these questions you should:

* Work out how the basic mathematical operation works step-by-step
* Replicate these operations using the basic bitwise operators `<<, >>, &, ^, |`
* In this case, we have addition. How does addition work normally (base 10/decimal) ?
* If the two digits of the number add up to less than 10, you add that digit to your sum, with no carry
* If the two digits of the number add up to 10 or more, you add the least significant digit 
  and carry the 1 to the next position.
* Now in binary, our least significant digit is always 0, so this actually makes things simpler a bit.

Let's look at an example of adding 2 + 3:

```
0 0 1 0 (2)
0 0 1 1 (3)
```

First, let's look at the rightmost bits. 0 + 1 = 1 "one" and 1 "zero", so we have 1. 
This gives us:

```
0 0 1 0 (2)
0 0 1 1 (3)
```

Now let's look at the next digit (2nd from the right. 1 + 1. Here we have to carry since we have two "ones", 
and the maximum we can have in binary is 1, just as the maximum we can have in base 10 is 10. 
So just like in regular decimal addition, we set our bit here to 0 and carry the 1 to the left. 
This gives us our final answer:

```
0 1 0 1 (5)
```

Now when we look at the final solution, all we 
are doing is repeating these steps over and over again until we have nothing left to carry.

How do we check if only one bit is 1? Use `^`.
How do we check if both bits are 1? Use `&`.

Then the final step is to work out when to terminate your addition. 
I would argue this is actually quite tricky and pushes the question above easy. 
But if you wouldn't work it out you could actually just use a loop through all of the bits.

-----

Imagine we are doing addition in binary. We can break it into 3 parts:

calculate every bit correspondingly and find what remains
if it exceeds, bring it to next bit as a carry
add remain and carry, which we can do recursively
For example,

```
7 + 5 =

0 0 1 1 1
0 0 1 0 1
----------
0 0 0 1 0 -----> remain = a xor b
0 1 0 1 0 -----> carry = (a and b) << 1
---------- -----> another addition
0 1 0 0 0
0 0 1 0 0
----------
0 1 1 0 0
```

So answer is pretty trivial, we do first 2 steps and invoke the method again using the results of previous steps as arguments.

#### **Solution**

First this problem is not intended to be so difficult, 
but a weird feature of Python makes it unnecessarily troublesome. 
I'll assume you have learned the basic ideas for adding integers 
using bit operations ( if not read the section above called **"Basics"**). 

I suggest this video:

[![Youtube Video](https://img.youtube.com/vi/qq64FrA2UXQ/0.jpg)](https://www.youtube.com/watch?v=qq64FrA2UXQ&t=848s)

This post, however, will focus on why this simple idea cannot be implemented smoothly using Python.

Let's see a java version of the solution:

```java
class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int sum = a ^ b;
            int carry = (a & b) << 1;
            a = sum;
            b = carry;
        }
        return a;
    }
}
```

The correctness of this version relies on the fact that integers have **fixed** length (32 bits) in java. 
So `carry` (or `b`) will eventually be moved out of boundary and go to 0, and you can 
get out of the while loop. 

**This is NOT the case for the Python! Python allows unlimited length of integers. 
If you try to mimic the code above, you will get to infinite loop!**

___(It is not very important but there is still a maximum integer in Python, 
although you can leftshift a bit infinitely many times).___

So what do we do? The first step is to manually bound the length of `sum` and `carry` by setting up a mask `0xFFFFFFFF`. `&` 
this mask with an (very long) integer will only keep the last 32 bits. 
Then, at each step of the loop, we `& sum` and `carry` with this mask, 
and eventually `carry` will be wiped out once it goes beyond 32 bits.

The Python code so far is

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
		    sum = (a^b) & mask
			carry = ((a&b)<<1) & mask
            a = sum
			b = carry
        
        # Warning: this return statement is not correct yet!!!
	    return a
```

BUT this is not the whole story. Although we successfully get out of the while loop, 
sadly a consequence is that the value of a also has only 32 bits. 
If it is a non-negative value then we are fine, but we will **lose information** 
if it is negative in the normal sense!

For example, for the testcase `a=-12, b=-8`. We know the finally answer is `-20`, 
and the current code will produce 32 bits `0xFFFFFFEC` which looks like `-20` in our usual sense. 
Well, Python doesn't think so! Python believes this is a large positive integer `4294967276`, 
because all the bits to the far left are 0.

So what is the true representation of `-20` in Python? I don't know the exact answer but logically 
since integers have "infinite" length, it can be thought of as `0x...FFFFFFFFFFFFFFEC` 
where there are infinitely many `F`.

At this moment, what we want to do it to convert the 32 bits sense `0xFFFFFFEC` to the infinite bits 
sense `0x...FFFFFFFFFFFFFFEC`. We can achieve this by using two's complements. First, we take the 
two's complement of `-20` in the 32 bits sense. This gives us a nice, positive `20` which is valid 
no matter how many bits we are using. Then, we take the two's complement of `20` is the infinite bits sense. 
This will produce a `-20` that Python can interpret.

Let's recall the rule for taking two's complements: **Flip all the bits, then plus one**.

So, to take the two's complement of `-20` in the 32 bits sense. We flip all the 32 bits of `0xFFFFFFEC` 
and add `1` to it. Note that here we cannot use the bit operation `~` because it will flip infinite many bits, 
not only the last 32. Instead, we `xor` it with the mask `0xFFFFFFFF`. Recall that `xor` with 1 has the same 
effect as flipping. This only flips the last 32 bits, all the 0's to the far left remains intact. 
Then we add 1 to it to finish the two's complement and produce a valid `20`

```
(0xFFFFFFEC^mask)+1 == 0x14 == 20
```

Next, we take the two's complement of 20 in the Python fashion. Now we can directly use the default bit operation

```
~20+1 == -20
```

Write these two steps in one line

```
~((0xFFFFFFEC^mask)+1)+1 == -20 == 0x...FFFFFFFFFFFFFFEC
```

Wait a minute, do you spot anything weird? We are not supposed to use `+` in the 
first place, right? Why are there two `+1`'s? 
Does it mean this method won't work? 
Hold up and let me give the **final magic** of today:

for any number `x`, we have

```
~(x+1)+1 = ~x
```

(Here the whole `(0xFFFFFFEC^mask)` is considered as `x`).

In other words, the two `+1`'s miraculously cancel each other! 
so we can simply write

```
~(0xFFFFFFEC^mask) == -20
```

To sum up, since Python allows arbitrary length for integers, 
we first use a mask `0xFFFFFFFF` to restrict the lengths. 
But then we lose information for negative numbers, 
so we use the magical formula `~(a^mask)` to convert the result 
to Python-interpretable form.

Here is the complete code

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry

        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        return a
```