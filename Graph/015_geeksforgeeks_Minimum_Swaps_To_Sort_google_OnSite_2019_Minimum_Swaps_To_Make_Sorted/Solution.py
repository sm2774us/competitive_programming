#
# Time : O(N log N); Space: O(N)
# @tag : Graph ; Selection Sort ; Heap and Dictionary ; Union Find
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Minimum Swaps to Sort
#
# Description:
#
# Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .
#
# Output:
# For each test case in a new line output will be an integer denoting  minimum umber of swaps that are  required to sort the array.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 105
# 1 <= A[] <= 106
#
# User Task:
# You don't need to read input or print anything. Your task is to complete the function minSwaps() which takes the array arr[] and its size N as inputs and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0.
#
# Expected Time Complexity: O(NlogN).
# Expected Auxiliary Space: O(N).
#
# Example(To be used only for expected output):
# Input:
# 2
# 5
# 1 5 4 3 2
# 4
# 8 9 16 15
#
# Output:
# 2
# 1
#
# Explanation:
# Test Case 1: We need two swaps, swap 2 with 5 and 3 with 4 to make it sorted.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-swaps/1 (GeeksForGeeks - Minimum Swaps to Sort)
#
# **************************************************************************
# Solution Explanation ( for graph DS based solution , i.e. , method -> minSwapsUsingGraph(...)
# **************************************************************************
# Refer to Solution_Explanation.md.
#

#
from typing import List
import heapq

import unittest


class Solution:
    # NOTE: Sub-Optimal Solutuon : DO NOT USE THIS SOLUTION IN AN INTERVIEW
    # Method 1: Selection Sort
    # O(N^2)
    def minSwapsUsingSelectionSort(self, A: List[int]) -> int:
        count = 0
        for i in range(len(A) - 1):
            idx = i
            for j in range(i + 1, len(A)):
                if A[j] < A[idx]:
                    idx = j
            if A[idx] != A[i]:
                A[idx], A[i] = A[i], A[idx]
                count += 1
        return count

    # Method 2 : Heap + Dictionary Solution
    # Time Complexity: O(n Log n)
    # Auxiliary Space: O(n)

    # Intuition: Selection sort minimizes swaps. So there is a O(N^2) solution. the problem is that selection sort
    #            keeps finding the min element in the unsorted portion of the array.
    #            This leads to finding min by O(N) in each iteration.
    #            So how can we speed it up?
    #
    #            We can use a heap to give us the smallest element all the time when we need it.
    #            We can loop through the whole array while updating it on the run.
    #            Now a problem arises: Since we are using a heap, we have no idea where the smallest element is at.
    #            We can not perform a swap, we can only check if the current element is the smallest or not.
    #            If we do that comparison, this could lead to an incorrect number of swaps.
    #            This due to the fact that swaps can luckily get two elements to the correct position at the same time
    #            e.g.: [4,2,3,1] -> [1,2,3,4] (One swap, two elements are at correct position).
    #
    #            Therefore, we need to have a dictionary that maps each value of the array to its indices and use,
    #            update this dictionary while we do the swaps within the array by using the heap.
    #
    #            We can find where the minimum of the unsorted portion of the array is by using the dictionary
    #            and then do a swap operation within the array and swap the corresponding key,
    #            values in the dictionary to keep it correct.
    #
    #
    # Time complexity:
    # O(N) -> Build Heap
    # O(N logN) -> N pops from heap
    # = O(N + N logN) -> O(N logN)
    #
    # Space:
    # Heap + dic -> O(N)
    def minSwapsUsingHeapAndDict(self, A: List[int]) -> int:
        keyToIndex = dict([(A[i], i) for i in range(len(A))])
        heap = A[::]
        heapq.heapify(heap)

        swaps = 0
        for i in range(len(A)):
            smallest = heapq.heappop(heap)

            # check if previous swaps luckily made the array sorted
            if A[i] != smallest:
                currNum = A[i]  # needed to update the dic two lines below
                A[i], A[keyToIndex[smallest]] = A[keyToIndex[smallest]], A[i]
                keyToIndex[smallest], keyToIndex[currNum] = (
                    keyToIndex[currNum],
                    keyToIndex[smallest],
                )
                swaps += 1

        return swaps

    # Method 3 : Using Graph Data Structure

    # Python3 program to find  minimum number
    # of swaps required to sort an array
    #
    # Function returns the minimum
    # number of swaps required to sort the array
    #
    # Time Complexity: O(n Log n)
    # Auxiliary Space: O(n)
    # https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
    def minSwapsUsingGraph(self, A: List[int]) -> int:
        n = len(A)

        # Create two arrays and use
        # as pairs where first array
        # is element and second array
        # is position of first element
        arrpos = [*enumerate(A)]

        # Sort the array by array element
        # values to get right position of
        # every element as the elements
        # of second array.
        arrpos.sort(key=lambda it: it[1])

        # To keep track of visited elements.
        # Initialize all elements as not
        # visited or false.
        vis = {k: False for k in range(n)}

        # Initialize result
        ans = 0
        for i in range(n):

            # alreadt swapped or
            # alreadt present at
            # correct position
            if vis[i] or arrpos[i][0] == i:
                continue

            # find number of nodes
            # in this cycle and
            # add it to ans
            cycle_size = 0
            j = i
            while not vis[j]:
                # mark node as visited
                vis[j] = True

                # move to next node
                j = arrpos[j][0]
                cycle_size += 1

            # update answer by adding
            # current cycle
            if cycle_size > 0:
                ans += cycle_size - 1
                # return answer
        return ans

    # Method 4 : Using Union Find
    def minSwapsUsingUnionFind(self, A: List[int]) -> int:
        d = {}

        def find(a):
            d.setdefault(a, a)
            if d[a] != a:
                d[a] = find(d[a])
            return d[a]

        def union(a, b):
            d[find(a)] = find(b)

        for i, x in enumerate(A):
            d[x] = "i" + str(i)

        A.sort()

        for i, x in enumerate(A):
            union(x, "i" + str(i))

        return len(A) - len(set(map(find, A)))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minSwapsUsingSelectionSort(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 2, 3], 0],
            [[1, 3, 2], 1],
            [[5, 1, 3, 2, 6, 11], 2],
            [[5, 1, 3, 2, 0], 2],
            [[5, 4, 3, 2, 1, 0], 3],
            [[2, 4, 1, 3, 0], 3],
            [[21, 14, 61, 8, 0], 4],
        ):
            self.assertEqual(solution, sol.minSwapsUsingSelectionSort(A))

    def test_minSwapsUsingHeapAndDict(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 2, 3], 0],
            [[1, 3, 2], 1],
            [[5, 1, 3, 2, 6, 11], 2],
            [[5, 1, 3, 2, 0], 2],
            [[5, 4, 3, 2, 1, 0], 3],
            [[2, 4, 1, 3, 0], 3],
            [[21, 14, 61, 8, 0], 4],
        ):
            self.assertEqual(solution, sol.minSwapsUsingHeapAndDict(A))

    def test_minSwapsUsingGraph(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 2, 3], 0],
            [[1, 3, 2], 1],
            [[5, 1, 3, 2, 6, 11], 2],
            [[5, 1, 3, 2, 0], 2],
            [[5, 4, 3, 2, 1, 0], 3],
            [[2, 4, 1, 3, 0], 3],
            [[21, 14, 61, 8, 0], 4],
        ):
            self.assertEqual(solution, sol.minSwapsUsingGraph(A))

    def test_minSwapsUsingUnionFind(self) -> None:
        sol = Solution()
        for A, solution in (
            [[1, 2, 3], 0],
            [[1, 3, 2], 1],
            [[5, 1, 3, 2, 6, 11], 2],
            [[5, 1, 3, 2, 0], 2],
            [[5, 4, 3, 2, 1, 0], 3],
            [[2, 4, 1, 3, 0], 3],
            [[21, 14, 61, 8, 0], 4],
        ):
            self.assertEqual(solution, sol.minSwapsUsingUnionFind(A))


# main
if __name__ == "__main__":
    unittest.main()
