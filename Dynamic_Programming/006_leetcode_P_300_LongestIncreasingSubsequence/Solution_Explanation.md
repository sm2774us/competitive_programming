## LeetCode - Problem 300 - Longest Increasing Subsequence

### Longest Increasing Subsequence Problem and Its Duality

In this post I will give some algorithm problem from Google OA as well as Leetcode and my thoughts on them.

Our main problem here will be the OA problem appeared in the OA practice of Google Intern 2020 Online Assesment.

#### Problem Description:
___
You are given an array `A` representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in `A`). For the i-th student, if there is a row in which all the students are taller than `A[i]`, the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.

Write a function that, given a non-empty array `A` containing `N` integers, denoting the heights of the students, returns the minimum number of rows created.

```
For example, given A = [5, 4, 3, 6, 1], the function should return 2.
Students will arrive in sequential order from A[0] to A[N−1]. So, the first 
student will have height = 5, the second student will have height = 4, and so on.
For the first student, there is no row, so the student will create a new row.
Row1 = [5]
For the second student, all the students in Row1 have height greater than 4. 
So, the student will stand in Row1.
Row1 = [5, 4]
Similarly, for the third student, all the students in Row1 have height greater 
than 3. So, the student will stand in Row1.
Row1 = [5, 4, 3]
For the fourth student, there is no row in which all the students have height 
greater than 6. So, the student will create a new row.
Row1 = [5, 4, 3]
Row2 = [6]
For the fifth student, all the students in Row1 and Row2 have height greater 
than 1. So, the student can stand in either of the two rows.
Row1 = [5, 4, 3, 1]
Row2 = [6]
Since two rows are created, the function should return 2.
```

Assume that:
* N is an integer within the range [1..1,000]
* each element of array A is an integer within the range [1..10,000]

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment

#### Thoughts
___
##### Original Problem
___
**Patience.** Deal cards ___c<sub>1</sub>,c<sub>2</sub>,...,c<sub>n</sub>___ into piles according to two rules:

* Can’t place a higher-valued card onto a lowered-valued card.
* Can form a new pile and put a card onto it.

**Goal.** Form as few piles as possible.

##### Dual Problem
___
The dual problem for this is Longest increasing subsequence. And the Problem is defined as: Given a sequence of elements  from a totally-ordered universe, find the longest increasing subsequence.

##### Duality Proof
___
* Greedy Algorithm
    * Place each card on leftmost pile that fits.
    * **Observation.** At any stage during greedy algorithm, top cards of piles increase from left to right.
* Weak duality.
    * In any legal game of patience, the number of piles ≥ length of any increasing subsequence.
    * **Proof.**
      
      1] Cards within a pile form a decreasing subsequence.
      
      2] ___Any___ increasing sequence can use at most one card from each pile.

* Strong duality
    * [Hammersley 1972]Min number of piles = max length of an IS; moreover **greedy algorithm** finds both.
    * **Proof.**
      
      Each card maintains a pointer to top card in previous pile at time of insertion.
      
      1] Follow pointers to obtain IS whose length equals the number of piles.

      2] By weak duality, both are optimal.

Conclusion

The length of longest increasing subsequence is equal to the smallest number of decreasing subsequences.

#### Solution
___
##### Greedy Algorithm + Binary Search Algorithm
___
Time Complexity: ![equation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20%5Clarge%20%5Cmathcal%7BO%7D%28n*log%28n%29%29)

```python
from typing import List

import unittest

class Solution(object):
    # Greedy Algorithm + Binary Search Algorithm
    # Time complexity: O(n log n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # greedy and binary search
        tail_list = [0] * len(nums)
        size = 0
        for height in nums:
            # i: start index of rows
            # j: end index of rows
            i, j = 0, size
            while i != j:
                m = int((i + j) / 2)
                # note here we need <= to ensure in each row is strictly decreasing
                # according to the problem description
                if tail_list[m] <= height:
                    i = m + 1
                else:
                    j = m
            tail_list[i] = height
            size = max([i + 1, size])
        return size


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lengthOfLIS(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[10,9,2,5,3,7,101,18], 4],
            [[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], 6],
            [[5,8,3,7,9,1], 3],
        ):
            self.assertEqual(solution, sol.lengthOfLIS(nums))


# main
if __name__ == "__main__":
    unittest.main()
```

___
##### DP
___
Time Complexity: ![equation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20%5Clarge%20%5Cmathcal%7BO%7D%28n%5E2%29)

```python
from typing import List

import unittest

class Solution(object):
    # DP
    # Time complexity: O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP, convert to Longest Non-decreasing Subsequence Problem (LNDS)
        # memo[i] LNDS including ending with arr[i]
        n = len(nums)
        if n == 0:
            return 0
        memo = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] >= nums[j]:
                    memo[i] = max([memo[i], memo[j]+1])
        return max(memo)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_lengthOfLIS(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[10,9,2,5,3,7,101,18], 4],
            [[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], 6],
            [[5,8,3,7,9,1], 3],
        ):
            self.assertEqual(solution, sol.lengthOfLIS(nums))


# main
if __name__ == "__main__":
    unittest.main()
```

#### Related Problems
___
* [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
* [Google | Summer Intern OA 2019 | Decreasing Subsequences](https://leetcode.com/discuss/interview-question/350233/Google-or-Summer-Intern-OA-2019-or-Decreasing-Subsequences)
* [72. Edit Distance](https://leetcode.com/problems/edit-distance/) (in sense of DP for Leetcode 300)
    * ___x = c<sub>1</sub>c<sub>2</sub>...c<sub>n</sub>___.
    * ___y =___ sorted sequence of ___c<sub>k</sub>___, removing any duplicates.
    * Mismatch penalty = Inf; gap penalty = 1.  
* [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)

#### Interesting Related Algorithm
___
* Patience sorting
    * Deal all cards using greedy algorithm; repeatedly remove smallest card.
    * For uniformly random deck, time complexity: ![equation](https://latex.codecogs.com/svg.latex?%5Cbg_white%20%5Clarge%20O%28n%5E%7B3/2%7D%29)
    * ([Persi Diaconis]Patience sorting is the fastest wayto sort a pile of cards by hand.)

#### Reference
___
* [DP slides from Princeton CS 423](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf) (Patience solitaire)
