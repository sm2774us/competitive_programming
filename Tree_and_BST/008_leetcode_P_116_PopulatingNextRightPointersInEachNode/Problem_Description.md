# LeetCode - Problem 116 - Populating Next Right Pointers in Each Node

## Problem Description:

### Example 1:

![Example 1](example_1.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, 
just like in Figure B. 
The serialized output is in level order as connected by the next pointers, 
with '#' signifying the end of each level.
```

#### Constraints:

    1. The number of nodes in the given tree is less than 4096.
    2. -1000 <= node.val <= 1000