#
# Time : O(Nlogk); Space: O(N)
# @tag : Hashing ; Heap/PriorityQueue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 347: Top K Frequent Elements
#
# Description:
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
# Note:
#
#   * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#   * Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#   * It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
#   * You can return the answer in any order.
#
# **************************************************************************
# Source: https://leetcode.com/problems/top-k-frequent-elements/ (Leetcode - Problem 347 - Top K Frequent Elements)
#         https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times/0 (GeeksForGeeks - First element to occur k times)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Time: O(Nlogk)
# Space: O(N)
#
# 1. Build a frequency dictionary (freq is positive)
# 2. Build a heap
# 3. Make sure heap conatins k items at maximum by popping out the items with least frequency as you push to heap
# 4. The time complexity of adding an element in a heap is O(log(k)) and we do it N times that means O(Nlog(k)) time complexity for this step.
# 5. Heap now contains k items (the desired output basically)
# 6. Pop and append to the output list - O(klog(k))
# 7. return list [ reverse the list since heappop() will pop smallest first ]
#
# NOTE: you need reverse the res list before returning. Since heappop() will pop smallest first.
# **************************************************************************
#
from typing import List

import heapq

import unittest

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # to store frequency of occurence of every element
        frequencyMap = {}

        for i in range(len(nums)):
            frequencyMap[nums[i]] = frequencyMap.get(nums[i], 0) + 1

        # creating maxHeap from frequencyMap
        elements = [(-frequencyMap[key], key) for key in frequencyMap]

        heapq.heapify(elements)

        # getting k most frequent elements
        ans = [heapq.heappop(elements)[-1] for _ in range(k)]

        return ans

    def topKFrequentGFG(self, nums: List[int], k: int) -> int:
        # to store frequency of occurence of every element
        frequencyMap = {}

        for i in range(len(nums)):
            frequencyMap[nums[i]] = frequencyMap.get(nums[i], 0) + 1

        # creating maxHeap from frequencyMap
        elements = [(-frequencyMap[key], key) for key in frequencyMap]

        heapq.heapify(elements)

        # getting k most frequent elements
        ans = [heapq.heappop(elements)[-1] for _ in range(k)]

        return ans[0]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_topKFrequent(self) -> None:
        sol = Solution()
        for nums, k, solution in (
                [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
                [[1], 1, [1]],
                [[1, 7, 4, 3, 4, 8, 7], 2, [4, 7]]
        ):
            self.assertEqual(
                solution,
                sol.topKFrequent(nums, k),
                "Should return the minimum window in S which will contain all the characters in T"
            )

    def test_topKFrequentGFG(self) -> None:
        sol = Solution()
        for nums, k, solution in (
                [[1, 1, 1, 2, 2, 3], 2, 1],
                [[1], 1, 1],
                [[1, 7, 4, 3, 4, 8, 7], 2, 4]
        ):
            self.assertEqual(
                solution,
                sol.topKFrequentGFG(nums, k),
                "Should return the minimum window in S which will contain all the characters in T"
            )

if __name__ == "__main__":
    unittest.main()
