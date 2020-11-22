## Geeks For Geeks : Maximum sum increasing subsequence

Find a subsequence of a given sequence such that subsequence sum is as high as possible and subsequence's elements are in sorted order, from lowest to highest. This subsequence is not necessarily contiguous or unique. The Maximum sum increasing subsequence (MSIS) problem is a variation of Longest Increasing Subsequence

For example, consider the subsequence `{0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11}`. 
The maximum sum increasing subsequence is `{8, 12, 14}` which has a sum of `34`.

The Maximum sum increasing subsequence (MSIS) problem is a 
standard variation of [Longest Increasing Subsequence problem](https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/).
The idea is to use [Recursion](https://www.techiedelight.com/recursion-practice-problems-with-solutions/) to solve this problem. For each item, there are two possibilities --

* We include current item in MSIS if it is greater than the previous element in MSIS and recur for remaining items.
* We exclude current item from MSIS and recur for remaining items.
* Finally, we return maximum sum we get by including or excluding current item. The base case of the recursion would be when no items are left.

Below is a Python implementation of the idea:

```python
from typing import List
import math

import unittest


class Solution(object):
    # TC: O(2^N) Exponential
    # SC: O(1)
    #
    # Function to find maximum sum of increasing subsequence
    def maxSumIS(self, A: List[int], n: int, i: int = 0, prev: float = math.inf,  sum: int = 0) -> int:
        # Base case: nothing is remaining
        if i == n:
            return sum

        # case 1: exclude the current element and process the
        # remaining elements
        excl = self.maxSumISRecursive(A, n, i + 1, prev, sum)

        # case 2: include the current element if it is greater
        # than previous element
        incl = sum
        if A[i] > prev:
            incl = self.maxSumISRecursive(A, n, i + 1, A[i], sum + A[i])

        # return maximum of above two choices
        return max(incl, excl)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSumIS(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 101, 2, 3, 100], 106],
            [[1, 2, 3], 6]
        ):
            self.assertEqual(solution, sol.maxSumIS(A, len(A)))
            self.assertEqual(solution, sol.maxSumIS(A, len(A), 0, math.inf, 0))

# main
if __name__ == "__main__":
    unittest.main()
```

**Time Complexity:** O(2^N)

**Space Complexity:** O(1)

The problem has an [optimal substructure](https://www.techiedelight.com/introduction-dynamic-programming/#optimal-substructure). 
That means the problem can be broken down into smaller, simple “subproblems”, which can further be divided into yet simpler, 
smaller subproblems until the solution becomes trivial. Above solution 
also exhibits [[overlapping subproblems]](https://www.techiedelight.com/introduction-dynamic-programming/#overlapping-subproblems). 
If we draw the recursion tree of the solution, we can see that the same sub-problems are getting computed again and again.

We know that problems having optimal substructure and overlapping subproblems can be solved by using **Dynamic Programming**, 
in which subproblem solutions are ___Memoized___ rather than computed again and again. 
The ___Memoized___ version follows the top-down approach, since we first break the problem 
into subproblems and then calculate and store values.

We can also solve this problem in bottom-up manner. 
In the bottom-up approach, we solve smaller sub-problems first, 
then solve larger sub-problems from them. 
The following bottom-up approach computes `sum[i]`, 
for each `0 <= i < n`, which stores the maximum sum of an increasing subsequence 
of subarray `arr[0..i]` that ends with `arr[i]`. 
To calculate `sum[i]`, we consider MSIS of all smaller values of `i` 
(say `j`) already computed and pick the maximum `sum[j]` 
where `arr[j]` is less than the current element `arr[i]` 
and add current element `arr[i]` to it. 
It has the same asymptotic run-time as Memoization but no recursion overhead.

Below is a Python implementation of the idea:

```python
from typing import List
import math

import unittest


class Solution(object):
    # TC: O(N^2)
    # SC: O(N)
    #
    # Function to find maximum sum of increasing subsequence
    def maxSumIS(self, A: List[int], n: int) -> int:
        # list to store sub-problem solution. sum[i] stores the maximum
        # sum of the increasing sub-sequence that ends with A[i]
        sum = [0] * n

        # base case
        sum[0] = A[0]

        # start from second element in the list
        for i in range(1, n):

            # do for each element in sublist A[0..i-1]
            for j in range(i):

                # find increasing sub-sequence with maximum sum that ends with
                # A[j] where A[j] is less than the current element A[i]
                if sum[i] < sum[j] and A[i] > A[j]:
                    sum[i] = sum[j]

            # include A[i] in MSIS
            sum[i] += A[i]

        # find increasing sub-sequence with maximum sum
        return max(sum)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSumIS(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 101, 2, 3, 100], 106],
            [[1, 2, 3], 6]
        ):
            self.assertEqual(solution, sol.maxSumIS(A, len(A)))
```

The time complexity of above solution is **O(n<sup>2</sup>)** and auxiliary space used by the program is `O(n)`.

How to print MSIS?

Above solutions only print the sum of MSIS but do not actually print MSIS itself. To print the MSIS, we actually have to store the maximum sum increasing subsequence in lookup table along with storing maximum sum.

For example, consider `arr = [ 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11 ]`

The Maximum sum Increasing Subsequence `MSIS[i]` of subarray `arr[0..i]` that ends with `arr[i]` are -

<font face="consolas" size="3"><br>
MSIS[0] – 8<br>
MSIS[1] – 4<br>
MSIS[2] – 8 12<br>
MSIS[3] – 2<br>
MSIS[4] – 8 10<br>
MSIS[5] – 4 6<br>
<strong>MSIS[6] – 8 12 14</strong><br>
MSIS[7] – 1<br>
MSIS[8] – 4 6 9<br>
MSIS[9] – 4 5<br>
MSIS[10] – 8 12 13<br>
MSIS[11] – 2 3<br>
MSIS[12] – 4 6 9 11<br>
<br>
</font>

Below is Python implementation of the idea:
```python
# Iterative function to princreasing subsequence with the maximum sum
def printMSIS(A):

	n = len(A)

	# MSIS[i] stores the increasing subsequence having maximum sum
	# that ends with A[i]
	MSIS = [[] for _ in range(n)]
	MSIS[0].append(A[0])

	# sum[i] stores the maximum sum of the increasing subsequence
	# that ends with A[i]
	sum = [0] * n
	sum[0] = A[0]

	# start from second element in the list
	for i in range(1, n):

		# do for each element in sublist[0..i-1]
		for j in range(i):

			# find increasing subsequence with maximum sum that ends with
			# A[j] where A[j] is less than the current element A[i]

			if sum[i] < sum[j] and A[i] > A[j]:
				MSIS[i] = MSIS[j].copy()				# update increasing subsequence
				sum[i] = sum[j]						 # update maximum sum

		# include current element in increasing subsequence
		MSIS[i].append(A[i])

		# add current element to maximum sum
		sum[i] += A[i]

	# j will contain index of MSIS
	j = 0
	for i in range(1, n):
		if sum[i] > sum[j]:
			j = i

	# print MSIS
	print(MSIS[j])


if __name__ == '__main__':

	A = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
	printMSIS(A)
```

```
Output:

[8, 12, 14]

```

The time complexity of above solution is **O(n<sup>2</sup>)** and auxiliary space used by the program is **O(n<sup>2</sup>)**.