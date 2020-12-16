## Geeks For Geeks : Two elements whose sum is closest to zero

Question: An Array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero.

For the below array, program should print -80 and 85.

### Solution

##### **Method - Using Sorting**

**Algorithm**

1) Sort all the elements of the input array.
2) Use two index variables l and r to traverse from left and right ends respectively. Initialize l as 0 and r as n-1.
3) sum = a[l] + a[r]
4) If sum is -ve, then l++
5) If sum is +ve, then r–
6) Keep track of abs min sum.
7) Repeat steps 3, 4, 5 and 6 while l < r

```python
from typing import List

class Solution(object):

    def partition(self, arr, si, ei):
        x = arr[ei]
        i = (si - 1)

        for j in range(si, ei):
            if (arr[j] <= x):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
        return (i + 1)

    # Implementation of Quick Sort
    # arr[] --> Array to be sorted
    # si --> Starting index
    # ei --> Ending index
    def quickSort(self, arr, si, ei):
        pi = 0  # Partitioning index */
        if (si < ei):
            pi = self.partition(arr, si, ei)
            self.quickSort(arr, si, pi - 1)
            self.quickSort(arr, pi + 1, ei)

    def minAbsSumPair(self, arr: List[int], n: int) -> int:

        # Variables to keep track
        # of current sum and minimum sum
        sum, min_sum = 0, 10 ** 9

        # left and right index variables
        l = 0
        r = n - 1

        # variable to keep track of
        # the left and right pair for min_sum
        min_l = l
        min_r = n - 1

        # Array should have at least two elements*/
        if (n < 2):
            print("Invalid Input", end="")
            return

        # Sort the elements */
        self.quickSort(arr, l, r)

        while (l < r):
            sum = arr[l] + arr[r]

            # If abs(sum) is less
            # then update the result items
            if (abs(sum) < abs(min_sum)):
                min_sum = sum
                min_l = l
                min_r = r
            if (sum < 0):
                l += 1
            else:
                r -= 1

        print("The two elements whose sum is minimum are",
              arr[min_l], "and", arr[min_r])
        return (arr[min_l] + arr[min_r])
```
**Output:**
```
The two elements whose sum is minimum are -80 and 85
```

##### **Time Complexity:** O(NlogN)

Time complexity to sort + complexity of finding the optimum pair = `O(NlogN) + O(N) = O(NlogN)`.
