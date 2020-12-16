## Geeks For Geeks : A Boolean Matrix Question

Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1.

### **Examples:** 

```
Example 1
The matrix
1 0
0 0
should be changed to following
1 1
1 0

Example 2
The matrix
0 0 0
0 0 1
should be changed to following
0 0 1
1 1 1

Example 3
The matrix
1 0 0 1
0 0 1 0
0 0 0 0
should be changed to following
1 1 1 1
1 1 1 1
1 0 1 1
```

### Solution
#### **Method 1 (Use two temporary arrays):**

1. Create two temporary arrays row[M] and col[N]. Initialize all values of row[] and col[] as 0.
1. Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true, then mark row[i] and col[j] as true.
1. Traverse the input matrix mat[M][N] again. For each entry mat[i][j], check the values of row[i] and col[j]. If any of the two values (row[i] or col[j]) is true, then mark mat[i][j] as true.

```python
from typing import List

class Solution(object):

    # Solution 1: Use two temporary arrays
    #
    # TC: O(M*N)
    # SC: O(M+N)
    def booleanMatrix(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        row = [0] * R
        col = [0] * C

        # Initialize all values of row[] as 0
        for i in range(0, R):
            row[i] = 0

        # Initialize all values of col[] as 0
        for i in range(0, C):
            col[i] = 0

        # Store the rows and columns to be marked
        # as 1 in row[] and col[] arrays respectively
        for i in range(0, R):

            for j in range(0, C):
                if (matrix[i][j] == 1):
                    row[i] = 1
                    col[j] = 1

        # Modify the input matrix mat[] using the
        # above constructed row[] and col[] arrays
        for i in range(0, R):

            for j in range(0, C):
                if (row[i] == 1 or col[j] == 1):
                    matrix[i][j] = 1
```
**Output:**
```
Input Matrix
1 0 0 1
0 0 1 0
0 0 0 0
Matrix after modification
1 1 1 1
1 1 1 1
1 0 1 1
```

**Time Complexity:** `O(M*N)`

**Auxiliary Space:** `O(M + N)`

#### **Method 2 (A Space Optimized Version of Method 1):**

This method is a space optimized version of above method 1. This method uses the first row and first column of the input matrix in place of the auxiliary arrays row[] and col[] of method 1. So what we do is: first take care of first row and column and store the info about these two in two flag variables rowFlag and colFlag. Once we have this info, we can use first row and first column as auxiliary arrays and apply method 1 for submatrix (matrix excluding first row and first column) of size (M-1)*(N-1).

1. Scan the first row and set a variable rowFlag to indicate whether we need to set all 1s in first row or not.
1. Scan the first column and set a variable colFlag to indicate whether we need to set all 1s in first column or not.
1. Use first row and first column as the auxiliary arrays row[] and col[] respectively, consider the matrix as submatrix starting from second row and second column and apply method 1.
1. Finally, using rowFlag and colFlag, update first row and first column if needed.

```python
from typing import List

class Solution(object):

    # Solution 2: Space optimized version of Solution 1
    #
    # TC: O(M*N)
    # SC: O(1)
    def booleanMatrix(self, matrix: List[List[int]]) -> None:
        # r = len(matrix)
        # c = len(matrix[0])
        #
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == 1:
        #             for t in range(c):
        #                 if matrix[i][t] != 1:
        #                     matrix[i][t] = '1'
        #             for u in range(r):
        #                 if matrix[u][j] != 1:
        #                     matrix[u][j] = '1'
        #
        # for i in range(r):
        #     matrix[i] = list(map(int, matrix[i]))


        # variables to check if there are any 1
        # in first row and column
        row_flag = False
        col_flag = False

        # updating the first row and col
        # if 1 is encountered
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if (i == 0 and matrix[i][j] == 1):
                    row_flag = True

                if (j == 0 and matrix[i][j] == 1):
                    col_flag = True

                if (matrix[i][j] == 1):
                    matrix[0][j] = 1
                    matrix[i][0] = 1

        # Modify the input matrix mat[] using the
        # first row and first column of Matrix mat
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                #print(f"{i} ; {j}")
                if (matrix[0][j] == 1 or matrix[i][0] == 1):
                    matrix[i][j] = 1

        # modify first row if there was any 1
        if (row_flag == True):
            for i in range(0, len(matrix)):
                matrix[0][i-1] = 1

        # modify first col if there was any 1
        if (col_flag == True):
            for i in range(0, len(matrix)):
                matrix[i][0] = 1
```

**Output:**
```
Input Matrix
1 0 0 1
0 0 1 0
0 0 0 0
Matrix after modification
1 1 1 1
1 1 1 1
1 0 1 1
```

**Time Complexity:** `O(M*N)`

**Auxiliary Space:** `O(1)`