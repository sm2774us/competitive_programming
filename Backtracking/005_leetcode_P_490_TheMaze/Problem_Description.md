# LeetCode - Problem 490 - The Maze

## Problem Description:

There is a **ball** in a maze with empty spaces and walls. The ball can go 
through empty spaces by rolling **up, down, left** or **right**, but it won’t stop 
rolling until hitting a wall. When the ball stops, it could choose the next 
direction.

Given the ball’s **start position**, the **destination** and the **maze**, determine 
whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 
means the empty space. You may assume that the borders of the maze are 
all walls. The start and destination coordinates are represented by row and 
column indexes.

#### **Example 1:**

> **Input 1:** `a maze represented by a 2D array`
> ```
> 0 0 1 0 0
> 0 0 0 0 0
> 0 0 0 1 0
> 1 1 0 1 1
> 0 0 0 0 0
> ```
>
> **Input 2:** `start coordinate (rowStart, colStart) = (0, 4)`
>
> **Input 3:** `destination coordinate (rowDest, colDest) = (4, 4)`
>
> **Output:** `true`
> 
> **Explanation:** `One possible way is : left -> down -> left -> down -> right -> down -> right.`
>
![Image_1](Image_1.png)
