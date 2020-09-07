#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given a sorted array of positive integers. Your task is to rearrange  the array elements alternately i.e
# first element should be max value, second should be min value, third should be second max, fourth
# should be second min and so on...
#
# Note: O(1) extra space is allowed. Also, try to modify the input array as required.
#
# Input:
# An array.
#
# Output:
# Output the modified array with alternated elements.
#
# Example:
#
# Given input            => [1, 2, 3, 4]
#       output should be => [4, 1, 3, 2]
#
# Constraints:
# 1 <=T<= 100
# 1 <=N<= 107
# 1 <=arr[i]<= 107
#
# **************************************************************************
#
# Explanation
#
# Given input            => [1, 2, 3, 4]
#       output should be => [4, 1, 3, 2]
#
# What it does, step by step. first, reversed():
#
# >>> list(reversed(nums))
# [4, 3, 2, 1]
# Then zip():
#
# >>> list(zip([4, 3, 2, 1], [1, 2, 3, 4]))
# [(4, 1), (3, 2), (2, 3), (1, 4)]
# You can see we have almost the list we want, we have a problem: these are tuples. we want to flatten them.
#
# >>> (4, 1) + (3, 2) + (2, 3) + (1, 4)
# (4, 1, 3, 2, 2, 3, 1, 4)
# Oh. That's nice. But how to do it inside the list? Simple: use sum(), which does exactly this - adding many things together. Only we need to give it something to start with - an empty tuple ():
#
# >>> sum([(4, 1), (3, 2), (2, 3), (1, 4)], ())
# (4, 1, 3, 2, 2, 3, 1, 4)
# But the we don't want the second half, so let's remove it. We know he list is exactly twice too long, yes?
#
# >>> (4, 1, 3, 2, 2, 3, 1, 4)[:len(nums)]
# (4, 1, 3, 2)
# That's it.
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/ ( Rearrange arrays alternately )
#
# Solution Hint: https://stackoverflow.com/questions/17436870/python-alternating-elements-of-a-sorted-array
#
from typing import List

import unittest

class Solution:
    def rearrange(self, nums: List[int]) -> List[int]:
        return list(sum(zip(reversed(nums), nums), ())[:len(nums)])

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_rearrange(self) -> None:
        s = Solution()
        for nums, solution in (
                [[1,2,3,4,5,6], [6,1,5,2,4,3]],
                [[1,2,3,4], [4,1,3,2]],
                [[1,2,3,4,5], [5,1,4,2,3]]
        ):
            self.assertEqual(solution, s.rearrange(nums), "Should return the array with the elements rearranged alternately")


if __name__ == '__main__':
    unittest.main()