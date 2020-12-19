# Time  :
# Space :
# @tag : String
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
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/top-k-frequent-elements/ (LeetCode - Problem 347 - Top K Frequent Elements)
#
#
from typing import List
from collections import Counter
from collections import defaultdict
from itertools import chain

import unittest


class Solution:

    # Solution 1: Using Counter
    def topKFrequent_solution_1(self, nums: List[int], k: int) -> List[int]:
        result = []

        # Our counter pairs are sorted in ascending order in terms of their frequency
        counter = sorted(Counter(nums).items(), key=lambda pair: pair[1])

        # Add k most frequent values into result
        for i in range(k):
            result.append(counter.pop()[0])
        return result

    def topKFrequent_solution_1_concise(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda pair: pair[1], reverse=True)
        return [k for k, v in counter[:k]]

    # Solution 2: Using Bucket Sort
    def topKFrequent_solution_2(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()
        for num, freq in Count:
            bucket[freq].append(num)
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

    # Solution 3: Using Bucket Sort
    def topKFrequent_solution_3(self, nums: List[int], k: int) -> List[int]:
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k:
                return res[:k]

        return res[:k]

    # Solution 3: Using Bucket Sort - slightly faster approach
    #
    # Instead of the range(len(nums)) on the second loop,
    # I am starting on the largest count, which can save up some computation and on the return,
    # instead of slicing always, only slicing for the case that the size is bigger than k
    def topKFrequent_solution_3_slightly_faster(
        self, nums: List[int], k: int
    ) -> List[int]:
        frequency = defaultdict(list)
        bigger = 0
        for num, count in Counter(nums).items():
            frequency[count].append(num)
            bigger = max(bigger, count)

        result = []
        for times in range(bigger, 0, -1):
            result.extend(frequency[times])
            if len(result) >= k:
                break

        return result if len(result) == k else result[:k]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_topKFrequent(self) -> None:
        sol = Solution()
        for nums, k, solution in ([[1, 1, 1, 2, 2, 3], 2, [1, 2]], [[1], 1, [1]]):
            self.assertEqual(solution, sol.topKFrequent_solution_1(nums, k))
            self.assertEqual(solution, sol.topKFrequent_solution_1_concise(nums, k))
            self.assertEqual(solution, sol.topKFrequent_solution_2(nums, k))
            self.assertEqual(solution, sol.topKFrequent_solution_3(nums, k))
            self.assertEqual(
                solution, sol.topKFrequent_solution_3_slightly_faster(nums, k)
            )


if __name__ == "__main__":
    unittest.main()
