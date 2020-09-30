# Time : O( k*log(k) + (n-k)logk ) for init.
#        O( k + (n-k)logk ) for init if heapq.heapify is used.
#        O( logk ) for add.
# Space: O( k )
# **************************************************************************
# Where: k is the length of the heap
#        n is the size of the stream/list
# **************************************************************************
# @tag : Heap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 703: Kth Largest Element in a Stream
#
# Description:
#
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element
# in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains
# initial elements from the stream. For each call to the method KthLargest.add, return the element representing
# the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8

# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
#
# **************************************************************************
# Source: https://leetcode.com/problems/kth-largest-element-in-a-stream/ (Leetcode - Problem 703 - Kth Largest Element in a Stream)
#         https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0 (GeeksForGeeks - Kth largest element in a stream)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# LeetCode - Problem - 703: Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#
# Algorithm
# **************************************************************************
#   Basically three steps:
#
#   1. push first k elements into a heap with len as k
#   2. push the rest of the list into it, but pop out unnecessary part in order to keep the heap having len of k
#   3. For add(), if len(heap)<k, push it! If val should be in top k by comparing smallest top k, push it!
#
# Algorithm Notes
# **************************************************************************
#   * Python has a built in heapq library for min-heaps which store the minimum number at the top of the heap.
#   * The k'th largest element in a list will be the top of the min-heap when we restrict the size of the heap to k.
#   * Consider the following cases:
#       1. Case 1: Length of nums is greater than k :
#           +> nums = [1, 2, 3, 4] and k = 2.
#           +> Here the k largest element is 3, and so if we instantiate a min-heap from nums we will have a
#              heap of size 4. After removing the first two elements, i.e. the two smallest elements, we are left
#              with 3 at the top of the min-heap.
#       2. Case 2: Length of nums is less than k :
#           +> nums = [1, 2, 3, 4] and k = 5.
#           +> Because len(nums) == 4, the 5th largest element is just the smallest element, so we return 1,
#              which is also the top of the min-heap.
#       3. Case 3: Length of nums is equal to k :
#           +> nums = [1, 2, 3, 4] and k = 4.
#           +> The 4th largest element is just the smallest element which is just the head of the min-heap,
#              so 1 is returned.
# **************************************************************************
# Complexity Analysis:
# **************************************************************************
#   1. Time Complexity                        : O( k*log(k) + (n-k)logk ) for init. O( logk ) for add.
#       Improves to (using heapq.heapify )    : O( k + (n-k)logk ) for init. O( logk ) for add.
#   2. Space Complexity : O( k )
# Where: k is the size of the heap
#        n is the size of the stream/list
# **************************************************************************
#
#
from typing import List
import heapq

import unittest


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heapque = []

        # # O(k*log(k))
        # for i in nums[:k]:
        #     heapq.heappush(self.heapque, i)

        # O(k)
        self.heapque = [i for i in nums[:k]]
        heapq.heapify(self.heapque)

        # O( (n-k)logk )
        if nums[k:]:
            for i in nums[k:]:
                if i > self.heapque[0]:
                    heapq.heappop(self.heapque)
                    heapq.heappush(self.heapque, i)

    def add(self, val: int) -> int:
        """
        :type val: int
        :rtype: int
        """
        if len(self.heapque) < self.k:
            # O( log(k) )
            heapq.heappush(self.heapque, val)
        elif val > self.heapque[0]:
            # O( log(k) )
            heapq.heappop(self.heapque)
            heapq.heappush(self.heapque, val)

        if len(self.heapque) < self.k:
            return -1
        return self.heapque[0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_k_th_largestElementInStream(self) -> None:
        k_th_largest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(4, k_th_largest.add(3))
        self.assertEqual(5, k_th_largest.add(5))
        self.assertEqual(5, k_th_largest.add(10))
        self.assertEqual(8, k_th_largest.add(9))
        self.assertEqual(8, k_th_largest.add(4))


if __name__ == "__main__":
    unittest.main()
