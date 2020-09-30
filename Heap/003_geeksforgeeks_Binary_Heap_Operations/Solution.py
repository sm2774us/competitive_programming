#
# Time : O(Q*Log(size of Heap)); Space: O(1)
# @tag : Heap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Binary Heap Operations
#
# Description:
#
# A binary heap is a Binary Tree with the following properties:
# 1) It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.
#
# 2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.
#
# You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
# 1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
# 2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
# 3) 3  (a query like this removes the min element from the min-heap and prints it ).
#
# Example 1:
#
# Input:
# Q = 7
# Queries:
# insertKey(4)
# insertKey(2)
# extractMin()
# insertKey(6)
# deleteKey(0)
# extractMin()
# extractMin()
# Output: 2 6 - 1
# Explanation: In the first test case for
# query
# insertKey(4) the heap will have  {4}
# insertKey(2) the heap will be {2 4}
# extractMin() removes min element from
#              heap ie 2 and prints it
#              now heap is {4}
# insertKey(6) inserts 6 to heap now heap
#              is {4 6}
# deleteKey(0) delete element at position 0
#              of the heap,now heap is {6}
# extractMin() remove min element from heap
#              ie 6 and prints it  now the
#              heap is empty
# extractMin() since the heap is empty thus
#              no min element exist so -1
#              is printed.
#
# Example 2:
#
# Input:
# Q = 5
# Queries:
# insertKey(8)
# insertKey(9)
# deleteKey(1)
# extractMin()
# extractMin()
# Output: 8 -1
#
#
# Your Task:
# You are required to complete the 3 methods insertKey() which take one argument the value to be inserted, deleteKey() which takes one argument the position from where the element is to be deleted and extractMin() which returns the minimum element in the heap(-1 if the heap is empty)
#
# Expected Time Complexity: O(Q*Log(size of Heap) ).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 <= Q <= 104
# 1 <= x <= 104
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/operations-on-binary-min-heap/1 (GeeksForGeeks - Binary Heap Operations)
#
#
import sys

# Import the heap functions from python library
from heapq import heappush, heappop, heapify

# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

import unittest

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1

# A class for Min Heap
class MinHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i - 1) / 2)

    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )

    # Method to remove minium element from min heap
    def extractMin(self):
        if not self.heap:
            return -1
        return heappop(self.heap)

    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, INT_MIN)
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMedian(self) -> None:
        heapObj = MinHeap()
        heapObj.insertKey(3)
        heapObj.insertKey(2)
        heapObj.deleteKey(1)
        heapObj.insertKey(15)
        heapObj.insertKey(5)
        heapObj.insertKey(4)
        heapObj.insertKey(45)

        self.assertEqual(2, heapObj.extractMin())
        self.assertEqual(4, heapObj.getMin())
        heapObj.decreaseKey(2, 1)
        self.assertEqual(1, heapObj.getMin())

        heapObj = MinHeap()
        heapObj.insertKey(4)
        heapObj.insertKey(2)
        self.assertEqual(2, heapObj.extractMin())
        heapObj.insertKey(6)
        heapObj.deleteKey(0)
        self.assertEqual(6, heapObj.extractMin())
        self.assertEqual(-1, heapObj.extractMin())


if __name__ == "__main__":
    unittest.main()
