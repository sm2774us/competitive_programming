## Geeks For Geeks : Matrix Chain Multiplication

Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
The problem is not actually to perform the multiplications, but merely to decide 
in which order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is associative. 
In other words, no matter how we parenthesize the product, the result will be the same. 
For example, if we had four matrices A, B, C, and D, we would have: 

```
(ABC)D = (AB)(CD) = A(BCD) = ....
```

However, the order in which we parenthesize the product affects the number of simple arithmetic operations 
needed to compute the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, 
and C is a 5 × 60 matrix. Then,  

```
(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
```

Clearly the first parenthesization requires less number of operations.

Given an array `p[]` which represents the chain of matrices such that the i<sup>th</sup> matrix A<sub>i</sub> 
is of dimension `p[i-1] * p[i]`. 
We need to write a function `MatrixChainOrder()` that should return the minimum number of multiplications 
needed to multiply the chain. 

```
Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000  
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
```

```
Input: p[] = {10, 20, 30, 40, 30} 
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30
```

```
Input: p[] = {10, 20, 30}  
Output: 6000  
There are only two matrices of dimensions 10x20 and 20x30. So there 
is only one way to multiply the matrices, cost of which is 10*20*30
```

**Matrix chain multiplication** (or Matrix Chain Ordering Problem, MCOP) is an optimization problem 
to find the most efficient way to multiply given sequence of matrices. 
The problem is not actually to perform the multiplications, but merely to decide the sequence 
of the matrix multiplications involved.

The matrix multiplication is associative as no matter how the product is parenthesized, 
the result obtained will remain the same. 
For example, for four matrices A, B, C, and D, we would have

```
((AB)C)D = ((A(BC))D) = (AB)(CD) = A((BC)D) = A(B(CD))
```

However, the order in which the product is parenthesized affects the number of simple arithmetic operations 
needed to compute the product, or the efficiency. For example, if A is a 10 × 30 matrix, B is a 30 × 5 matrix,
and C is a 5 × 60 matrix, then:
 
 * computing `(AB)C` needs `(10×30×5) + (10×5×60) = 1500 + 3000 = 4500` operations
 * while computing `A(BC)` needs `(30×5×60) + (10×30×60) = 9000 + 18000 = 27000` operations

Clearly the first method is more efficient.

The idea is to break the problem into a set of related subproblems which group the given matrix in such a way 
that yields the lowest total cost.

Below is the recursive algorithm to find the minimum cost -
 * Take the sequence of matrices and separate it into two subsequences.
 * Find the minimum cost of multiplying out each subsequence.
 * Add these costs together, and add in the cost of multiplying the two result matrices.
 * Do this for each possible position at which the sequence of matrices can be split, and take the minimum over all of them.

For example, if we have four matrices `ABCD`, we compute the cost required to find each of `(A)(BCD)`, 
`(AB)(CD)`, and `(ABC)(D)`, making recursive calls to find the minimum cost to compute 
`ABC`, `AB`, `CD`, and `BCD`. We then choose the best one. Better still, this yields not only the minimum cost, 
but also demonstrates the best way of doing the multiplication.

Below is the Python implementation of the idea:

```python
# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j):

	# base case: one matrix
	if j <= i + 1:
		return 0

	# stores minimum number of scalar multiplications (i.e., cost)
	# needed to compute the matrix M[i+1]...M[j] = M[i..j]
	min = float('inf')

	# take the minimum over each possible position at which the
	# sequence of matrices can be split

	"""
		(M[i+1]) x (M[i+2]..................M[j])
		(M[i+1]M[i+2]) x (M[i+3.............M[j])
		...
		...
		(M[i+1]M[i+2]............M[j-1]) x (M[j])
	"""

	for k in range(i + 1, j):

		# recur for M[i+1]..M[k] to get an i x k matrix
		cost = MatrixChainMultiplication(dims, i, k)

		# recur for M[k+1]..M[j] to get a k x j matrix
		cost += MatrixChainMultiplication(dims, k, j)

		# cost to multiply two (i x k) and (k x j) matrix
		cost += dims[i] * dims[k] * dims[j]

		if cost < min:
			min = cost

	# return min cost to multiply M[j+1]..M[j]
	return min


if __name__ == '__main__':

	# Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
	# input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
	dims = [10, 30, 5, 60]

	print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1))
```
```
Output:

Minimum cost is 4500
```

The time complexity of above solution is exponential as we are doing a lot of redundant work. 
For example, for matrix `ABCD` we will make a recursive call to find the best cost for computing both 
`ABC` and `AB`. But finding the best cost for computing `ABC` also requires finding the best cost for 
`AB`. As the recursion grows deeper, more and more of this type of unnecessary repetition occurs. 
The idea is to use **memoization**. Now each time we compute the minimum cost needed to multiply out a specific subsequence, 
we save it. If we are ever asked to compute it again, we simply give the saved answer, and do not recompute it.

Below is the Python implementation of the idea:

```python
# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j, T):
 
    # base case: one matrix
    if j <= i + 1:
        return 0
 
    # stores minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i+1]...M[j] = M[i..j]
    min = float('inf')
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a lookup table
    if T[i][j] == 0:
 
        # take the minimum over each possible position at which the
        # sequence of matrices can be split
 
        """
            (M[i+1]) x (M[i+2]..................M[j])
            (M[i+1]M[i+2]) x (M[i+3.............M[j])
            ...
            ...
            (M[i+1]M[i+2]............M[j-1]) x (M[j])
        """
 
        for k in range(i + 1, j):
 
            # recur for M[i+1]..M[k] to get an i x k matrix
            cost = MatrixChainMultiplication(dims, i, k, T)
 
            # recur for M[k+1]..M[j] to get a k x j matrix
            cost += MatrixChainMultiplication(dims, k, j, T)
 
            # cost to multiply two (i x k) and (k x j) matrix
            cost += dims[i] * dims[k] * dims[j]
 
            if cost < min:
                min = cost
 
        T[i][j] = min
 
    # return min cost to multiply M[j+1]..M[j]
    return T[i][j]
 
 
if __name__ == '__main__':
 
    # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
    # input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
    dims = [10, 30, 5, 60]
 
    # lookup table to store the solution to already computed sub-problems
    T = [[0 for x in range(len(dims))] for y in range(len(dims))]
 
    print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1, T))
```
```
Output:

Minimum cost is 4500
```

The time complexity of above solution is <span class="consolas red">O(n<sup>3</sup>)</span> and auxiliary space 
used by the program is <span class="consolas green">O(1)</span>.


The following bottom-up approach computes, for each `2 <= k <= n`, the minimum costs of all subsequences of length `k`, 
using the costs of smaller subsequences already computed. It has the same asymptotic runtime and requires no recursion.

Below is the Python implementation of the idea:

```python
# Function to find the most efficient way to multiply
# given sequence of matrices
def matrixChainMultiplication(dims):
 
    n = len(dims)
 
    # c[i,j] = minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix M[i]M[i+1]...M[j] = M[i..j]
    # The cost is zero when multiplying one matrix
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    for length in range(2, n + 1):  # Subsequence lengths
 
        for i in range(1, n - length + 2):
 
            j = i + length - 1
            c[i][j] = float('inf')
 
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
 
                if cost < c[i][j]:
                    c[i][j] = cost
 
                k = k + 1
 
    return c[1][n - 1]
 
 
if __name__ == '__main__':
 
    # Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
    # input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
    dims = [10, 30, 5, 60]
 
    print("Minimum cost is", matrixChainMultiplication(dims))
```
```
Output:

Minimum cost is 4500
```
