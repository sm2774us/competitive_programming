## Geeks For Geeks : Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

##### **Examples:**

```
  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1
```

### Solution

##### **Method 1 - Brute Force Algorithm - (Simple but Inefficient)**

Run two loops. In the outer loop, pick elements one by one from left. 
In the inner loop, compare the picked element with the elements 
starting from the right side. Stop the inner loop when
you see an element greater than the picked element and keep 
updating the maximum `j-i` so far. 

```python
from typing import List

class Solution(object):
    # Python3 program to find the maximum
    # j – i such that arr[j] > arr[i]

    # For a given array arr[], returns
    # the maximum j – i such that
    # arr[j] > arr[i]
    #
    def maxIndexDiff(self, arr: List[int], n: int) -> int:
        maxDiff = -1
        for i in range(0, n):
            j = n - 1
            while (j > i):
                if arr[j] > arr[i] and maxDiff < (j - i):
                    maxDiff = j - i;
                j -= 1

        return maxDiff
```

**Time Complexity:** O(N^2)

##### **Method 2 - Improvised Brute Force Algorithm**

Improvising the Brute Force Algorithm and looking for BUD, i.e Bottlenecks, 
unnecessary and duplicated works. A quick observation actually shows that 
we have been looking to find the first greatest element traversing from the end 
of the array to the current index. We can see that we are trying to find the 
first greatest element again and again for each element in the array. 
Let’s say we have an array with us for example [1, 5, 12, 4, 9] now we know 
that 9 is the element which is greater than 1, 5, and 4 but why do we need 
to find that again and again. We can actually keep a track of the 
maximum number moving from the end to the start of the array. 
The approach will help us understand better and also this improvisation 
is great to come up within an interview. 

```python
from typing import List

class Solution(object):
    # Python3 program to implement
    # the above approach

    # For a given array arr,
    # calculates the maximum j – i
    # such that arr[j] > arr[i]
    #
    # TC: O(N * log(N))
    # SC: O(N)
    #
    def maxIndexDiff(self, arr: List[int], n: int) -> int:
        maxFromEnd = [-38749432] * (n + 1)

        # Create an array maxfromEnd
        for i in range(n - 1, 0, -1):
            maxFromEnd[i] = max(maxFromEnd[i + 1], arr[i])

        maxDiff = 0
        for i in range(0, n):
            low = i + 1;
            high = n - 1;
            ans = i;

            while (low <= high):
                mid = int((low + high) / 2)

                if (arr[i] <= maxFromEnd[mid]):

                    # We store this as current
                    # answer and look for further
                    # larger number to the right side
                    ans = max(ans, mid)
                    low = mid + 1
                else:
                    high = mid - 1

            # Keeping a track of the
            # maximum difference in indices
            maxDiff = max(maxDiff, ans - i)

        return maxDiff
```

**Time Complexity:** O(N * log(N))
**Space Complexity:** O(N)

##### **Method 3 - Efficient**

To solve this problem, we need to get two optimum indexes of `arr[]`: left index `i` 
and right index `j`. For an element `arr[i]`, we do not need to consider `arr[i]` 
for left index if there is an element smaller than `arr[i]` on left side of `arr[i]`. 
Similarly, if there is a greater element on right side of `arr[j]` then 
we do not need to consider this `j` for right index. 
So we construct two auxiliary arrays `leftMinArr[]` and `rightMaxArr[]` such that 
`leftMinArr[i]` holds the smallest element on left side of `arr[i]` including `arr[i]`, 
and `rightMaxArr[j]` holds the greatest element on right side of `arr[j]` including `arr[j]`. 
After constructing these two auxiliary arrays, 
we traverse both of these arrays from left to right. 
While traversing `leftMinArr[]` and `rightMaxArr[]` if we see that `leftMinArr[i]` 
is greater than `rightMaxArr[j]`, then we must move ahead in `leftMinArr[]` 
(or do `i++`) because all elements on left of `leftMinArr[i]` are greater 
than or equal to `leftMinArr[i]`. Otherwise we must move ahead in `rightMaxArr[j]` 
to look for a greater `j – i` value.

```python
from typing import List

class Solution(object):
    # Python3 program to implement
    # the above approach
    #
    # For a given array arr[],
    # returns the maximum j - i
    # such that arr[j] > arr[i]
    # TC: O(N)
    # SC: O(N)
    #
    def maxIndexDiff(self, arr: List[int], n: int) -> int:
        # Construct leftMinArr[] such that
        # leftMinArr[i] stores the minimum
        # value from (arr[0], arr[1], ... arr[i])
        leftMinArr = [0 for i in range(n)]
        leftMinArr[0] = arr[0]
        for i in range(1, n):
            leftMinArr[i] = min(arr[i], leftMinArr[i - 1])

        # Construct rightMaxArr[] such that
        # rightMaxArr[j] stores the maximum
        # value from (arr[j], arr[j + 1], ... arr[n-1])
        rightMaxArr = [0 for i in range(n)]
        rightMaxArr[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            rightMaxArr[i] = max(arr[i], rightMaxArr[i + 1])
        i, j, maxDiff = 0, 0, 0

        # Traverse both arrays from left
        # to right to find optimum j - i
        # This process is similar to merge() of MergeSort
        while i < len(leftMinArr) and j < len(rightMaxArr):
            if leftMinArr[i] <= rightMaxArr[j]:
                maxDiff = max(maxDiff, j - i)
                j += 1
            else:
                i += 1
        return maxDiff
```

**Time Complexity:** O(N)
**Space Complexity:** O(N)
