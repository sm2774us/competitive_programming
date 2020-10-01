#
# Time : O(N); Space: O(1)
# @tag : Hashing
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 128: Longest Consecutive Sequence
#
# Description:
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-consecutive-sequence/ (Leetcode - Problem 128 -. Longest Consecutive Sequence)
#         https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/0 (GeeksForGeeks - Longest consecutive subsequence)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# 1. Each section marks its start and end.
# 2. Given n, get its neighbouring sections (n == section.max+1 or n == section.min-1) in Hashmap in O(1) and meanwhile update their start and end.
# 3. Finally return the max length of sections;
#
from typing import List

import unittest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        unions = {}
        maxlen = 0
        for n in nums:
            # if unions.__contains__(n):  # duplicate n, skip
            # or more pythonic
            # [ Time Complexity for 'in' statement => { lists - Average: O(n) ; set/dict - Average: O(1), Worst: O(n) } ]
            if n in unions.keys():
                continue
            start = end = n
            # if unions.__contains__(n + 1):  # update end if has bigger neighbouring section
            # or more pythonic
            # [ Time Complexity for 'in' statement => { lists - Average: O(n) ; set/dict - Average: O(1), Worst: O(n) } ]
            if (n + 1) in unions.keys():
                end = unions[n + 1][1]
            # if unions.__contains__(n - 1):  # update start if has smaller neighbouring section
            # or more pythonic
            # [ Time Complexity for 'in' statement => { lists - Average: O(n) ; set/dict - Average: O(1), Worst: O(n) } ]
            if (n - 1) in unions.keys():
                start = unions[n - 1][0]
            unions[start] = unions[end] = unions[n] = (start, end)
            maxlen = max(end - start + 1, maxlen)
        return maxlen


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestConsecutive(self) -> None:
        sol = Solution()
        self.assertEqual(4, sol.longestConsecutive([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    unittest.main()
