# LeetCode - Problem 79 - Word Search

## Problem Description:

Given an `m x n` board and a word, 
find if the `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

#### **Example 1:**

![Image_1](Image_1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
       word = "ABCCED"
Output: true
```

#### **Example 2:**

![Image_2](Image_2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
       word = "SEE"
Output: true
```

#### **Example 3:**

![Image_3](Image_3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
       word = "ABCB"
Output: false
```

#### **Constraints:**
* `m == board.length`
* `n = board[i].length`
* `1 <= m, n <= 200`
* `1 <= word.length <= 103`
* `board` and `word` consists only of lowercase and uppercase English letters.
