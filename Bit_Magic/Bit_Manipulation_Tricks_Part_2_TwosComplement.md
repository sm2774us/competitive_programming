# Bit Manipulation - Tricks - Part 2

## Two's Complement and Binary Logarithm

### Two's Complement

**Two's complement** is a [mathematical operation](https://en.wikipedia.org/wiki/Mathematical_operation) on [binary numbers](https://en.wikipedia.org/wiki/Binary_number), 
and is an example of a [radix complement](https://en.wikipedia.org/wiki/Method_of_complements). 
It is used in [computing](https://en.wikipedia.org/wiki/Computing) as a method of [signed number representation](https://en.wikipedia.org/wiki/Signed_number_representation).

The two's complement of an N-bit number is defined as its complement with respect to 2<sup>N</sup>; 
the sum of a number and its two's complement is 2<sup>N</sup>. 
For instance, for the three-bit number `010`, the two's complement is `110`, 
because `010 + 110 = 8` which is equal to `23`. 
The two's complement is calculated by inverting the digits and adding one.

Two's complement is the most common method of representing signed [integers](https://en.wikipedia.org/wiki/Integer_(computer_science)) on computers,<sup>[\[1\]](https://en.wikipedia.org/wiki/Two%27s_complement#cite_note-1)</sup> 
and more generally, fixed point binary values. 
In this scheme, if the binary number 010<sub>2</sub> encodes the signed integer 2<sub>10</sub>, 
then its two's complement, 110<sub>2</sub>, encodes the inverse: −2<sub>10</sub>. 
In other words, to reverse the sign of most integers (all but one of them) in this scheme, 
you can take the two's complement of its binary representation.<sup>[\[2\]](https://en.wikipedia.org/wiki/Two%27s_complement#cite_note-1)</sup> 
The tables below illustrates this property.

##### Three-bit signed integers
| Decimal value	| Two's-complement representation |
| ------------- | ------------------------------- |
| 0	| 000 |
| 1 | 001 |
| 2 | 010 |
| 3 | 011 |
| −4 | 100 |
| −3 | 101 |
| −2 | 110 |
| −1 | 111 |

##### Eight-bit signed integers
| Decimal value | Two's-complement representation |
| ------------- | ------------------------------- |
| 0	| 0000 0000 |
| 1	| 0000 0001 |
| 2	| 0000 0010 |
| 126 | 0111 1110 |
| 127 | 0111 1111 |
| −128 | 1000 0000 |
| −127 | 1000 0001 |
| −126 | 1000 0010 |
| −2 | 1111 1110 |
| −1 | 1111 1111 |

### Binary Logarithm

From [Binary logarithm](https://en.wikipedia.org/wiki/Binary_logarithm) on Wikipedia:

> In mathematics, the binary logarithm (log<sub>2</sub>n) is the power to which the number 2 
> must be raised to obtain the value n. That is, for any real number x,
>
> x = log<sub>2</sub>n ⟺ 2<sup>x</sup> = n.
>
> For example, the binary logarithm of 1 is 0, the binary logarithm of 2 is 1, 
> the binary logarithm of 4 is 2, and the binary logarithm of 32 is 5.
>

##### Examples

For example, let's look at 5. In binary, 5 is bits `00000000000000000000000000000101` (assuming a 32bit `int` type), 
and -5 is bits `11111111111111111111111111111011` 
(assuming negative integers are implemented using [2s-complement](https://en.wikipedia.org/wiki/Two%27s_complement)). 
Remember that the `&` operator performs a [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operation, 
which returns a `1` for a given bit only if that bit is `1` in ___both___ input numbers, 
otherwise it returns a `0` instead. Thus:

```
  00000000000000000000000000000101 (5)
& 11111111111111111111111111111011 (-5)
----------------------------------
  00000000000000000000000000000001 (1)
```

So, `5 & -5 = 1`, then `log2(1) = 0`, and `0 + 1 = 1`.

Let's take a look at a more complex number, `1041204192`, 
which is bits `00111110000011111000001111100000`, 
and `-1041204192` is bits `11000001111100000111110000100000`:

```
  00111110000011111000001111100000 (1041204192)
& 11000001111100000111110000100000 (-1041204192)
----------------------------------
  00000000000000000000000000100000 (32)
```

So `1041204192 & -1041204192 = 32`, then `log2(32) = 5`, and `5 + 1 = 6`.

Just for kicks, lets look at `0`:

```
  00000000000000000000000000000000 (0)
& 00000000000000000000000000000000 (-0)
----------------------------------
  00000000000000000000000000000000 (0)
```

So `0 & -0 = 0`, and `log2(0)` is `-INFINITY` which is **undefined** for integers.

Here is `-1`:

```
  11111111111111111111111111111111 (-1)
& 00000000000000000000000000000001 (--1)
----------------------------------
  00000000000000000000000000000001 (1)
```

So `(-1) & -(-1) = 1`, then `log2(1) = 0`, and `0 + 1 = 1`.

And `-2`:

```
  11111111111111111111111111111110 (-2)
& 00000000000000000000000000000010 (--2)
----------------------------------
  00000000000000000000000000000010 (2)
```

So `(-2) & -(-2) = 2`, then `log2(2) = 1`, and `1 + 1 = 2`.