### A Proof of the Concatenation Comparator's Transtivity

We use a.b to represent the concatenation of non-negative integers a and b .

#### Theorem:

Let a, b, and c be non-negative integers. If a.b > b.a and b.c > c.b , we have a.c > c.a .

#### Proof:

We use [a] to denote the length of the decimal representation of a . For example, if a = 10 , we have [a] = 2 .

Since a.b > b.a and b.c > c.b , we have

```
a * 10^[b] + b > b * 10^[a] + a
b * 10^[c] + c > c * 10^[b] + b
```

, which is equivalent to

```
a * (10^[b] - 1) > b * (10^[a] - 1)
b * (10^[c] - 1) > c * (10^[b] - 1)
```

Obviously, ```10^[a] - 1 > 0``` , ```10^[b] - 1 > 0``` , and ```10^[c] - 1 > 0``` . 
Since ```c >= 0```, according to the above inequalities, 
we know that ```b > 0``` and ```a > 0``` . 
After multiplying the above two inequalities and cancelling ```b``` 
and ```(10^[b] - 1)```, we have

```a * (10^[c] - 1) > c * (10^[a] - 1)```

This is equivalent to

```a * 10^[c] + c > c * 10^[a] + a```

, which means ```a.c > c.a```.

##### Q.E.D.

### Next, we must prove after sorting, by concatenating the array,we get the largest number.

#### Main Idea

When you have a sorted sequence _A, B, C, D_, ..., 
then _A_ must be the first part of the largest number. 

This can be proved by contradiction:
If _A_ is not the first part of the largest number, 
then the largest number would be something like 
_X....XAX....X_ (_X_ represents other numbers). 
You can obtain a number no smaller than itself 
by swapping _A_ with the number preceding it. 
You can continue this process until _A_ becomes 
the first part of the number, and this number is larger than 
"the largest number", leading to a contradiction. 
(Note that the last swap that make _A_ the first part of the number 
guarantees to increase the number, 
because the assumption "_A_ is not the first part of the largest number")