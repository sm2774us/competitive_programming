## GeeksForGeeks - Box Stacking Problem

Given a set of rectangular 3D boxes, create a stack of boxes which is as tall 
as possible. A box can be placed on top of another box if the dimensions of 
the 2D base of the lower box are each strictly larger than those of the 
2D base of the higher box.

![Image_1](Image_1.png)

**Source:** [http://people.csail.mit.edu/bdean/6.046/dp/](http://people.csail.mit.edu/bdean/6.046/dp/). 
The link also has video for explanation of solution.

#### Example :

For example, consider below boxes where each box has dimensions `L x W x H`

```
(4 x 2 x 5)
(3 x 1 x 6)
(3 x 2 x 1)
(6 x 3 x 8)
```

The rotations of the boxes are :

```
(4 x 2 x 5)
(5 x 4 x 2)
(5 x 2 x 4)

(3 x 1 x 6)
(6 x 3 x 1)
(6 x 1 x 3)

(3 x 2 x 1)
(3 x 1 x 2)
(2 x 1 x 3)

(6 x 3 x 8)
(8 x 6 x 3)
(8 x 3 x 6)
```

The maximum height possible is 22 which can be obtained by boxes in following order:

```
(3 x 1 x 6)
(4 x 2 x 5)
(6 x 3 x 8)
(8 x 6 x 3)
```

The idea is to use [Dynamic Programming](https://www.techiedelight.com/introduction-dynamic-programming/) to solve 
this problem. We start by generating all rotations of each box. For simplicity, we can easily enforce the constraint 
that the width of a box is never more than the length. After generating all rotations, we sort the boxes 
in descending order of area and then apply the 
[LIS algorithm](https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/) 
to the get the maximum height. Let `L(i)` store the maximum possible height when ___i<sup>th</sup>___ box is on the top. 
Then, the recurrence is:

```
L(i) = height(i) + max(L(j) | j &lt; i and block i can be put on top of block j)
```

Finally, the maximum height is the maximum value in `L[]`. 
The algorithm can be implemented as follows in Python:

```python
```

Output:

```
The maximum height is 22
```

The time complexity of above solution is **O(n<sup>2</sup>)** and auxiliary space used by the program is 
**O(n)** where `n` is the number of boxes.

**Problem source:** [https://people.csail.mit.edu/bdean/6.046/dp/](https://people.csail.mit.edu/bdean/6.046/dp/)