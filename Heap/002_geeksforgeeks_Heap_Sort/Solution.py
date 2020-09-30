#
# Time : O(N * Log(N)); Space: O(1)
# @tag : Heap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Heap Sort
#
# Description:
#
# Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() which are used to implement Heap Sort.
#
# Example 1:
#
# Input:
# N = 5
# arr[] = {4,1,3,9,7}
# Output:1 3 4 7 9
# Explanation:After sorting elements
# using heap sort, elements will be
# in order as 1,3,4,7,9.

# Example 2:
#
# Input:
# N = 10
# arr[] = {10,9,8,7,6,5,4,3,2,1}
# Output:1 2 3 4 5 6 7 8 9 10
# Explanation:After sorting elements
# using heap sort, elements will be
# in order as 1, 2,3,4,5,6,7,8,9,10.

# Your Task :
# Complete the functions heapify() and buildheap().
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/heap-sort/1 (GeeksForGeeks - Heap Sort)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# How to build the heap?
# Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom-up order.
#
# Lets understand with the help of an example:
#
# Input data: 4, 10, 3, 5, 1
#          4(0)
#         /   \
#      10(1)   3(2)
#     /   \
#  5(3)    1(4)
#
# The numbers in bracket represent the indices in the array
# representation of data.
#
# Applying heapify procedure to index 1:
#          4(0)
#         /   \
#     10(1)    3(2)
#     /   \
# 5(3)    1(4)
#
# Applying heapify procedure to index 0:
#         10(0)
#         /  \
#      5(1)  3(2)
#     /   \
#  4(3)    1(4)
# The heapify procedure calls itself recursively to build heap in top down manner.
#
# **************************************************************************
#
#
from heapq import *

import unittest


class Solution:
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, n, largest)

    # The main function to sort an array of given size
    def buildHeap(self, arr):
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)

        return arr


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMedian(self) -> None:
        solution = Solution()
        self.assertEqual([1, 3, 4, 7, 9], solution.buildHeap([4, 1, 3, 9, 7]))
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            solution.buildHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        )


if __name__ == "__main__":
    unittest.main()
