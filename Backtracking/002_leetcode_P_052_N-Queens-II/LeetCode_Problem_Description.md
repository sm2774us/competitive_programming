# LeetCode - Problem 52 - N-Queens II

## Problem Description:

The ___**n-queens puzzle**___ is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. Given an integer n, print all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard `[3 1 4 2]`.

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return ___all distinct solutions___ to the ___**n-queens puzzle**___.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

#### **Example 1:**

![Image_1](LeetCode_Image_1.jpg)

```
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.```

```
Input: n = 1
Output: 1
```

#### **Constraints:**
* 1 <= n <= 9