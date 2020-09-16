#
# Time : O(N); Space: O(N)
#
# Time O(N) for one pass
# Space O(N) in worst case
#
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 503: Next Greater Element I
#
# Description:
#
# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
#
# Note: The length of given array won't exceed 10000.
#
# **************************************************************************
# Source: https://leetcode.com/problems/next-greater-element-ii/ (Leetcode - Problem 503 - Next Greater Element II)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# First ignore that it's a circular array. Then the code is almost the same except that stack should be initisalized as an emplty stack:
#
# class Solution(object):
#     def nextGreaterElements(self, nums):
#         n = len(nums)
#         ret = [-1] * n
#         stack1 = []
#         # stack = nums[::-1]
#         for i in range(n - 1, -1, -1):
#             while stack1 and stack1[-1] <= nums[i]:
#                 stack1.pop()
#             if stack1:
#                 ret[i] = stack1[-1]
#             stack1.append(nums[i])
#         return ret
# Then consider the circular condition. When stack1 is empty, we still could try to find the next greater element from the begining of the array. The code is like this:
#
# class Solution(object):
#     def nextGreaterElements(self, nums):
#         n = len(nums)
#         ret = [-1] * n
#         stack1 = []
#         stack2 = nums[::-1]
#         for i in range(n - 1, -1, -1):
#             while stack1 and stack1[-1] <= nums[i]:
#                 stack1.pop()
#             if stack1:
#                 ret[i] = stack1[-1]
#             else:
#                 while stack2 and stack2[-1] <= nums[i]:
#                     stack2.pop()
#                 if stack2:
#                     ret[i] = stack2[-1]
#             stack1.append(nums[i])
#         return ret
#
# But there's no need to distinguish stack1 and stack2, so the original code follows, which as given below:
#
# class Solution(object):
#     def nextGreaterElements(self, nums):
#         n = len(nums)
#         ret = [-1] * n
#         stack = nums[::-1]
#         for i in range(n - 1, -1, -1):
#             while stack and stack[-1] <= nums[i]:
#                 stack.pop()
#             if stack:
#                 ret[i] = stack[-1]
#             stack.append(nums[i])
#         return ret
#
from typing import List
import unittest


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            stack.append(nums[i])
        return ret


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_nextGreaterElements(self) -> None:
        s = Solution()
        nums = [1, 2, 1]
        expected = [2, -1, 2]
        self.assertEqual(
            expected,
            s.nextGreaterElements(nums),
            "Should return the Next Greater Number for every element in a circular array",
        )


if __name__ == "__main__":
    unittest.main()
