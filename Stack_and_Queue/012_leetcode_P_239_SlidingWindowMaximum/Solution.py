#
# Leetcode - Problem 239 - Sliding Window Maximum
# **************************************************************************
# Google Interview Variant - { Google | OA 2019 | Largest Subarray Length K }
# Time : O(N); Space: O(1)          [ Values are Unique ]
# Time : O(NK) time; Space: O(1)    [ Values are Non-Unique ]
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 239: Sliding Window Maximum
#
# Description:
#
# You are given an array of integers nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Example 3:
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# Example 4:
#
# Input: nums = [9,11], k = 2
# Output: [11]
# Example 5:
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
#
# Constraints:
#
#   * 1 <= nums.length <= 105
#   * -104 <= nums[i] <= 104
#   * 1 <= k <= nums.length
#
# **************************************************************************
# Source: https://leetcode.com/problems/sliding-window-maximum/ ( Leetcode - Problem 239 - Sliding Window Maximum )
#         https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0 (GeeksForGeeks - Maximum of all subarrays of size k)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
#
# Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing, and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.
#
# For each index i:
#
#   1. Pop (from the end) indexes of smaller elements (they'll be useless).
#   2. Append the current index.
#   3. Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
#   4. If our window has reached size k, append the current window maximum to the output.
#
from typing import List
from collections import deque

import unittest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        return res

    def largest_subarrayGoogleVariant(self, a, k):
        # store first starting index for a subarray as the largest, since 'a' will always be <= 'k'
        first_idx = 0
        # check indices where a subarray of size k can be made
        for x in range(1, len(a) - k + 1):
            # replace the largest first index if a larger value is found
            if a[first_idx] < a[x]:
                first_idx = x

        # return subarray starting at that largest possible first index with size k
        return a[first_idx : first_idx + k]

    def largest_subarray_non_unique_GoogleVariant(self, a, k):
        first_idx = 0
        for x in range(1, len(a) - k + 1):
            # compare values at each index for the would be sub arrays
            for i in range(k):
                # replace the largest index and break out of the inner loop is larger value is found
                if a[first_idx + i] < a[x + i]:
                    first_idx = x
                    break
                # if the current stored largest subarray is larger than the current subarray, move on
                elif a[first_idx + i] > a[x + i]:
                    break

        return a[first_idx : first_idx + k]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxSlidingWindow(self) -> None:
        s = Solution()
        for a, k, solution in (
            [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
            [[1], 1, [1]],
            [[1, -1], 1, [1, -1]],
            [[9, 11], 2, [11]],
            [[4, -2], 2, [4]],
        ):
            self.assertEqual(
                solution,
                s.maxSlidingWindow(a, k),
                "Should return the max sliding window ( or maximum of all subarrays of size K )",
            )

    def test_largest_subarrayGoogleVariant(self) -> None:
        s = Solution()
        for a, k, solution in (
            [[1, 4, 3, 2, 5], 4, [4, 3, 2, 5]],
            [[1, 4, 3, 2, 5], 3, [4, 3, 2]],
            [[10, 1, 4, 3, 2, 5], 2, [10, 1]],
        ):
            self.assertEqual(
                solution,
                s.largest_subarrayGoogleVariant(a, k),
                "Should return the largest subarray of length K",
            )
        # assert (s.largest_subarrayGoogleVariant([1, 4, 3, 2, 5], 4) == [4, 3, 2, 5])
        # assert (s.largest_subarrayGoogleVariant([1, 4, 3, 2, 5], 3) == [4, 3, 2])
        # assert (s.largest_subarrayGoogleVariant([10, 1, 4, 3, 2, 5], 2) == [10, 1])

    def test_largest_subarray_non_unique_GoogleVariant(self) -> None:
        s = Solution()
        for a, k, solution in (
            [[1, 4, 3, 2, 5], 4, [4, 3, 2, 5]],
            [[1, 4, 3, 2, 5], 3, [4, 3, 2]],
            [[10, 1, 4, 3, 2, 5], 2, [10, 1]],
        ):
            self.assertEqual(
                solution,
                s.largest_subarray_non_unique_GoogleVariant(a, k),
                "Should return the largest subarray of length K",
            )
        # assert (s.largest_subarray_non_unique_GoogleVariant([1, 4, 3, 2, 5], 4) == [4, 3, 2, 5])
        # assert (s.largest_subarray_non_unique_GoogleVariant([1, 4, 3, 2, 5], 3) == [4, 3, 2])
        # assert (s.largest_subarray_non_unique_GoogleVariant([10, 1, 4, 3, 2, 5], 2) == [10, 1])


if __name__ == "__main__":
    unittest.main()
